import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(project_root)

from app.database.config import Base, engine
from app.database.models import MonitoredSite

# Criar todas as tabelas no banco de dados
if __name__ == "__main__":
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")
