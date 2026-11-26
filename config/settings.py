GAME_NAME = "MindReader"

GAME_DESCRIPTION = (
  "Think of any character, celebrity, or animal. Let AI guess who it is!"
)


YES = 1
NO = 0


FEATURES = [
  "is_real",
  "is_human",
  "is_animal",
  "is_fictional",
  "is_animated",
  "is_superhero",
  "has_superpowers",
  "is_villain",
  "is_from_movie",
  "is_from_tv",
  "is_from_anime",
  "is_from_video_game",
  "is_musician",
  "is_athlete",
  "is_politician",
  "wears_costume",
  "has_magic",
  "is_detective",
  "is_robot",
  "is_mammal",
  "can_fly",
  "uses_weapon",
  "is_actor",
  "is_actress",
  "is_from_indian_cinema",
  "is_from_bollywood",
  "is_from_tamil_cinema",
  "is_from_telugu_cinema",
  "is_from_malayalam_cinema",
  "is_from_kannada_cinema",
  "is_from_bengali_cinema",
  "is_from_marathi_cinema",
  "is_from_punjabi_cinema",
  "is_film_director",
  "is_film_producer",
  "is_film_composer",
  "is_playback_singer",
]


QUESTIONS = {
  "is_real": "Is your character a real person?",
  "is_human": "Is your character human?",
  "is_animal": "Is your character an animal?",
  "is_fictional": "Is your character fictional?",
  "is_animated": "Does your character come from animation?",
  "is_superhero": "Is your character a superhero?",
  "has_superpowers": "Does your character have superpowers?",
  "is_villain": "Is your character a villain?",
  "is_from_movie": "Is your character from a movie?",
  "is_from_tv": "Is your character from a TV show?",
  "is_from_anime": "Is your character from anime?",
  "is_from_video_game": "Is your character from a video game?",
  "is_musician": "Is your character a musician or singer?",
  "is_athlete": "Is your character a professional athlete?",
  "is_politician": "Is your character a politician?",
  "wears_costume": "Does your character wear a distinctive costume?",
  "has_magic": "Does your character use magic?",
  "is_detective": "Is your character a detective?",
  "is_robot": "Is your character a robot or AI?",
  "is_mammal": "Is your character a mammal?",
  "can_fly": "Can your character fly?",
  "uses_weapon": "Is your character associated with a weapon?",
  "is_actor": "Is this person an actor?",
  "is_actress": "Is this person an actress?",
  "is_from_indian_cinema": "Is this person associated with Indian cinema?",
  "is_from_bollywood": "Are they associated with Bollywood?",
  "is_from_tamil_cinema": "Are they associated with Tamil cinema?",
  "is_from_telugu_cinema": "Are they associated with Telugu cinema?",
  "is_from_malayalam_cinema": "Are they associated with Malayalam cinema?",
  "is_from_kannada_cinema": "Are they associated with Kannada cinema?",
  "is_from_bengali_cinema": "Are they associated with Bengali cinema?",
  "is_from_marathi_cinema": "Are they associated with Marathi cinema?",
  "is_from_punjabi_cinema": "Are they associated with Punjabi cinema?",
  "is_film_director": "Are they a film director?",
  "is_film_producer": "Are they a film producer?",
  "is_film_composer": "Are they a film composer?",
  "is_playback_singer": "Are they a playback singer?",
}


MAX_QUESTIONS = 30

MIN_CANDIDATES_FOR_QUESTION = 2

ANSWER_OPTIONS = ["Yes", "No", "Not sure"]


DATASET_PATH = "data/characters.csv"

TARGET_COLUMN = "name"

CATEGORY_COLUMN = "category"


TREE_CRITERION = "entropy"

TREE_MAX_DEPTH = 1

RANDOM_STATE = 42
