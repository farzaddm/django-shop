# Backend E-commerce Django API


## 🚀 What I Learned & What’s Implemented in This Project

This project is the result of completing **The Ultimate Django Series** by *Mosh Hamedani*.
It demonstrates a **production-ready backend architecture** for an e-commerce system and reflects the practical skills and best practices learned throughout all three parts of the course.


## 🧠 Key Concepts, Features & Skills Learned

### 🗄 Database Design & ORM

* Designing relational schemas for e-commerce systems
* Query optimization with:

  * `select_related`
  * `prefetch_related`

### 📦 File & Image Handling

* Uploading **product images**
* Configuring `MEDIA_ROOT` and `MEDIA_URL`
* Writing **custom validators** for uploaded files and images
* Restricting file size, file type, and image dimensions
* Handling media files safely in development and production

### 🔐 Authentication & Authorization

* Django authentication system
* Custom user model integration
* Token-based authentication
* Permission classes and access control
* Protecting sensitive endpoints
* Role-based access (admin vs regular users)

### 🧩 Django Admin Customization

* Customizing the **Django admin panel**
* Adding:

  * Custom list displays
  * Search fields
  * Filters
  * Inline related models

### 🔔 Signals & Business Logic

* Writing **custom Django signals**
* Automatically creating related objects

### 🌐 REST APIs with Django REST Framework

* Building RESTful APIs using:

  * Serializers
  * ViewSets
  * Routers
* Nested serializers
* Custom serializer methods
* Pagination, filtering, searching, and ordering

### 🛒 E-commerce Functionality

* Product catalog
* Shopping cart logic
* Cart items and quantities
* Order creation workflow
* Order items snapshotting product data
* Price calculations and validations

### 🧪 Testing & Code Quality

* Writing **automated tests with pytest**
* Testing:

  * Models
  * APIs
  * Permissions
* Using fixtures for clean test data
* Ensuring predictable and stable behavior

### ⚡ Performance & Scalability

* Using **Redis** for caching
* Avoiding N+1 query problems
* Background processing with **Celery**
* Asynchronous tasks for:

  * Sending emails
  * Long-running operations

### 📬 Email & Background Services

* Email sending using **Dockerized SMTP server**
* Integration with **smtp4dev** for local development
  👉 [https://github.com/rnwood/smtp4dev/blob/master/docs/Installation.md](https://github.com/rnwood/smtp4dev/blob/master/docs/Installation.md)
* Testing email workflows without real SMTP providers
* Running supporting services via Docker

### 🐳 Docker & Development Environment

* Using Docker to run auxiliary services
* Understanding containerized development workflows
* Isolating infrastructure from application code


## 🗂 ER Model (Database Design)

![ER Diagram](./docs/er-diagram.png)

## 🛠 Prerequisites

Make sure you have the following installed:

- Python 3.10+  
- pip  
- Virtual environment tool (`venv` or `virtualenv`)  
- MySQL (or Postgres) configured for your Django project

## 📦 Installation

1. **Clone this repo**

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

   Create a `.env` file and add your secret settings (e.g., `SECRET_KEY`, database credentials).

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

## 📌 API Usage

Once the server is running, visit:

```
http://localhost:8000/api/
http://localhost:8000/admin/
```

Use your favorite API client (e.g., Postman, Insomnia) to test endpoints.

## 🧪 Running Tests

To run the test suite:

```bash
pytest
```