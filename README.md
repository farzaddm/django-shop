# Backend E-commerce Django API


This project is the result of completing **[The Ultimate Django Series](https://codewithmosh.com/p/the-ultimate-django-series)** by *[Mosh Hamedani](https://codewithmosh.com/)*.  
It demonstrates a **backend architecture** for an e-commerce system and reflects the practical skills and best practices learned throughout all three parts of the course.


## 🧱 Project Structure

The project is organized into multiple Django apps, each responsible for a specific domain of the system.
This structure improves **separation of concerns**, **maintainability**, and **scalability** as the project grows.

* **core** – Project-specific shared logic such as base configurations, signals, and utilities
* **store** – Core e-commerce domain: products, collections, carts, orders, pricing, and validations
* **likes** – Handling user likes and related interactions
* **tags** – Tagging system for categorizing and filtering entities
* **mailer** – Email-related logic and background email tasks
* **storefront** – Project configuration layer (settings, URLs, ASGI/WSGI, Celery setup)


## 🧠 Key Concepts & Features

### 🌐 REST API & Architecture

* RESTful API built with Django REST Framework
* Pagination, filtering, searching, and ordering
* Clean separation between domain logic and API layer

### 🗄 Database & ORM

* Relational database design for an e-commerce system
* Optimized queries using `select_related` and `prefetch_related`

### 🛒 E-commerce Core

* Product catalog and collections
* Shopping cart and order workflow
* Price validation and business rules

### 🔐 Authentication & Authorization

* Django authentication system
* Custom user model
* Token-based authentication and permission handling (JWT)

### 📦 Media & File Handling

* Product image uploads
* File and image validation using Django and custom validators

### 🔔 Signals & Business Logic

* Custom Django signals
* Automatic creation and synchronization of related objects

### 🧩 Admin Customization

* Customized Django admin interface
* Advanced list views, filters, search, and inline models

### 🧪 Testing & Code Quality

* Automated testing with `pytest`
* Test data generation using **model_bakery**
* Reusable **fixtures** for consistent and maintainable tests

### ⚡ Performance & Background Tasks

* Redis used for caching and as a message broker
* Background task processing with Celery
* Task monitoring with Flower
* Performance and load testing using Locust

### 📬 Email & Background Services

* Local email testing using a Dockerized SMTP server (smtp4dev)
* No real SMTP provider required during development
* Web-based admin panel available for inspecting sent emails

### 🐳 Docker & Development Environment

* Docker-based development setup
* Reproducible and isolated environment for services and dependencies


## 🗂 ER Model (Database Design)

![ER Diagram](docs/er/django-e-commer.png)


## 🛠 Prerequisites

Make sure you have the following installed:

* Python 3.10+
* pip
* Virtual environment tool (`venv` or `virtualenv`)
* MySQL (or PostgreSQL)
* Docker


## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ultimate-django.git
cd ultimate-django
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set environment variables**

Create a `.env` file and configure sensitive settings such as `SECRET_KEY` and database credentials.

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Start the development server**

```bash
python manage.py runserver
```


## 🧪 Running Tests

```bash
pytest
```


## 📄 API Documentation

The project includes OpenAPI documentation and an interactive Swagger UI generated from the API schema.
The documentation focuses on **happy path scenarios**, demonstrating the intended and correct usage of the API endpoints rather than edge cases or failure states.

* [Swagger schema file](https://github.com/farzaddm/django-ecommerce-api/blob/main/docs/schema.yml)
* [Swagger documentation page](https://farzaddm.github.io/django-ecommerce-api/)
