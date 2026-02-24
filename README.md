# 📄 Django Resume API

A RESTful API for managing resumes built with **Django REST Framework**.  
Create, read, update, and delete resumes with work experience, education, and skills.

![CI/CD Pipeline](https://github.com/ranim-ahmadi/django-resume-api/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-97%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-5.2-green)
![PostgreSQL](https://img.shields.io/badge/postgresql-15-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)

---

## ✨ Features

### Core Features
- ✅ CRUD operations for resumes
- ✅ Nested resources: experiences, education, skills
- ✅ Validations (email, dates, proficiency 1-5)
- ✅ Filtering by email
- ✅ Search by name or title
- ✅ Ordering by created_at/updated_at
- ✅ Pagination (10 items/page)
- ✅ PostgreSQL database
- ✅ Swagger/ReDoc documentation

### Bonus Features
- ✅ **97% test coverage** (pytest + factory-boy)
- ✅ **Docker** containerization
- ✅ **GitHub Actions CI/CD** pipeline
- ✅ **Secure environment variables**

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL 15+
- Docker (optional)
- Git

---

## 💻 Local Installation

```bash
# 1. Clone repository
git clone https://github.com/ranim-ahmadi/django-resume-api.git
cd django-resume-api

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Configure environment
cp .env.example .env
# Edit .env with your credentials

# 6. Run migrations
python manage.py migrate

# 7. Create superuser 
python manage.py createsuperuser

# 8. Start server
python manage.py runserver
Access: http://localhost:8000/api/

🐳 Docker Installation
bash
# 1. Clone repository
git clone https://github.com/ranim-ahmadi/django-resume-api.git
cd django-resume-api

# 2. Configure environment
cp .env.example .env
# Edit .env with your credentials

# 3. Build and run
docker-compose up --build
Access: http://localhost:8000/api/

📚 API Endpoints
Method	Endpoint	Description
GET	/api/resumes/	List all resumes
POST	/api/resumes/	Create a resume
GET	/api/resumes/{id}/	Get resume + nested data
PUT	/api/resumes/{id}/	Update resume
DELETE	/api/resumes/{id}/	Delete resume
GET	/api/resumes/{id}/experiences/	List experiences
POST	/api/resumes/{id}/experiences/	Add experience
GET	/api/resumes/{id}/education/	List education
POST	/api/resumes/{id}/education/	Add education
GET	/api/resumes/{id}/skills/	List skills
POST	/api/resumes/{id}/skills/	Add skill
Query Parameters
Filter: ?email=john@email.com

Search: ?search=python

Order: ?ordering=created_at or ?ordering=-created_at

Page: ?page=2

🧪 Testing
bash
# Run all tests
pytest

# Run with coverage
pytest --cov=resumes --cov-report=html
# Open htmlcov/index.html to view coverage report
Test Coverage: 97% ✅

📖 API Documentation
When server is running:

Swagger UI: http://localhost:8000/api/docs/

ReDoc: http://localhost:8000/api/redoc/

🔄 GitHub Actions CI/CD
The pipeline automatically:

✅ Runs tests with PostgreSQL

✅ Checks migrations

✅ Builds Docker image

Pipeline Status
https://github.com/ranim-ahmadi/django-resume-api/actions/workflows/ci.yml/badge.svg

