
import pandas as pd
import random
from config.settings import (
    FEATURES,
    TARGET_COLUMN,
    MAX_QUESTIONS
)

from engine.decision_tree import get_best_question


def initialize_game(data):
    """Create a fresh game state."""

    required_columns = [TARGET_COLUMN] + FEATURES

    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Dataset is missing columns: {missing_columns}"
        )
    rng = random.Random()

    tie_breakers = {
        name: rng.random()
        for name in data[TARGET_COLUMN].tolist()
    }
    return {
        "all_candidates": data.copy(),
        "candidates": data.copy(),
        "asked_features": [],
        "answers": {},
        "question_count": 0,
        "status": "playing",
        "current_guess": None,
        "rejected_guesses": [],
        "candidate_scores": {},
        "tie_breakers": tie_breakers,
    }



def rank_candidates(state):
    """
    Rank characters using weighted answer matching.

    Informative features receive more weight.
    Rejected guesses are never considered.
    Ties are broken randomly per game, not by CSV order.
    """

    candidates = state["candidates"].copy()
    original = state["all_candidates"]
    answers = state["answers"]

    definite_answers = {
        feature: answer
        for feature, answer in answers.items()
        if answer is not None
    }

    if candidates.empty:
        state["candidate_scores"] = {}
        return candidates

    # Calculate how informative each feature is.
    weights = {}

    for feature in definite_answers:
        probabilities = original[feature].value_counts(
            normalize=True
        )

        entropy = 0.0

        for probability in probabilities:
            if probability > 0:
                import math
                entropy -= probability * math.log2(probability)

        weights[feature] = entropy

    total_weight = sum(weights.values())

    scores = []

    for _, candidate in candidates.iterrows():

        weighted_score = 0.0

        for feature, answer in definite_answers.items():

            weight = weights[feature]

            if candidate[feature] == answer:
                weighted_score += weight
            else:
                weighted_score -= weight

        if total_weight > 0:
            percentage = (
                (weighted_score + total_weight)
                / (2 * total_weight)
            ) * 100
        else:
            percentage = 50.0

        scores.append(percentage)

    candidates["_match_score"] = scores

    # Break ties independently of CSV row order.
    candidates["_tie_breaker"] = candidates[
        TARGET_COLUMN
    ].map(state["tie_breakers"])

    candidates = candidates.sort_values(
        by=["_match_score", "_tie_breaker"],
        ascending=[False, False]
    )

    state["candidate_scores"] = {
        row[TARGET_COLUMN]: round(row["_match_score"], 1)
        for _, row in candidates.iterrows()
    }

    return candidates.drop(
        columns=["_match_score", "_tie_breaker"]
    )


def prepare_guess(state):
    """Prepare the highest-ranked candidate as a guess."""

    if state["candidates"].empty:
        state["status"] = "no_match"
        state["current_guess"] = None
        return

    ranked = rank_candidates(state)

    state["candidates"] = ranked

    state["current_guess"] = (
        ranked.iloc[0][TARGET_COLUMN]
    )

    state["status"] = "confirm_guess"


def apply_answer(state, feature, answer):
    """Record an answer without strictly eliminating candidates."""

    if feature not in FEATURES:
        raise ValueError(f"Unknown feature: {feature}")

    if feature in state["asked_features"]:
        raise ValueError(f"Question already asked: {feature}")

    if answer not in (0, 1, None):
        raise ValueError("Answer must be 1, 0, or None.")

    if state["status"] != "playing":
        return state

    state["asked_features"].append(feature)
    state["answers"][feature] = answer
    state["question_count"] += 1

    # Recalculate rankings instead of eliminating candidates.
    rank_candidates(state)

    # Make a guess after the question limit.
    if state["question_count"] >= MAX_QUESTIONS:
        prepare_guess(state)

    # Also make a guess when every feature has been asked.
    elif len(state["asked_features"]) >= len(FEATURES):
        prepare_guess(state)

    return state


def confirm_guess(state, is_correct):
    """Accept or reject the current guess."""

    if state["status"] != "confirm_guess":
        return state

    if is_correct:
        state["status"] = "guessed"
        return state

    rejected_name = state["current_guess"]

    state["rejected_guesses"].append(rejected_name)

    state["candidates"] = state["candidates"][
        state["candidates"][TARGET_COLUMN] != rejected_name
    ].copy()

    state["current_guess"] = None

    if state["candidates"].empty:
        state["status"] = "no_match"
        return state

    rank_candidates(state)

    if (
        state["question_count"] >= MAX_QUESTIONS
        or len(state["asked_features"]) >= len(FEATURES)
    ):
        prepare_guess(state)
    else:
        state["status"] = "playing"

    return state


def get_next_question(state):
    """Choose the next question, using a fallback if needed."""

    if state["status"] != "playing":
        return None

    # First try the information-gain question selector.
    best_feature = get_best_question(
        state["candidates"],
        state["asked_features"]
    )

    if best_feature is not None:
        return best_feature

    # Fallback: ask the next unanswered feature.
    for feature in FEATURES:
        if feature not in state["asked_features"]:
            return feature

    # No questions remain.
    prepare_guess(state)
    return None


def get_remaining_candidates(state):
    """Return candidates in ranking order."""

    ranked = rank_candidates(state)

    return ranked[TARGET_COLUMN].tolist()


def get_best_guess(state):
    """Return the current guess."""

    if state["status"] in ("confirm_guess", "guessed"):
        return state["current_guess"]

    return None


def get_game_status(state):
    """Return current game statistics."""

    return {
        "status": state["status"],
        "question_count": state["question_count"],
        "remaining_candidates": len(state["candidates"]),
        "current_guess": state["current_guess"],
        "rejected_guesses": len(state["rejected_guesses"])
    }
