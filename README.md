# Blogging Platform

This is a Django-based blogging platform that allows users to create, read, update, and delete blog posts. It also supports user authentication and commenting on posts.

## Features

- User authentication (signup, login, logout)
- CRUD operations for blog posts
- Commenting on blog posts
- RESTful API endpoints using Django Rest Framework
- Class-based views for better organization and reusability


## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd blogging_platform
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the blog at `http://127.0.0.1:8000/`
- Use the authentication system to sign up, log in, and manage your profile.
- Create, edit, and delete blog posts.
- Comment on posts to engage with the content.

## API Endpoints

- `POST /api/posts/` - Create a new post
- `GET /api/posts/` - List all posts
- `GET /api/posts/<id>/` - Retrieve a specific post
- `PUT /api/posts/<id>/` - Update a specific post
- `DELETE /api/posts/<id>/` - Delete a specific post
- `POST /api/posts/<post_id>/comments/` - Add a comment to a post

