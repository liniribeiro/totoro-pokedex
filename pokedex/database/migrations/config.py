from alembic.config import Config

from pokedex.settings import DATABASE_URL, BASE_DIR

alembic_cfg = Config()
alembic_cfg.set_main_option('script_location', f"{BASE_DIR}/pokedex/database/migrations")
alembic_cfg.set_main_option('sqlalchemy.url', DATABASE_URL)
