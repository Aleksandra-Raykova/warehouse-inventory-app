# Warehouse Inventory API

Django REST application for managing warehouse inventory and users.

## Overview
This project implements a small API to manage categories and items, plus a custom user model that uses email as the unique identifier. It uses Django and Django REST Framework (DRF). The repository includes a Dockerfile, migrations and a few basic tests.

## Features
- Custom user model (email as username)
- Item and Category models and CRUD endpoints
- Django REST Framework integration
- Token authentication is included in installed apps
- Dockerfile for containerized development

## Requirements
- Python 3.11+ (Dockerfile uses python:3.14)
- pip
- SQLite for development (configurable to PostgreSQL or other DB)
- Docker (optional)

## Quick start (local)
1. Clone repository:
   git clone https://github.com/Aleksandra-Raykova/warehouse-inventory-app.git
2. Enter the project directory and create a virtual environment:
   python -m venv .venv
   source .venv/bin/activate  # Linux / macOS
   .venv\Scripts\activate     # Windows
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations and create a superuser:
   python manage.py migrate
   python manage.py createsuperuser
5. Start the development server:
   python manage.py runserver

## API (expected routes)
- GET /items/                — list items
- POST /items/               — create item
- GET /items/{id}/           — retrieve item
- PUT /items/{id}/           — update item
- DELETE /items/{id}/        — delete item
- POST /users/register/      — user registration
