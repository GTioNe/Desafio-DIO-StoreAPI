from fastapi import FastAPI
from contextlib import asynccontextmanager

from store.db.mongo import connect_to_mongo, close_mongo_connection
from store.controllers.product import router as product_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()


app = FastAPI(
    title="My Store API",
    description="API de loja desenvolvida com TDD - Projeto personalizado do aluno DIO",
    version="0.1.0",
    lifespan=lifespan
)

# Incluir routers
app.include_router(product_router)


@app.get("/")
async def root():
    return {
        "message": "Bem-vindo à My Store API!",
        "description": "API de loja desenvolvida com TDD - Projeto personalizado do aluno DIO",
        "version": "0.1.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API funcionando corretamente"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

