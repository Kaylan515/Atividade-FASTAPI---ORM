# models é o arquivo onde fica as classes (tabelas)
# instalar = pip install sqlalchemy
# instalar = pip install alembic
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    descricao = Column(String(150), nullable=True)
    
    produtos = relationship("Produto", back_populates="categoria")

    def __repr__(self):
        return f"Categoria(id={self.id}, nome='{self.nome}', descricao='{self.descricao}')"

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    preco = Column(Float)
    estoque = Column(Integer)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    categoria = relationship("Categoria", back_populates="produtos")

    def __repr__(self):
        return f"Produto(id={self.id}, nome='{self.nome}', preco={self.preco}, estoque={self.estoque}, categoria_id={self.categoria_id})"
