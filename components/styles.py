import streamlit as st


def load_css():
    """
    Inject custom CSS into the Streamlit application.
    """

    css = """
    <style>

    /* Main application background */
    .stApp {
        background:
            radial-gradient(
                circle at top left,
                #243b64 0%,
                #111827 45%,
                #080d18 100%
            );

        color: #f8fafc;
    }

    /* Main content container */
    .block-container {
        max-width: 1050px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    /* Main heading */
    .main-title {
        font-size: 3.2rem;
        font-weight: 800;
        text-align: center;
        color: #ffffff;
        letter-spacing: -2px;
        margin-bottom: 0.2rem;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 1.05rem;
        color: #a5b4fc;
        margin-bottom: 2rem;
    }

    /* Question card */
    .question-card {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.2);
    }

    .question-text {
        font-size: 1.8rem;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.4;
    }

    /* Information cards */
    .info-card {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 14px;
        padding: 1.2rem;
        text-align: center;
    }

    .info-number {
        font-size: 1.8rem;
        font-weight: 800;
        color: #818cf8;
    }

    .info-label {
        font-size: 0.85rem;
        color: #cbd5e1;
    }

    /* Primary buttons */
    .stButton > button {
        width: 100%;
        min-height: 3rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        font-size: 1rem;
        font-weight: 700;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #a5b4fc;
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(99, 102, 241, 0.25);
    }

    /* Progress bar */
    .stProgress > div > div > div > div {
        background-color: #818cf8;
    }

    /* Text and labels */
    p, label, span {
        color: inherit;
    }

    /* Responsive heading */
    @media (max-width: 650px) {
        .main-title {
            font-size: 2.4rem;
        }

        .question-text {
            font-size: 1.35rem;
        }

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }

    </style>
    """

    st.markdown(css, unsafe_allow_html=True)
