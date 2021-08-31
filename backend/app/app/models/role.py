from sqlalchemy import Column, ForeignKey, String, Boolean, Integer
from app.db.base_class import Base
from app.api.deps import get_db

db = get_db()
role_association_table = db.Table('role_association',
                Column('user_id', Integer, ForeignKey('user.id')),
                Column('role_id', Integer, ForeignKey('role.id')),
)

class Role(Base):
    """ A role that a user has within a group.

    Args:
        Base ([type]): [description]
    """
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)  # TODO: Make this the primary key?
    colour = Column(String, default=None)
    manageServer = Column(Boolean, default=True)
    manageMessages = Column(Boolean, default=True)
    manageEmojis = Column(Boolean, default=True)
    manageChannels = Column(Boolean, default=True)

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
