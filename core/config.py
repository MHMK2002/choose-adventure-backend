from dotenv import load_dotenv
from pydantic import field_validator
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_PREFIX: str = '/api/v1'
    DEBUG: bool = False

    DATABASE_URL: str
    ALLOWED_ORIGINS: str = ''
    OPENAI_API_KEY: str
    OPENAI_API_BASE: str

    @field_validator('ALLOWED_ORIGINS')
    def parse_allowed_origins(cls, v: str) -> list[str]:
        if not v:
            return []
        return [origin.strip() for origin in v.split(',')]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True


settings = Settings()  # type: ignore
