
import streamlit as st
import pandas as pd

from config.settings import (
    GAME_NAME,
    GAME_DESCRIPTION,
    DATASET_PATH
)

from components.styles import load_css

from components.ui import (
    render_header,
    render_game_statistics,
    render_question,
    render_answer_buttons,
    render_success,
    render_no_match,
    render_candidate_options,
    render_restart_button
)

from engine.game_logic import (
    initialize_game,
    apply_answer,
    confirm_guess,
    get_next_question,
    get_remaining_candidates,
    get_best_guess
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title=GAME_NAME,
    layout="centered"
)

load_css()


# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

@st.cache_data
def load_character_data():
    return pd.read_csv(DATASET_PATH)


character_data = load_character_data()


# --------------------------------------------------
# INITIALIZE GAME
# --------------------------------------------------

if "game_state" not in st.session_state:
    st.session_state.game_state = initialize_game(
        character_data
    )


def restart_game():
    """Start a completely new game."""

    st.session_state.game_state = initialize_game(
        character_data
    )


# --------------------------------------------------
# HEADER AND STATISTICS
# --------------------------------------------------

render_header()
render_game_statistics(st.session_state.game_state)

state = st.session_state.game_state


# --------------------------------------------------
# PLAYING MODE
# --------------------------------------------------

if state["status"] == "playing":

    next_feature = get_next_question(state)

    if next_feature is not None:

        render_question(next_feature)

        answer = render_answer_buttons()

        if answer != "no_answer":

            apply_answer(
                state,
                next_feature,
                answer
            )

            st.rerun()

    else:

        st.warning(
            "MindReader cannot find another useful question."
        )

        st.write("Remaining possible characters:")

        render_candidate_options(
            get_remaining_candidates(state)
        )


# --------------------------------------------------
# GUESS CONFIRMATION MODE
# --------------------------------------------------

elif state["status"] == "confirm_guess":

    guess = get_best_guess(state)

    st.markdown(
        """
        <div class="question-card">
            <div class="question-text">
                I think I know your character!
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h2 style='text-align:center'>{guess}</h2>",
        unsafe_allow_html=True
    )

    st.write("Did I guess correctly?")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Yes, that's correct!",
            use_container_width=True
        ):

            confirm_guess(state, True)
            st.rerun()

    with col2:

        if st.button(
            "No, try again",
            use_container_width=True
        ):

            confirm_guess(state, False)
            st.rerun()


# --------------------------------------------------
# SUCCESS MODE
# --------------------------------------------------

elif state["status"] == "guessed":

    render_success(
        get_best_guess(state)
    )

    render_restart_button()


# --------------------------------------------------
# NO MATCH MODE
# --------------------------------------------------

elif state["status"] == "no_match":

    render_no_match()

    st.info(
        "MindReader could not identify your character. "
        "The character may not be in the current dataset."
    )

    render_restart_button()


# --------------------------------------------------
# QUESTION LIMIT MODE
# --------------------------------------------------

elif state["status"] == "limit_reached":

    st.warning(
        "MindReader reached its question limit!"
    )

    st.write("Here are the remaining possibilities:")

    render_candidate_options(
        get_remaining_candidates(state)
    )

    render_restart_button()


# --------------------------------------------------
# RESTART BUTTON
# --------------------------------------------------

if state["status"] not in (
    "guessed",
    "no_match",
    "limit_reached"
):

    st.divider()

    if st.button(
        "🔄 Restart Game",
        use_container_width=True
    ):

        restart_game()
        st.rerun()
