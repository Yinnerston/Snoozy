from backend.app.app.models.user import User
from sqlalchemy.sql import roles
from backend.app.app.models import role
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relation, relationship
from sqlalchemy.ext.associationproxy import association_proxy

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401
    from .group import Group  # noqa: F401
    from .role import Role, role_association_table # noqa: F401


class UserInGroup(User):
    """ User within a server.
    TODO: Permissions, custom profile pic for server, etc

    Args:
        Base ([type]): [description]
    """
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
    # TODO: Is this a Single group
    group = relationship("Group", back_populates="owner")
    # Association proxy is used here to provide a view of the name argument in the roles
    _roles = relationship("Role", secondary=lambda: role_association_table)
    # Association proxy translates userInGroup.roles.append(str)
    # into userInGroup._roles.append(Role(str))
    roles = association_proxy('_roles', 'name') # 'name' attribute from the '_roles' relationship
