from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_connection_string: str

    @property
    def database_url(self) -> str:
        return self.postgres_connection_string.replace(
            "postgresql://", "postgresql+asyncpg://"
        )


settings = Settings()
