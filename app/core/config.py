from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Achadinhos API"
    app_version: str = "0.1.0"

    model_config = SettingsConfigDict(env_prefix="ACHADINHOS_")


settings = Settings()
