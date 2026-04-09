from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = Field(
        default="", description="optional override for full DB URL"
    )

    model_config = SettingsConfigDict(
        env_file=".env", extra="allow"
    )

    @property
    def get_database_url(self) -> str:
        if self.DATABASE_URL and self.DATABASE_URL.startswith("postgres://"):
            return self.DATABASE_URL.replace("postgres://", "postgresql://", 1)
        return self.DATABASE_URL

settings = Settings()