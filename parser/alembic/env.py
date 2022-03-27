from __future__ import with_statement

import os

from logging.config import fileConfig
from pathlib import Path

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import engine_from_config
from sqlalchemy import pool

# Необходимо для загрузки переменных из .env файла
dotenv_path = os.path.join(
    Path(__file__).parent.parent.parent.joinpath('config'),
    '.env',
)
load_dotenv(dotenv_path)

# это объект Alembic Config, который предоставляет
# доступ к значениям в используемом файле .ini.
config = context.config

# Интерпретировать файл конфигурации для ведения журнала Python.
# Эта строка в основном настраивает регистраторы.
fileConfig(config.config_file_name)

# Добавление объекта MetaData моделей
# для поддержки 'автоматической генерации'
from app.db.base import Base  # noqa

target_metadata = Base.metadata


def get_url():
    """Предоставление корректного подключения к БД."""
    user = os.getenv('FASTAPI_DB_USERNAME', 'postgres')
    password = os.getenv('FASTAPI_DB_PASSWORD', '')
    server = os.getenv('FASTAPI_DB_HOST', 'localhost')
    port = os.getenv('FASTAPI_DB_PORT', 5432)
    db = os.getenv('FASTAPI_DATABASE', 'parser')
    return f'postgresql://{user}:{password}@{server}:{port}/{db}'


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """

    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={'paramstyle': 'named'},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration['sqlalchemy.url'] = get_url()
    connectable = engine_from_config(
        configuration,
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
