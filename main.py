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
@app.get("/produtos/cadastro")
def exibir_produto(
    request: Request,
    db: Session = Depends(get_db)
):
    categorias = db.query(Categoria).all()

    return templates.TemplateResponse(
        request,
        "cadastro_produto.html",
        {
            "request": request,
            "categorias": categorias
        }
    )

#Rota para cadastrar um produto
@app.post("/produtos")
def cadastrar_produto(
    nome: str = Form(...),
    preco: int = Form(...),
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

    return RedirectResponse(url="/listar_produtos", status_code=303)

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

#Area de categorias
@app.get("/categorias/cadastro", response_class=HTMLResponse)
def formulario_categoria(request: Request):
    return templates.TemplateResponse(
        request,
        "cadastro_categoria.html",
        {"request": request}
    )

#Rota para cadastrar categoria
@app.post("/categorias")
def cadastrar_categoria(
    nome: str = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    nova_categoria = Categoria(
        nome=nome,
        descricao=descricao
    )

    db.add(nova_categoria)
    db.commit()

    return RedirectResponse(url="/listar_categorias", status_code=303)

#Rota para listar categorias
@app.get("/listar_categorias")
def listar_categorias(
    request: Request,
    db: Session = Depends(get_db)
):
    categorias = db.query(Categoria).all()

    return templates.TemplateResponse(
        request,
        "categorias.html",
        {"request": request, "categorias": categorias}
    )

#Rota para deletar categoria
@app.post("/categorias/{id}/deletar")
def deletar_categoria(
    id: int,
    db: Session = Depends(get_db)
):
    categoria = db.query(Categoria).get(id)

    if categoria:
        db.delete(categoria)
        db.commit()

    return RedirectResponse(url="/listar_categorias", status_code=303)