from pydantic_settings import BaseSettings

class ApiSetting(BaseSettings):
    reload: bool = True # Auto App reload when edit project file
    host: str = '127.0.0.1' # Host of place App. For product mode host placement: '0.0.0.0'
    port: int = 8000 #Port of place App

class DBSetting(BaseSettings):
    db_path: str = 'database.db' # Path to DataBase file example: DataBase.db (sqlite3)
    url: str = f'sqlite+aiosqlite:///{db_path}' # Select lib of the db
    echo: bool = False # DataBase logs
    autoflush: bool = False #automatic flush call which occurs
    expire_on_commit: bool = False # ХЗ

class Settings(BaseSettings):
    api: ApiSetting = ApiSetting()
    db: DBSetting = DBSetting()

