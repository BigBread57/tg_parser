# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.message import Message  # noqa
from app.models.channel import Channel  # noqa
