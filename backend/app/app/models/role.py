from sqlalchemy import Column, ForeignKey, String, Boolean, Integer, Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base

from .tables import userprofile_role_association_table

class Role(Base):
    """ A role that a user has within a group.

    Args:
        Base ([type]): [description]
    """
    id = Column(Integer, primary_key=True, index=True)
    # A group can have many roles
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship("Group", back_populates="roles")
    # Bidirectional many-to-many relationship with users in group
    usersWithRole = relationship("UserProfile", secondary=userprofile_role_association_table, back_populates="roles")

    name = Column(String, unique=True)  # TODO: Make this the primary key?
    colour = Column(String, default=None)
    manageServer = Column(Boolean, default=True)
    manageMessages = Column(Boolean, default=True)
    manageEmojis = Column(Boolean, default=True)
    manageChannels = Column(Boolean, default=True)

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

