from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    AZURE_DEPLOYMENT: str
    AZURE_API_VERSION: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ENDPOINT: str

    DATABASE_URL: str = "sqlite:///./hikayeapp.db"

    SECRET_KEY: str = "change_this_secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 365 #one year

    APP_NAME: str = "Hikayeapp Backend"
    DEBUG: bool = True

    
    model_config = SettingsConfigDict(env_file=".env",
                                      env_file_encoding="utf-8",
                                      extra="ignore"
                                      )


settings = Settings()
    
