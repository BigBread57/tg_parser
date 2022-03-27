from pydantic import PostgresDsn

from app.settings import config

DATABASES = PostgresDsn.build(
    scheme=config('FASTAPI_DRIVER_NAME', default='postgresql', cast=str),
    user=config('FASTAPI_DB_USERNAME', default='', cast=str),
    password=config('FASTAPI_DB_PASSWORD', default='', cast=str),
    host=config('FASTAPI_DB_HOST', default='localhost', cast=str),
    port=config('FASTAPI_DB_PORT', default=5432, cast=str),
    path=f"/{config('FASTAPI_DATABASE', default='parser', cast=str) or ''}",
)

FIRST_SUPERUSER = config('FIRST_SUPERUSER', default='admin', cast=str)
FIRST_SUPERUSER_PASSWORD = config('FIRST_SUPERUSER_PASSWORD', default='admin', cast=str)
