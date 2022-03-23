from starlette.config import Config

config = Config(".env")

DATABASES = {
    'drivername': 'postgresql',
    'database': config('DATABASE'),
    'username': config('USERNAME'),
    'password': config('PASSWORD'),
    'host': config('HOST'),
    'port': config('PORT'),
}

FIRST_SUPERUSER = 'admin'
FIRST_SUPERUSER_PASSWORD = 'admin'
