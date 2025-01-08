from sqlalchemy import Column, String, BIGINT, ForeignKey, Boolean, Date
from src.models.sqlite.settings.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    senha = Column(String(50), nullable=False)
    cpf = Column(String(50), nullable=False, unique=True)
    telefone = Column(String(50), nullable=False, unique=True)
    ativo = Column(Boolean, nullable=False)
    tipo_usuario = Column(String(50), nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email}, senha={self.senha}, cpf={self.cpf}, telefone={self.telefone}, ativo={self.ativo}, tipo_usuario={self.tipo_usuario})"


class Jovem(User):
    __tablename__ = "jovens"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    user_id = Column(BIGINT, ForeignKey("users.id"), nullable=False)
    rg = Column(String(50), nullable=False, unique=True)
    data_nascimento = Column(Date, nullable=False)
    
    def __repr__(self):
        return f"Jovem(id={self.id}, user_id={self.user_id}, rg={self.rg}, data_nascimento={self.data_nascimento})"
    
class Recrutador(User):
    __tablename__ = "recrutadores"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    user_id = Column(BIGINT, ForeignKey("users.id"), nullable=False)
    empresa = Column(String(50), nullable=False)
    cargo = Column(String(50), nullable=False)
    
    def __repr__(self):
        return f"Recrutador(id={self.id}, user_id={self.user_id}, empresa={self.empresa}, cargo={self.cargo})"
