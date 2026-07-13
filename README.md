# Game Store Backend

Backend API for the Game Store built using FastAPI and PostgreSQL.

## Features
- User Registration
- User Login (JWT Authentication)
- Protected Routes
- CRUD Game APIs
- PostgreSQL Database
- SQLAlchemy ORM
- Password Hashing (Passlib + bcrypt)

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT
- Passlib
- Uvicorn

## Installation

```bash
git clone https://github.com/Rakesh-R-140/game-store-backend.git
cd game-store-backend
python -m venv venv
```

Activate the virtual environment:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/game_store
SECRET_KEY=your_secret_key
ALGORITHM=HS256
```

## Run

```bash
uvicorn main:app --reload
```

## API Testing (Swagger UI)

### Available Endpoints
![Swagger UI Overview](docs/screenshots/swagger-overview.png)

### Register Endpoint
![Register API](docs/screenshots/register-api.png)

### Login Endpoint (returns JWT token)
![Login API](docs/screenshots/login-api.png)

### Get Games Endpoint
![Get Games API](docs/screenshots/get-games-api.png)

