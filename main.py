from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy.orm import joinedload
from models import Categoria, Produto

# Import a biblioteca:
# pip install jinja2 python-multipart

# inicializar o app fastapi
app = FastAPI(title="Gerenciamento de Produtos")

# configurar templates
templates = Jinja2Templates(directory="templates")

# Rota inicial
#Rota inicial para apresentação
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request": request}
    )

#Para exibir um html na rota - exibir o formulário
@app.get("/produtos/cadastro", response_class=HTMLResponse)
def exibir_produto(request: Request):
    return templates.TemplateResponse(request, "cadastro_produto.html", {"request": request})

#Rota para cadastrar um produto
@app.post("/produtos")
def cadastrar_produto(
    nome: str = Form(...),
    preco: float = Form(...), 
    estoque: int = Form(...),
    categoria_id: int = Form(...),
    db: Session = Depends(get_db)
):
    novo_produto = Produto(
        nome=nome,
        preco=preco,
        estoque=estoque,
        categoria_id=categoria_id
    )

    db.add(novo_produto)
    db.commit()

    return RedirectResponse(url="/", status_code=303)

#Listar produtos
@app.get("/listar_produtos")
def exibir_produtos(
    request: Request,
    db: Session = Depends(get_db)
):
    produtos = db.query(Produto).options(joinedload(Produto.categoria)).all()
    return templates.TemplateResponse(
        request,
        "produtos.html",
        {"request": request, "produtos": produtos}
    )

#Rota para deletar um produto
@app.post("/produtos/{id}/deletar")
def deletar_produto(
    id: int,
    db: Session = Depends(get_db)
):
    produto = db.query(Produto).get(id)
    if produto:
        db.delete(produto)
        db.commit()
    return RedirectResponse(url="/listar_produtos", status_code=303)