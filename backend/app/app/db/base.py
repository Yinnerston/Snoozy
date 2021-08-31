# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.item import Item  # noqa
from app.models.user import User  # noqa
from app.models.group import Group # noqa
from app.models.channel import Channel # noqa
from app.models.role import Role, role_association_table # noqa
from app.models.user_in_group import UserInGroup # noqa