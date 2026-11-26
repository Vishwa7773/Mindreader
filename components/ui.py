
import streamlit as st

from config.settings import (
    GAME_NAME,
    GAME_DESCRIPTION,
    QUESTIONS,
    MAX_QUESTIONS
)


def render_header():
    """Display the game title and description."""

    st.markdown(
        f'<div class="main-title"> {GAME_NAME}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="subtitle">{GAME_DESCRIPTION}</div>',
        unsafe_allow_html=True
    )


def render_game_statistics(state):
    """Display question count and remaining candidates."""

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-number">
                    {state['question_count']}/{MAX_QUESTIONS}
                </div>
                <div class="info-label">Questions Asked</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-number">
                    {len(state['candidates'])}
                </div>
                <div class="info-label">Possible Characters</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    progress = min(
        state["question_count"] / MAX_QUESTIONS,
        1.0
    )

    st.progress(progress)


def render_question(feature):
    """Display the next decision-tree question."""

    question = QUESTIONS.get(
        feature,
        "Can you tell me something about your character?"
    )

    st.markdown(
        f"""
        <div class="question-card">
            <div style="color:#a5b4fc; font-size:0.9rem;">
                THINK CAREFULLY...
            </div>
            <div class="question-text">
                {question}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )



def render_answer_buttons():
    """Display Yes, No and Not Sure buttons."""

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Yes", key="answer_yes",
                     use_container_width=True):
            return 1

    with col2:
        if st.button("No", key="answer_no",
                     use_container_width=True):
            return 0

    with col3:
        if st.button("Not Sure", key="answer_unknown",
                     use_container_width=True):
            return None

    return "no_answer"


def render_success(guess):
    """Display the successful character prediction."""

    st.balloons()

    st.markdown(
        f"""
        <div class="question-card">
            <div style="font-size:3rem;">🎯</div>
            <div style="font-size:1.1rem; color:#a5b4fc;">
                I THINK I KNOW YOUR CHARACTER!
            </div>
            <div style="font-size:2.3rem; font-weight:800; color:white;">
                {guess}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_no_match():
    """Display a message when no candidates remain."""

    st.warning(
        "I couldn't find a matching character. "
        "Your character may not be in my dataset."
    )


def render_candidate_options(candidates):
    """Show remaining candidates when the game cannot decide."""

    st.subheader("Possible characters")

    for candidate in candidates[:10]:
        st.write(f"• {candidate}")

    if len(candidates) > 10:
        st.caption(
            f"And {len(candidates) - 10} more possibilities..."
        )


def render_restart_button():
    """Display a restart button."""

    return st.button(
        "🔄 Play Again",
        use_container_width=True,
        key="restart_game"
    )
