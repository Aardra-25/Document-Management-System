from pydantic_settings import BaseSettings, SettingsConfigDict


class GoogleGenAISettings(BaseSettings):
    google_genai_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow"
    )


google_genai_config = GoogleGenAISettings()