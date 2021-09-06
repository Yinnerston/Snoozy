from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .tables import user_group_association_table

if TYPE_CHECKING:
    from .item import Item  # noqa: F401
    from .group import Group  # noqa: F401


class User(Base):
    """ User that has items and belongs to servers

    Args:
        Base ([type]): [description]
    """
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
    groups = relationship("Group", secondary=user_group_association_table, back_populates="_users")
    user_profiles = relationship("UserProfile", back_populates="user")
