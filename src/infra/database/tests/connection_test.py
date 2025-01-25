import pytest
from src.infra.database.connection import db_connection_handler
from sqlalchemy.engine import Engine
from sqlalchemy import text

def test_connect_to_db():
    assert db_connection_handler.get_engine() is None
    

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()
    print(db_connection_handler.session)
    
    assert db_engine is not None
    assert isinstance(db_engine, Engine)
    
    # Testa se a conexão realmente funciona
    try:
        with db_engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.scalar() == 1
            
    except Exception as e:
        pytest.fail(f"Falha ao conectar ao banco de dados: {str(e)}")
        
    
def test_session_close():
    with db_connection_handler as db:
        assert db.session is not None
    assert db_connection_handler.session.is_active is True
      
