import pytest
from httpx import AsyncClient
from app.main import app
from app.database import Base, engine


# I basically do testing with the help of POSTMAN using API CURL 


@pytest.fixture(autouse=True)
def create_test_db():
    
    # creating a fresh schema for tests
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.mark.asyncio
async def test_create_and_get_book():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {"title": "Test Book", "author": "Alice", "description": "desc", "status": "available"}
        r = await ac.post("/books/", json=payload)
        assert r.status_code == 201
        data = r.json()
        assert data["title"] == "Test Book"
        book_id = data["id"]

        r2 = await ac.get(f"/books/{book_id}")
        assert r2.status_code == 200
        assert r2.json()["id"] == book_id

        r3 = await ac.get("/books/")
        assert r3.status_code == 200
        assert len(r3.json()) >= 1
