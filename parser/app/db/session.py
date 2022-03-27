import typing

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util.compat import contextmanager

from app.settings.common import DATABASES

engine = create_engine(DATABASES, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# @contextmanager
# def session(**kwargs) -> typing.ContextManager[SessionLocal]:
#     """Provide a transactional scope."""
#     new_session = SessionLocal(**kwargs)
#     try:
#         yield new_session
#         new_session.commit()
#     except Exception:
#         new_session.rollback()
#         raise
#     finally:
#         new_session.close()
