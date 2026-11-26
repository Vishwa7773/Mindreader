
import math

from config.settings import FEATURES


# --------------------------------------------------
# QUESTION GROUPS
# --------------------------------------------------

QUESTION_GROUPS = {
    "identity": [
        "is_real",
        "is_human",
        "is_animal",
        "is_fictional",
        "is_animated"
    ],

    "indian_cinema": [
        "is_from_indian_cinema",
        "is_actor",
        "is_actress",
        "is_musician",
        "is_film_director",
        "is_film_producer",
        "is_film_composer",
        "is_playback_singer"
    ],

    "film_industry": [
        "is_from_bollywood",
        "is_from_tamil_cinema",
        "is_from_telugu_cinema",
        "is_from_malayalam_cinema",
        "is_from_kannada_cinema",
        "is_from_bengali_cinema",
        "is_from_marathi_cinema",
        "is_from_punjabi_cinema"
    ],

    "entertainment": [
        "is_from_movie",
        "is_from_tv",
        "is_from_anime",
        "is_from_video_game"
    ],

    "profession": [
        "is_musician",
        "is_athlete",
        "is_politician"
    ],

    "fictional_traits": [
        "is_superhero",
        "has_superpowers",
        "is_villain",
        "wears_costume",
        "has_magic",
        "is_detective",
        "is_robot",
        "uses_weapon"
    ],

    "animal_traits": [
        "is_mammal",
        "can_fly"
    ]
}


def calculate_entropy(values):
    """Calculate Shannon entropy."""

    probabilities = values.value_counts(normalize=True)

    entropy = 0.0

    for probability in probabilities:
        entropy -= probability * math.log2(probability)

    return entropy


def calculate_information_gain(candidates, feature):
    """Calculate information gain for a binary question."""

    if candidates.empty:
        return 0.0

    if feature not in candidates.columns:
        return 0.0

    if candidates[feature].nunique() <= 1:
        return 0.0

    parent_entropy = calculate_entropy(candidates["name"])

    total = len(candidates)
    weighted_entropy = 0.0

    for answer in (0, 1):

        subset = candidates[
            candidates[feature] == answer
        ]

        if subset.empty:
            continue

        weight = len(subset) / total

        child_entropy = calculate_entropy(
            subset["name"]
        )

        weighted_entropy += weight * child_entropy

    return max(
        0.0,
        parent_entropy - weighted_entropy
    )



def get_active_group(answers):

    # Real people
    if answers.get("is_real") == 1:

        # Indian cinema
        if answers.get("is_from_indian_cinema") == 1:

            # Once actor/actress is established,
            # identify their film industry.
            if (
                answers.get("is_actor") == 1
                or answers.get("is_actress") == 1
            ):
                return "film_industry"

            return "indian_cinema"

        return "profession"

    # Animals
    if answers.get("is_animal") == 1:
        return "animal_traits"

    # Fictional characters
    if answers.get("is_fictional") == 1:

        if answers.get("is_animated") == 1:
            return "entertainment"

        return "fictional_traits"

    if answers.get("is_human") == 1:
        return "profession"

    return "identity"



def get_question_statistics(candidates, asked_features):
    """Calculate information gain for eligible questions."""

    statistics = {}

    for feature in FEATURES:

        if feature in asked_features:
            continue

        if feature not in candidates.columns:
            continue

        if candidates[feature].nunique() <= 1:
            continue

        statistics[feature] = calculate_information_gain(
            candidates,
            feature
        )

    return dict(
        sorted(
            statistics.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )


def get_best_question(candidates, asked_features, answers=None):
    """
    Choose the best context-aware question.

    First select an appropriate question group.
    Then use information gain within that group.
    """

    if candidates.empty:
        return None

    if answers is None:
        answers = {}

    statistics = get_question_statistics(
        candidates,
        asked_features
    )

    if not statistics:
        return None

    active_group = get_active_group(answers)

    preferred_features = QUESTION_GROUPS.get(
        active_group,
        FEATURES
    )

    eligible_questions = {
        feature: gain
        for feature, gain in statistics.items()
        if feature in preferred_features
    }

    if eligible_questions:

        return max(
            eligible_questions,
            key=eligible_questions.get
        )

    # Fallback: use the strongest remaining question.
    return max(
        statistics,
        key=statistics.get
    )
