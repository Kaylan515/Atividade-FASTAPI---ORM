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

# joinedload
é uma estratégia de "carregamento ansioso" (eager loading) do SQLAlchemy que busca dados de objetos relacionados em uma única consulta SQL usando LEFT OUTER JOIN. Ele evita o problema "N+1" ao preencher coleções ou referências de objetos instantaneamente, otimizando a performance, sendo ideal para relacionamentos muitos-para-um.