from pydantic_settings import BaseSettings, SettingsConfigDict

class Keys(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )
    
    MONGO_DB_CONNECTOR: str
    OPENAI_API_KEY: str

keys = Keys()