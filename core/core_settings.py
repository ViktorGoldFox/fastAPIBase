from pydantic_settings import BaseSettings

class api_setting(BaseSettings):
    reload: bool = True # Auto app reload when edit project file
    host: str = '127.0.0.1' # Host of place app. For product mode host placement: '0.0.0.0'
    port: int = 8000 #Port of place app


class db_setting(BaseSettings):
    db_path: str = 'database.db' # Path to database file example: database.db (sqlite3)
    url: str = f'sqlite+aiosqlite:///{db_path}' # Select lib of the db
    echo: bool = False # DataBase logs
    autoflush: bool = False #automatic flush call which occurs
    expire_on_commit: bool = False # ХЗ

class settings(BaseSettings):
    api: api_setting = api_setting()
    db: db_setting = db_setting()

