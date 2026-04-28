# models é o arquivo onde fica as classes (tabelas)
# instalar = pip install sqlalchemy
# instalar = pip install alembic
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
