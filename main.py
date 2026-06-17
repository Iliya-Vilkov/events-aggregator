"""Агрегатор Events Provider — FastAPI приложение."""

from fastapi import FastAPI

app = FastAPI()


@app.get('/api/health')
async def health() -> dict[str, str]:
    """Проверка доступности сервиса."""
    return {'status': 'ok'}
