GAME_MODES = ["osu", "taiko", "mania", "fruits"]

SCHEMAS = { mode : f"{mode}_schema.sql" for mode in GAME_MODES}

TABLES = { mode : f"{mode}_country_rankings" for mode in GAME_MODES}

CURRENT_MODE = "osu"

CRAWLER_NAME = "country_rankings"

START_PAGE = 1
END_PAGE = 2
DATABASE = "osu.db"


def change_current_mode(mode):
    CURRENT_MODE = mode