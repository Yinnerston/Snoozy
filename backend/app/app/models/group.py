from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

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
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="snoozyServer")
    users = relationship("User", back_populates="snoozyServer")
    channels = relationship("Channel", back_populates="group")
