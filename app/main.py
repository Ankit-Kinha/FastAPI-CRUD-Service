from fastapi import FastAPI
from .routers import books
from .middleware import APIKeyMiddleware

app = FastAPI(title="Stantech Assignment - Book CRUD")

# add API key middleware (reads SECRET_API_KEY env var)
app.add_middleware(APIKeyMiddleware)

app.include_router(books.router)

@app.get("/health")
def health():
    return {"status": "ok"}
