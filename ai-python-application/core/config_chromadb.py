from pydantic_settings import BaseSettings, SettingsConfigDict

class ChromaDBSettings(BaseSettings):
    DATA_PATH: str 
    EMBED_MODEL: str 
    
    model_config = SettingsConfigDict(
        env_prefix="CHROMADB_",
        env_file=".env",
        env_file_encoding="utf-8"
    )
    
config = ChromaDBSettings()