# 📄 Django Resume API

A RESTful API for managing resumes built with **Django REST Framework**.  
Create, read, update, and delete resumes with work experience, education, and skills.

<div align="center">

![CI/CD Pipeline](https://github.com/ranim-ahmadi/django-resume-api/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-97%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-5.2-green)
![PostgreSQL](https://img.shields.io/badge/postgresql-15-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)

</div>

---

## ✨ Features

### 🛠 Core Features
- **Full CRUD**: Manage resumes with ease.
- **Nested Resources**: Seamlessly handle experiences, education, and skills.
- **Robust Validations**: Email format, date logic, and proficiency levels (1-5).
- **Advanced Querying**: 
  - 🔍 Search by name or title.
  - 📧 Filter by email.
  - ↕️ Order by `created_at` or `updated_at`.
- **Pagination**: Optimized with 10 items per page.
- **Database**: Powered by PostgreSQL.
- **Documentation**: Auto-generated Swagger and ReDoc.

### 🎁 Bonus Features
- ✅ **97% Test Coverage** (pytest + factory-boy).
- ✅ **Dockerized**: Ready for containerized deployment.
- ✅ **CI/CD**: Fully automated GitHub Actions pipeline.
- ✅ **Secure**: Environment variable management for secrets.

---

## 🚀 Quick Start

### Prerequisites
- **Python** 3.11+
- **PostgreSQL** 15+
- **Docker** (optional)
- **Git**

---

## 💻 Local Installation

```bash
# 1. Clone the repository
git clone https://github.com/ranim-ahmadi/django-resume-api.git
cd django-resume-api

# 2. Set up a virtual environment
python -m venv venv

# 3. Activate the environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Configure environment variables
cp .env.example .env
# Edit .env with your database credentials

# 6. Run database migrations
python manage.py migrate

# 7. Create an admin user
python manage.py createsuperuser

# 8. Start the development server
python manage.py runserver
```

> **Access the API at:** [http://localhost:8000/api/](http://localhost:8000/api/)

---

## 🐳 Docker Installation

```bash
# 1. Clone and enter the project
git clone https://github.com/ranim-ahmadi/django-resume-api.git
cd django-resume-api

# 2. Prepare environment variables
cp .env.example .env

# 3. Build and launch containers
docker-compose up --build
```

> **Access the API at:** [http://localhost:8000/api/](http://localhost:8000/api/)

---

## 📚 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/resumes/` | List all resumes |
| `POST` | `/api/resumes/` | Create a new resume |
| `GET` | `/api/resumes/{id}/` | Retrieve a resume with nested data |
| `PUT` | `/api/resumes/{id}/` | Update an existing resume |
| `DELETE` | `/api/resumes/{id}/` | Remove a resume |
| `GET` | `/api/resumes/{id}/experiences/` | List experiences for a resume |
| `POST` | `/api/resumes/{id}/experiences/` | Add a new experience |
| `GET` | `/api/resumes/{id}/education/` | List education entries |
| `POST` | `/api/resumes/{id}/education/` | Add an education entry |
| `GET` | `/api/resumes/{id}/skills/` | List skills |
| `POST` | `/api/resumes/{id}/skills/` | Add a new skill |

### 🔍 Query Parameters
- **Filter**: `?email=user@example.com`
- **Search**: `?search=python`
- **Order**: `?ordering=-created_at` (descending)
- **Page**: `?page=2`

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=resumes --cov-report=html
```

> **Test Coverage: 97% ✅**  
> Open `htmlcov/index.html` in your browser to view the detailed report.

---

## 📖 Documentation

When the server is running, you can explore the API interactively:

- **Swagger UI**: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- **ReDoc**: [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)

---

## 🔄 GitHub Actions CI/CD

The pipeline automatically handles:
1. **Testing**: Runs the full suite against a PostgreSQL instance.
2. **Migrations**: Verifies that all migrations are up to date.
3. **Docker**: Builds the production-ready image.

![Pipeline Status](https://github.com/ranim-ahmadi/django-resume-api/actions/workflows/ci.yml/badge.svg)
