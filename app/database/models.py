from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MonitoredSite(Base):
    __tablename__ = "monitored_sites"

    id = Column(Integer, primary_key=True, index=True)  # ID único para cada site
    url = Column(String, unique=True, nullable=False)  # URL do site
    rss_feed = Column(String, unique=True, nullable=True)  # Endereço do RSS, se disponível
    is_active = Column(Boolean, default=True)  # Indica se o site está ativo para monitoramento
    last_checked = Column(DateTime, nullable=True)  # Última vez que o site foi verificado
    created_at = Column(DateTime, default=func.now())  # Data de criação do registro
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Última atualização
