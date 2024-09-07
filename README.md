# Document Management System

Welcome to the **Document Management System** (DMS), a web application that allows users to securely manage their documents. Users can upload, view, delete, and download documents after logging in.

## Features

- **User Authentication**: Users can create an account, log in, and log out.
- **Upload Documents**: After logging in, users can upload documents to the system.
- **View Documents**: Users can view uploaded documents directly within the application.
- **Delete Documents**: Users can delete unwanted documents.
- **Download Documents**: Users can download their documents from the system.

## Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django (Python)
- **Database**: SQLite (default in Django)
- **Storage**: FileSystem (for document storage)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **Django 3.2+**: [Django Documentation](https://docs.djangoproject.com/en/stable/)

## Setup Instructions

Follow the steps below to set up the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/document-management-system.git
   cd document-management-system
   ```

2. **Create a virtual environment (optional but recommended)**:

  ```
  python -m venv env
  source env/bin/activate  # For Windows: env\Scripts\activate
 ```
3. **Install the dependencies**:

```bash
   pip install -r requirements.txt
```
4. **Run database migrations** :
```
  python manage.py migrate
```

5. **Create a superuser (optional, for admin access)**:
```
   python manage.py createsuperuser
```
6. **Run the development server**:
```
   python manage.py runserver
```
7. **Open your browser and navigate to http://127.0.0.1:8000/ to access the system.**

**Usage**
Sign Up: Register an account on the sign-up page.
Login: Log in to access your dashboard.
Upload Documents: Use the upload feature to add new documents.
View/Download/Delete Documents: Manage your documents with ease.

**Folder Structure**
```
document-management-system/
│
├── documents/                 # Application to handle document upload and management
│   ├── migrations/            # Django migration files
│   ├── templates/             # HTML templates for the web pages
│   ├── static/                # Static files (CSS, images)
│   ├── views.py               # Views for handling document operations
│   ├── models.py              # Models for Document and User
│   └── urls.py                # URL configurations for document app
│
├── DMS/                   # Django project settings
│   ├── settings.py            # Main project settings
│   └── urls.py                # Project-wide URLs
│
├── media/                     # Directory where uploaded documents are stored
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
└── README.md                  # This README file
```

