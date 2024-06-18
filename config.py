from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    tg_bot_token: str
    
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings() # type: ignore