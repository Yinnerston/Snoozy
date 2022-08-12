
from sqlalchemy import Column, ForeignKey, Integer
from app.db.base_class import Base

class RoleAssociationTable(Base):
    user_id = Column(Integer, ForeignKey('user.id')),
    role_id = Column(Integer, ForeignKey('role.id')),