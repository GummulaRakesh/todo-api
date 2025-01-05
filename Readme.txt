# To-Do List API

## Overview
This is a REST API for managing a simple To-Do List application. The API allows users to create, update, delete, and fetch tasks while ensuring security using JWT-based authentication.

## Features
- User authentication with JWT tokens.
- CRUD operations for tasks.
- Secure endpoints that require authentication.

## Technologies Used
- **FastAPI** (Python Web Framework)
- **SQLite** (Database for simplicity, can be replaced with PostgreSQL/MySQL)
- **SQLAlchemy** (ORM for database operations)
- **JWT (JSON Web Token)** for authentication

---

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/GummulaRakesh/todo-api.git
cd todo-api
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Application
```sh
uvicorn main:app or uvicorn main:app --reload
```

The API will be available at: **http://127.0.0.1:8000**

---

## API Endpoints

### 1. Authentication
#### **Login User (Obtain Token)**
**POST /login**

**Request Body:**
```json
{
  "username": "admin",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

---

### 2. Task Management (Protected Endpoints)
All the following endpoints require authentication by passing the JWT token in the `Authorization` header as:
```
Authorization: Bearer <your_token>
```

#### **Create a New Task**
**POST /tasks**

**Request Body:**
```json
{
  "title": "Buy Groceries",
  "description": "Milk, Eggs, Bread"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Buy Groceries",
  "description": "Milk, Eggs, Bread",
  "status": "pending"
}
```

---

#### **Get All Tasks**
**GET /tasks**

**Response:**
```json
[
  {
    "id": 1,
    "title": "Buy Groceries",
    "description": "Milk, Eggs, Bread",
    "status": "pending"
  }
]
```

---

#### **Get a Task by ID**
**GET /tasks/{id}**

**Response:**
```json
{
  "id": 1,
  "title": "Buy Groceries",
  "description": "Milk, Eggs, Bread",
  "status": "pending"
}
```

---

#### **Update Task Status**
**PUT /tasks/{id}**

**Request Body:**
```json
{
  "status": "completed"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Buy Groceries",
  "description": "Milk, Eggs, Bread",
  "status": "completed"
}
```

---

#### **Delete a Task**
**DELETE /tasks/{id}**

**Response:**
```json
{
  "message": "Task deleted successfully"
}
```

---

## Authentication Details
- The API uses JWT authentication.
- When logging in, a token is issued, which must be included in the `Authorization` header for protected routes.
- Token format: `Bearer <your_token>`.

## Environment Variables
| Variable       | Description                          |
|---------------|----------------------------------|
| SECRET_KEY    | JWT Secret Key                    |
| ALGORITHM     | JWT Algorithm (default: HS256)   |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiration time (default: 30 minutes) |



---

**Author:** Rakesh Gummula  
**GitHub:** https://github.com/GummulaRakesh

