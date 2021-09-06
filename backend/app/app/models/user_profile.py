from typing import TYPE_CHECKING
from .user import User
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from app.db.base_class import Base
from .tables import userprofile_role_association_table

if TYPE_CHECKING:
    from .item import Item  # noqa: F401
    from .group import Group  # noqa: F401
    from .role import Role # noqa: F401
    from .user import User


class UserProfile(Base):
    """ A profile for a user. One for each server, one as default.
    TODO: Permissions, custom profile pic for server, etc

    Args:
        Base ([type]): [description]
    """
    id = Column(Integer, primary_key=True, index=True)
    alias = Column(String, index=True)
    # user profile sees the user
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="user_profiles")

    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship("Group", back_populates="users")
    # Association proxy is used here to provide a view of the name argument in the roles
    roles = relationship("Role", secondary=userprofile_role_association_table, back_populates="usersWithRole")
    # Association proxy translates userInGroup.roles.append(str)
    # into userInGroup._roles.append(Role(str))
    # roles = association_proxy('_roles', 'name') # 'name' attribute from the '_roles' relationship

    def __init__(self, user: User) -> None:
        """ Make a UserInGroup from a user

        Args:
            user (User): [description]
        """
        super().__init__()
        self.user = user
