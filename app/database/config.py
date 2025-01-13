from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração da URL do banco de dados (substitua pelos valores corretos)
DATABASE_URL = "postgresql://username:password@localhost/dbname"

# Criação do engine para conectar ao banco de dados
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Mantém a conexão viva, especialmente útil em produção
)

# Configuração da sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para a criação dos modelos
Base = declarative_base()

# Função auxiliar para obter a sessão do banco em endpoints ou scripts
def get_db():
    """
    Fornece uma sessão de banco de dados para endpoints do FastAPI.
    Usa `SessionLocal` e garante o fechamento correto da conexão.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
