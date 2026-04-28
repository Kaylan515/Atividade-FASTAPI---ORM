from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
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

@app.get("/produtos/novo")
def formulario_produto(request: Request, db: Session = Depends(get_db)):
    categorias = db.query(Categoria).all()
    return templates.TemplateResponse("cadastro_produto.html", {
        "request": request,
        "categorias": categorias
    })