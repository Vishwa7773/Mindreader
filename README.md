# MindReader

MindReader is an interactive character-guessing game inspired by `Akinator`. It asks users a series of questions and uses decision-tree-based question selection to identify the character, celebrity or personality they have in mind.

The project currently focuses on Indian film personalities across multiple regional film industries, while also including fictional characters, international celebrities, athletes, musicians and animals.

The goal is to make the game smarter over time by improving its dataset, question selection and candidate-ranking system.

## Features

- **Adaptive questions:** Selects questions based on the remaining candidates and previous answers.
- **Decision-tree logic:** Uses information gain to identify useful questions.
- **Candidate ranking:** Ranks possible characters according to how closely they match the user's answers.
- **Guess confirmation:** Allows users to confirm or reject the AI's guess.
- **Fault-tolerant answers:** A wrong answer does not immediately eliminate the correct character.
- **Multiple categories:** Includes real people, fictional characters, celebrities and animals.
- **Indian cinema coverage:** Includes personalities from Bollywood, Tamil, Telugu, Malayalam, Kannada, Bengali, Marathi and Punjabi cinema.
- **Streamlit interface:** Provides an interactive web-based game.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Pandas | Dataset management and processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and decision-tree functionality |

## Project Structure

```text
mindreader/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── images/
│
├── components/
│   ├── __init__.py
│   ├── styles.py
│   └── ui.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── data/
│   ├── characters.csv
│   └── expand_data.py
│
└── engine/
    ├── __init__.py
    ├── decision_tree.py
    └── game_logic.py
```

## Getting Started

Follow these steps to run MindReader locally.

### 1. Clone the repository

```bash
git clone <repository-url>
```

Alternatively, download the project and extract it to your computer.

### 2. Navigate to the project directory

```bash
cd mindreader
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows Command Prompt:

```cmd
venv\Scripts\activate
```

For PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

Streamlit will start the application and provide a local URL, usually:

```text
http://localhost:8501
```

Open that address in your browser to play.

## How It Works

MindReader uses a combination of information gain, candidate filtering and ranking to identify the character a user has in mind.

### Question Selection

The game evaluates available questions and selects one that can help distinguish between the remaining candidates.

Questions are organized into groups such as:

- Identity
- Indian cinema
- Film industry
- Profession
- Entertainment
- Fictional character traits
- Animal traits

Previous answers help determine which group is most relevant.

### Candidate Ranking

Instead of permanently eliminating a character whenever an answer does not match, MindReader maintains possible candidates and ranks them using the answers provided.

This makes the game more tolerant of incorrect or uncertain answers.

### Guess Confirmation

Once the game reaches its guessing stage, it presents its highest-ranked candidate.

The user can confirm the guess or reject it. Rejected candidates are removed from subsequent guesses.

## Dataset

The character database is stored in:

```text
data/characters.csv
```

It contains character names, categories and binary attributes used by the question-selection and ranking systems.

The Indian cinema dataset covers several film industries:

- Bollywood
- Tamil cinema
- Telugu cinema
- Malayalam cinema
- Kannada cinema
- Bengali cinema
- Marathi cinema
- Punjabi cinema

The dataset can be expanded as more personalities and attributes are added.

To run the expansion script:

```bash
python data/expand_data.py
```

The dataset is a growing collection rather than a complete record of every Indian film personality.

## Configuration

Game settings are maintained in:

```text
config/settings.py
```

This file contains:

- Available character features
- Questions associated with those features
- Maximum question count
- Dataset location
- Decision-tree configuration

The question-selection and game-state logic are maintained separately in the `engine` directory.

## Current Development Status

MindReader is an actively developing project.

Current development focuses on:

- Improving the accuracy of character predictions.
- Expanding and validating the character database.
- Improving question relevance and sequencing.
- Reducing repeated or unhelpful questions.
- Improving candidate-ranking logic.
- Making the game learn from incorrect guesses.
- Improving the overall user experience.

The current candidate scores are matching scores, not calibrated probabilities of a prediction being correct.

## Future Improvements

Some planned improvements include:

- A larger and more accurate Indian cinema database.
- More detailed attributes for individual actors and personalities.
- Better confidence estimation.
- Learning from user corrections.
- More advanced question-selection algorithms.
- Improved visual design and gameplay.
- Persistent game statistics and user feedback.

## Contributing

Contributions and suggestions are welcome.

If you would like to improve MindReader, you can contribute by:

1. Adding new characters and verifying their attributes.
2. Improving the question-selection algorithm.
3. Improving candidate-ranking accuracy.
4. Reporting bugs and suggesting features.
5. Improving the interface and overall gameplay.

Please ensure that new dataset entries use the same feature structure as the existing CSV file.

**MindReader** is a project built around a simple idea: how intelligently can a program identify what someone is thinking of by asking the right questions?  

  

*The project and the idea is highy inspired by [akinator](https://en.akinator.com/). This is just a fun side project.*