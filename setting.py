# configuration file
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App variables
    app_name: str = "Code 92 Internship Tracker"
    environment: str = "development"
    
    # Database variables
    db_driver: str
    db_username: str
    db_password: str
    db_host: str
    db_port: str
    db_database: str
    
    # Pydantic v2 syntax to automatically load from a .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Instantiate it once to be used across the app
settings = Settings()