# Django API Task Manager

A backend API built using Django and Django REST Framework to manage tasks, complementing the Next.js frontend.

## Features

- **Task Management:** Create, update, delete, and retrieve tasks via REST API.
- **Authentication:** Secure user authentication using JWT.
- **Django Admin Panel:** Manage tasks and users through the built-in admin panel.

## Prerequisites

- **Python 3.x:** Ensure you have Python installed. Download it from [python.org](https://www.python.org/).
- **Pip & Virtual Environment:** Install pip and use a virtual environment for package management.

## Installation

1. Clone the repository:

git clone https://github.com/kkadk/django-api-project-task_manager.git

2. Navigate to the project directory:

cd django-api-project-task_manager

3. Create and activate a virtual environment:

python3 -m venv venv

4. Activate the virtual environment:

# On Windows
env\Scripts\activate

# On macOS/Linux
source env/bin/activate

5. Install Dependencies:

pip install -r requirements.txt

### 6. Apply Migrations:

python manage.py migrate

### 7. Create a Superuser (For Admin Panel):

python manage.py createsuperuser

### 8. Run the Development Server:

python manage.py runserver

### 9. Access the Admin Panel:

Visit `http://127.0.0.1:8000/api/` in your browser or use Postman.

## Configuration

- **Environment Variables:** Configure the `.env` file for sensitive settings like database credentials and secret keys.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.


