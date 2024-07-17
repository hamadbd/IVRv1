# IvrV1 Project

## Overview

IvrV1 is a Django-based web application that provides user authentication and voice recording functionalities. Users can register with their Date of Birth (DOB) and Date of Arrival (DOA), and authenticate using their ID, DOB, and DOA. Upon successful authentication, users can be redirected to a page to record their voice.

## Features

- User registration with DOB, DOA, and password
- User authentication with ID, DOB, and DOA
- JWT token-based authentication
- Password hashing using bcrypt
- Server-side validation of user input
- PostgreSQL database for storing user and recording data
- Basic logging and error handling
- Login functionality for users created by the admin
- Viewing and playing saved recordings in a table



## Project Structure

IvrV1/
│
├── IvrV1/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
├── authentication/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ ├── migrations/
│ ├── init.py
│
├── home/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── views.py
│ ├── urls.py
│ ├── migrations/
│ ├── init.py
│
├── templates/
│ ├── base.html
│ ├── register.html
│ ├── ivr_call.html
│ ├── authenticated_page.html
│ ├── login.html
│ ├── home.html
│ ├── recording_list.html
│
├── manage.py
└── debug.log



## Setup Instructions

### Prerequisites

- Python 3.x
- PostgreSQL
- `pip` (Python package installer)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/hamadbd/IvrV1.git
    cd IvrV1
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure PostgreSQL**:
    - Create a PostgreSQL database and user with the necessary permissions.
    - Update the `DATABASES` settings in `IvrV1/settings.py` with your database details.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Run database migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser** (for accessing the Django admin interface):

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

8. **Access the application**:
    - Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Homepage**: `http://127.0.0.1:8000/`
- **Registration Form**: `http://127.0.0.1:8000/register/`
- **IVR Call Form**: `http://127.0.0.1:8000/ivr_call/`
- **Login Form**: `http://127.0.0.1:8000/login/`
- **Recorded Audios**: `http://127.0.0.1:8000/recordings/`

## Logging

The application uses basic logging to record debug information. Logs are saved to `debug.log` in the project root directory.

## License

This project is licensed under the MIT License.
