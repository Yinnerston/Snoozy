from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .group import Group  # noqa: F401


class Channel(Base):
    """ Channel within a server

    Args:
        Base ([type]): [description]
    """
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship("Group", back_populates="channels")
