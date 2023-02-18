from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    API_V1_URL: str
    RDB_URL: str
    STATISTIC_DB: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = '.env'


config = Settings()
