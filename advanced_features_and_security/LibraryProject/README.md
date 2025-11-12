# LibraryProject

## Overview
This is the initial Django project setup for the **ALX Django Learn Lab**.  
The purpose of this project is to understand the basic structure of a Django project and run the development server successfully.

## Steps Completed
1. Installed Django using `pip install django`
2. Created a new Django project named `LibraryProject`
3. Started the development server using `python manage.py runserver`
4. Verified that the default Django welcome page appears at `http://127.0.0.1:8000/`

## Project Structure Overview

### Key Files:
- **manage.py:** Command-line tool for interacting with the project.
- **settings.py:** Stores project configuration (apps, middleware, database, etc.).
- **urls.py:** URL routes for the project.
- **wsgi.py / asgi.py:** Used for deployment and server communication.

## Author
# Django Permissions and Groups

## Groups
- **Editors:** can_create, can_edit
- **Viewers:** can_view
- **Admins:** can_view, can_create, can_edit, can_delete

## Permissions
- Defined in `Book` model (`models.py`) under Meta:
  - can_view
  - can_create
  - can_edit
  - can_delete

## Usage
- Use `@permission_required('myapp.can_edit', raise_exception=True)` in views.
- Assign users to groups via admin panel or Django shell.

