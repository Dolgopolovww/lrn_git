class Role():
    __tablename__ = 'roles'

    id: int
    name: str


class User():
    __tablename__ = 'users'

    id: int
    role_id: int
    username: str
