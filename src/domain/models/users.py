from sqlalchemy import Column, String, BIGINT, ForeignKey, Date, Enum
from src.infra.database.base import Base
import enum

class UserType(enum.Enum):
    YOUNGSTER = "YOUNGSTER"
    RECRUITER = "RECRUITER"

class User(Base):
    __tablename__ = "users"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)
    cellphone = Column(String(20), unique=True, nullable=False)
    user_type = Column(Enum(UserType), nullable=False)
    password = Column(String(255), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': user_type
    }

class Youngster(User):
    __tablename__ = "youngsters"

    id = Column(BIGINT, ForeignKey('users.id'), primary_key=True)
    rg = Column(String(20), unique=True, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': UserType.YOUNGSTER,
    }

class Recruiter(User):
    __tablename__ = "recruiters"

    id = Column(BIGINT, ForeignKey('users.id'), primary_key=True)
    company = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': UserType.RECRUITER,
    }

