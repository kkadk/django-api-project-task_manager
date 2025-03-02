# Django API Task Manager

A backend API built using Django and Django REST Framework to manage tasks, complementing the Next.js frontend.

## Features

- **Task Management:** Create, update, delete, and retrieve tasks via REST API.
- **Authentication:** Secure user authentication using JWT.
- **Django Admin Panel:** Manage tasks and users through the built-in admin panel.
- **JWT Token:** based Authentication: Use JSON Web Tokens (JWT) for secure and stateless user authentication.


## Prerequisites

- **Python 3.x:** Ensure you have Python installed. Download it from [python.org](https://www.python.org/) or you can also use hombrew if you are on macOS.
- **Pip & Virtual Environment:** Install pip and use a virtual environment for package management.
- **Postman (Optional):** To test API endpoints locally (Optional but useful for manual testing).
- **Node.js & npm:** If you intend to run a Next.js frontend in parallel with this backend, ensure Node.js and npm are installed.


## Installation

1. Clone the repository:
```
git clone https://github.com/kkadk/django-api-project-task_manager.git
```
2. Navigate to the project directory:
```
cd django-api-project-task_manager
```
3. Create and activate a virtual environment:
```
python3 -m venv venv
```
4. Activate the virtual environment:
```
# On Windows
env\Scripts\activate
```
```
# On macOS/Linux
source env/bin/activate
```

5. Install Dependencies:
```
pip install -r requirements.txt
```
##  Apply Migrations:
```
python manage.py migrate
```
##  Create a Superuser (For Admin Panel):
```
python manage.py createsuperuser
```
## Run the Development Server:
```
python manage.py runserver
```
## Access URLs:

### 1. **Admin Panel:**  
   You can access the Django admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).


### 2. **User Management:**
   - **Register User:**  
     To register a new user, send a POST request to [http://127.0.0.1:8000/api/register/](http://127.0.0.1:8000/api/register/)
   
   - **Verify Email:**  
     To verify the user's email, send a GET request to [http://127.0.0.1:8000/api/verify-email/<token>/](http://127.0.0.1:8000/api/verify-email/<token>/)  
     Replace `<token>` with the actual verification token received in the registration email.

### 3. **Token Authentication:**
   These endpoints handle JWT authentication by issuing and refreshing access tokens:
   - **Obtain Access & Refresh Tokens (Login):**  
     POST request to [http://127.0.0.1:8000/api/token/](http://127.0.0.1:8000/api/token/)  
     Example request body:
     ```json
     {
       "username": "your_username",
       "password": "your_password"
     }
     ```

     Response:
     ```json
     {
       "access": "your_access_token_here",
       "refresh": "your_refresh_token_here"
     }
     ```

   - **Refresh Access Token:**  
     POST request to [http://127.0.0.1:8000/api/token/refresh/](http://127.0.0.1:8000/api/token/refresh/)  
     Example request body:
     ```json
     {
       "refresh": "your_refresh_token_here"
     }
     ```

     Response:
     ```json
     {
       "access": "new_access_token_here"
     }
     
### 4. **Task Management (CRUD Operations):**
   The following CRUD operations are available for tasks:
   - **Create Task:**  
     POST request to [http://127.0.0.1:8000/api/tasks/](http://127.0.0.1:8000/api/tasks/)
   
   - **Retrieve All Tasks:**  
     GET request to [http://127.0.0.1:8000/api/tasks/](http://127.0.0.1:8000/api/tasks/)
   
   - **Retrieve Specific Task:**  
     GET request to [http://127.0.0.1:8000/api/tasks/<task_id>/](http://127.0.0.1:8000/api/tasks/<task_id>/)  
     Replace `<task_id>` with the actual task ID to retrieve a specific task.
   
   - **Update Task:**  
     PUT/PATCH request to [http://127.0.0.1:8000/api/tasks/<task_id>/](http://127.0.0.1:8000/api/tasks/<task_id>/)  
     Replace `<task_id>` with the actual task ID to update a task.
   
   - **Delete Task:**  
     DELETE request to [http://127.0.0.1:8000/api/tasks/<task_id>/](http://127.0.0.1:8000/api/tasks/<task_id>/)  
     Replace `<task_id>` with the actual task ID to delete a task.

## Configuration

- **Environment Variables:** Configure the `.env` file for sensitive settings like database credentials and secret keys.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.


