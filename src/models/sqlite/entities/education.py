from sqlalchemy import Column, String, BIGINT, Integer, ForeignKey
from src.models.sqlite.settings.base import Base

class Escolaridade(Base):
    __tablename__ = "escolaridade"
    
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    user_id = Column(BIGINT, ForeignKey("users.id"), nullable=False)
    nivel = Column(String(50), nullable=False)  # Ex: Ensino Fundamental, Ensino Médio, Graduação, etc.
    instituicao = Column(String(100), nullable=False)
    ano_conclusao = Column(Integer)
    periodo_serie = Column(String(50), nullable=False)  # Ex: 1º ano, 2º semestre, etc.