"""Конфигурация приложения через переменные окружения."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Настройки приложения."""

    postgres_connection_string: str

    @property
    def database_url(self) -> str:
        """URL для подключения к БД через asyncpg."""
        return self.postgres_connection_string.replace(
            'postgresql://', 'postgresql+asyncpg://',
        )


settings = Settings()
