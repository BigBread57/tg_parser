import typing

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util.compat import contextmanager

from app.settings.common import config


engine = create_engine(URL.create(**config('DATABASES')), pool_pre_ping=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def session(**kwargs) -> typing.ContextManager[Session]:
    """Provide a transactional scope."""
    new_session = Session(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except Exception:
        new_session.rollback()
        raise
    finally:
        new_session.close()
