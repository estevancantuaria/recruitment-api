from sqlalchemy import Column, String, BIGINT, ForeignKey, Boolean, Date
from src.models.sqlite.settings.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(BIGINT, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    senha = Column(String(50))
    cpf = Column(String(50))
    telefone = Column(String(50))
    ativo = Column(Boolean)
    tipo_usuario = Column(String(50))


class Jovem(User):
    __tablename__ = "jovens"
    id = Column(BIGINT, primary_key=True)
    user_id = Column(BIGINT, ForeignKey("users.id"))
    rg = Column(String(50))
    data_nascimento = Column(Date)
    
class Recrutador(User):
    __tablename__ = "recrutadores"
    id = Column(BIGINT, primary_key=True)
    user_id = Column(BIGINT, ForeignKey("users.id"))
    empresa = Column(String(50))
    cargo = Column(String(50))