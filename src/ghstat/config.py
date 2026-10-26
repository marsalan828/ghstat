from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="GHSTAT_")
    base_url: str = "https://api.github.com"
    timeout: float = 5.0
    token: str | None = None