from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base_class import Base

userprofile_role_association_table = Table('userprofile_role_association_table', Base.metadata,
                Column('userprofile_id', Integer, ForeignKey('userprofile.id'), primary_key=True),
                Column('role_id', Integer, ForeignKey('role.id'), primary_key=True)
)

user_group_association_table = Table('user_group_association_table', Base.metadata,
                Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
                Column('group_id', Integer, ForeignKey('group.id'), primary_key=True)
)