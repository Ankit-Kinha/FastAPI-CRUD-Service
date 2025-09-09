# FastAPI-CRUD-Service
FastAPI CRUD Service

# FastAPI CRUD Project - Stantech

A fully functional **FastAPI CRUD application** for managing books, featuring database migrations, Docker support, and auto-generated API documentation via Swagger.

---

## Features

- CRUD operations for `Book` entity
- Database migrations with Alembic
- Auto-generated API docs via Swagger UI
- Docker-ready setup
- Unit and integration tests using `pytest`
- Count of books grouped by status

---

## Tech Stack

- **Backend:** FastAPI
- **Database:** SQLAlchemy ORM (SQLite/PostgreSQL)
- **Migrations:** Alembic
- **Testing:** pytest
- **Containerization:** Docker & Docker Compose
- **CI/CD:** GitHub Actions (optional)

---

## Prerequisites

- Python 3.9+
- pip
- Virtual environment (`venv`)  
- Docker (optional)

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd fast_dev
```

2. **Create a virtual environment and activate it:**

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```


3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Apply database migrations:**

```bash
alembic upgrade head
```


5. **Run the FastAPI server:**

```bash
uvicorn app.main:app --reload
```

6. **Run the FastAPI server:**

```arduino
(http://127.0.0.1:8000/docs)
```


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.




## 

This README provides an overview of the project's functionalities, installation instructions, and details on how to interact with the FastAPI . 
Adjust the repository URL and any specific details as needed.



