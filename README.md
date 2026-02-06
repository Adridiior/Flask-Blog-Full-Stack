# Flask Blog – Full Stack Web Application

This repository contains a **full-stack blog application** built with Flask, designed to demonstrate production-ready backend architecture, authentication workflows, and database integration.

The project goes beyond a basic tutorial app and focuses on **clean structure, maintainability, and real deployment constraints**.

🌐 **Live demo:**  
https://flask-blog-full-stack.onrender.com

---

## 🚀 Features

- User registration and authentication
- Secure login / logout with session management
- Authenticated users can create, edit, and delete posts
- Posts displayed in chronological order with pagination
- Modular architecture using Flask Blueprints
- CSRF protection for all forms
- Custom error handling (404 / 500)
- PostgreSQL database in production

---

## 🛠 Tech Stack

**Backend**
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF

**Database**
- PostgreSQL (production)
- SQLite (local development)

**Deployment**
- Gunicorn
- Render
- Environment-based configuration

---

## 📁 Project Structure

app/
│── routes/ # Blueprint-based route organization
│── models.py # SQLAlchemy models
│── templates/ # Jinja2 templates
│── static/ # CSS, JS, images
│── init.py # Application factory
migrations/ # Database migrations
run.py # Application entry point
requirements.txt


---

## ⚙️ Local Setup

```bash
git clone https://github.com/Adridiior/Flask-Blog-Full-Stack
cd Flask-Blog-Full-Stack

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

```

## Set environment variables (example):

export FLASK_ENV=development
export SECRET_KEY=your_secret_key
export DATABASE_URL=sqlite:///site.db


## Initialize the database:
flask db upgrade


## Run the app:
flask run


## Project Goals

This project was built to:
Practice real-world Flask architecture
Work with authentication and authorization flows
Handle production database constraints
Deploy and debug a live application
Serve as a foundation for future features
Planned improvements include comments moderation, user profiles, image uploads, and API endpoints.


# License
MIT License

