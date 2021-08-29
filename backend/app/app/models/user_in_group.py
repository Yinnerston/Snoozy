from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relation, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401
    from .group import Group  # noqa: F401


class UserInGroup(Base):
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
    groups = relationship("Group", back_populates="owner")
