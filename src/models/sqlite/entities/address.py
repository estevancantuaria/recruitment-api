from sqlalchemy import Column, String, BIGINT, ForeignKey, Boolean, Date
from src.models.sqlite.settings.base import Base

class Address(Base):
    __tablename__ = "endereco"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    user_id = Column(BIGINT, ForeignKey("users.id"), nullable=False)
    rua = Column(String(100), nullable=False)
    numero = Column(String(10), nullable=False)
    complemento = Column(String(50))
    bairro = Column(String(50))
    cidade = Column(String(50), nullable=False)
    estado = Column(String(50), nullable=False)
    cep = Column(String(20), nullable=False)
