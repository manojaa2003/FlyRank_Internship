# 🚀 Task API using FastAPI

A simple RESTful Task Management API built with **FastAPI** as part of the **FlyRank AI Backend Engineering Internship**.

The API demonstrates the complete CRUD (Create, Read, Update, Delete) workflow using an in-memory data store. It also includes automatic API documentation using **Swagger UI**.

---

## 📌 Features

- Create a new task
- Retrieve all tasks
- Retrieve a task by ID
- Update an existing task
- Delete a task
- Input validation using Pydantic
- Proper HTTP status codes
- Interactive API documentation with Swagger UI

---

## 🛠️ Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/manojaa2003/FlyRank_Internship.git
```

### 2. Navigate into the project

```bash
cd FlyRank_Internship
```

### 3. Create a virtual environment (Optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

---

# ▶️ Run the Application

Run the following command:

```bash
uvicorn AI_Backend_Engineering_Task_1:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

# 📚 API Endpoints

| Method | Endpoint | Description | Success Status |
|---------|----------|-------------|----------------|
| GET | `/` | Returns API information | 200 OK |
| GET | `/health` | Health check endpoint | 200 OK |
| GET | `/tasks` | Retrieve all tasks | 200 OK |
| GET | `/tasks/{task_id}` | Retrieve a task by ID | 200 OK |
| POST | `/tasks` | Create a new task | 201 Created |
| PUT | `/tasks/{task_id}` | Update an existing task | 200 OK |
| DELETE | `/tasks/{task_id}` | Delete a task | 204 No Content |

---

# 📄 Example curl Request

Create a new task

```bash
curl -i -X POST http://127.0.0.1:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Buy milk"}'
```

Example Response

```http
HTTP/1.1 201 Created
date: Thu, 16 Jul 2026 09:04:27 GMT
server: uvicorn
content-length: 40
content-type: application/json

{"id":5,"title":"Buy milk","done":false}
```

---

# 📖 Swagger UI

FastAPI automatically generates interactive API documentation.

Open the following URL in your browser:

```
http://127.0.0.1:8000/docs
```

Using Swagger UI, you can:

- Create tasks
- Retrieve tasks
- Update tasks
- Delete tasks
- Test all endpoints without Postman or curl

### Swagger Screenshot

> Replace the image below with your screenshot.

```text
README.md
│
└── images
      └── swagger-ui.png
```

Then include it like this:

```markdown
![Swagger UI](images/swagger-ui.png)
```

---

# 📂 Project Structure

```
.
├── AI_Backend_Engineering_Task_1.py
├── README.md
└── images
    └── swagger-ui.png
```

---

# ✅ Implemented Features

- RESTful API using FastAPI
- CRUD Operations
- Path Parameters
- Request Body Validation
- Pydantic Models
- JSON Responses
- Proper HTTP Status Codes
- Swagger/OpenAPI Documentation

---

# 👨‍💻 Author

**Manoj A A**

FlyRank AI Backend Engineering Internship Assignment