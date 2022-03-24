from pydantic import PostgresDsn

from app.settings import config

SQLALCHEMY_DATABASE_URI = PostgresDsn.build(
    scheme=config('FASTAPI_DRIVER_NAME', default='postgresql', cast=str),
    user=config('FASTAPI_USERNAME', default='', cast=str),
    password=config('FASTAPI_PASSWORD', default='', cast=str),
    host=config('FASTAPI_HOST', default='localhost', cast=str),
    port=config('FASTAPI_PORT', default='localhost', cast=str),
    path=f"/{config('FASTAPI_DATABASE', default='parser', cast=str) or ''}",
)

FIRST_SUPERUSER = config('FIRST_SUPERUSER', default='admin', cast=str)
FIRST_SUPERUSER_PASSWORD = config('FIRST_SUPERUSER_PASSWORD', default='admin', cast=str)
