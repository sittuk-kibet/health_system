# health_system
# 🏥 Health Information System API

A simple health information system API built with **FastAPI** and **SQLite**, designed to allow healthcare providers (e.g., doctors) to manage clients and enroll them in various health programs such as **Malaria**, **HIV**, **TB**, etc.

This project is part of an internship assessment, demonstrating REST API development, clean code architecture, and software engineering best practices.

---

## 📌 Features

✅ Register a new client  
✅ Create health programs (e.g., Malaria, TB, HIV)  
✅ Enroll clients in one or more health programs  
✅ Search for clients by name  
✅ View client profiles (including enrolled programs)  
✅ Expose all client data via REST API  
✅ Auto-generated interactive API docs (Swagger + ReDoc)

---

## 🚀 Tech Stack

| Technology         | Description                          |
|--------------------|--------------------------------------|
| 🐍 Python 3.10+    | Programming language                |
| ⚡ FastAPI          | High-performance Python web framework |
| 🗄️ SQLite + SQLAlchemy | Lightweight relational DB + ORM    |
| 🧪 Pytest           | For testing endpoints               |
| 📄 Pydantic         | For request/response validation     |
| 🔄 Uvicorn          | ASGI server for local development   |

---

## 📁 Project Structure

```plaintext
health_system/
├── app/
│   ├── crud/          # Database access logic (CRUD functions)
│   ├── database.py    # DB connection and setup
│   ├── main.py        # App entry point
│   ├── models/        # SQLAlchemy ORM models
│   ├── routers/       # FastAPI route definitions
│   └── schemas/       # Pydantic models for request/response
├── tests/             # Test cases using pytest + TestClient
├── [requirements.txt](http://_vscodecontentref_/0)   # Project dependencies
├── README.md     
```markdown
# 🏥 Health Information System API

A simple health information system API built with **FastAPI** and **SQLite**, designed to allow healthcare providers (e.g., doctors) to manage clients and enroll them in various health programs such as **Malaria**, **HIV**, **TB**, etc.

This project is part of an internship assessment, demonstrating REST API development, clean code architecture, and software engineering best practices.

---

## 📌 Features

✅ Register a new client  
✅ Create health programs (e.g., Malaria, TB, HIV)  
✅ Enroll clients in one or more health programs  
✅ Search for clients by name  
✅ View client profiles (including enrolled programs)  
✅ Expose all client data via REST API  
✅ Auto-generated interactive API docs (Swagger + ReDoc)

---

## 🚀 Tech Stack

| Technology         | Description                          |
|--------------------|--------------------------------------|
| 🐍 Python 3.10+    | Programming language                |
| ⚡ FastAPI          | High-performance Python web framework |
| 🗄️ SQLite + SQLAlchemy | Lightweight relational DB + ORM    |
| 🧪 Pytest           | For testing endpoints               |
| 📄 Pydantic         | For request/response validation     |
| 🔄 Uvicorn          | ASGI server for local development   |

---

## 📁 Project Structure

```plaintext
health_system/
├── app/
│   ├── crud/          # Database access logic (CRUD functions)
│   ├── database.py    # DB connection and setup
│   ├── main.py        # App entry point
│   ├── models/        # SQLAlchemy ORM models
│   ├── routers/       # FastAPI route definitions
│   └── schemas/       # Pydantic models for request/response
├── tests/             # Test cases using pytest + TestClient
├── requirements.txt   # Project dependencies
├── README.md          # You're reading it
```

---

## 🛠️ Setup & Run Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/health-info-system.git
cd health-info-system
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```

### 5. Open in Browser

- **Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📬 API Endpoints Summary

| Method | Endpoint                  | Description                          |
|--------|---------------------------|--------------------------------------|
| POST   | `/clients/`               | Register new client                 |
| GET    | `/clients/`               | Search clients by name              |
| GET    | `/clients/{id}`           | Get client profile                  |
| POST   | `/clients/{id}/enroll`    | Enroll client in programs           |
| POST   | `/programs/`              | Create a new health program         |
| GET    | `/programs/`              | List all available programs         |

---

## 🧪 Running Tests

Run all test cases:

```bash
pytest
```

To fix module errors, ensure `PYTHONPATH` is set correctly:

```bash
PYTHONPATH=./ pytest
```

Or use the included `pytest.ini` file.

---

## ✅ Completed Functional Requirements

| Feature                                   | Status |
|------------------------------------------|--------|
| Create a health program                  | ✅ Done |
| Register a new client                    | ✅ Done |
| Enroll client into one or more programs  | ✅ Done |
| Search for clients                       | ✅ Done |
| View client profile                      | ✅ Done |
| Expose client profile via API            | ✅ Done |
| Clean, documented code                   | ✅ Done |
| Tests using Pytest                       | ✅ Done |
| API-first design (OpenAPI docs)          | ✅ Done |

