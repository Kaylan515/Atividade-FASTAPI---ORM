# Instalar as Bibliotecas:
pip install fastapi uvicorn sqlalchemy alembic python-dotenv
pip install jinja2 python-multipart

# Rodar o fastapi:
no terminal: python -m uvicorn main:app --reload

Acesse no navegador= http://127.0.0.1:8000

# Acessar a documentação
Acesse no navegador= http://127.0.0.1:8000

# Utilizar o alembic
python -m alembic init alembic (Não esqueça de configurar o env.py)
python -m alembic revision --autogenerate -m 'criar tabelas'
python -m alembic upgrade head