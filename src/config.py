"""Конфигурация приложения через переменные окружения."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Настройки приложения."""

    postgres_connection_string: str

    @property
    def database_url(self) -> str:
        """URL для подключения к БД через asyncpg."""
        url = self.postgres_connection_string
        if url.startswith('postgres://'):
            url = 'postgresql://' + url[len('postgres://'):]
        return url.replace('postgresql://', 'postgresql+asyncpg://')


settings = Settings()
