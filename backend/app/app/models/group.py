from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .tables import user_group_association_table
if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Group(Base):
    """ Discord-like server class

    Args:
        Base ([type]): [description]
    """
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    # TODO: One to one relationship
    # TODO: Automatically populate owner in users

    # One to many relationship with roles
    roles = relationship("Role", back_populates="group")   # TODO: How is the foreign key implemented again?
    # Many to many relationship with User
    _users = relationship("User", secondary=user_group_association_table, back_populates="groups")
    # One to many relationship with UserProfile
    users = relationship("UserProfile", back_populates="group") 
    channels = relationship("Channel", back_populates="group")

