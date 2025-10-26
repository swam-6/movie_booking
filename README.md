project:
  name: Movie Booking System
  description: >
    A simple Django-based web application to browse movies and book tickets. 
    Users can choose from Silver, Gold, and Platinum tickets. 
    The system includes an admin panel to manage movies and view bookings.
  version: 1.0.0
  author: Swaminadhan G
  license: MIT

features:
  - View available movies with showtime, description, and duration
  - Book tickets by selecting ticket type and number of tickets
  - Confirmation page for bookings
  - Admin panel to add, update, and manage movies and bookings
  - Ticket type pricing support (Silver, Gold, Platinum)
  - Basic seat availability management
  - Responsive templates using simple CSS

technologies:
  backend:
    - Django 4.x
    - Python 3.11+
  database:
    - SQLite (default)
  frontend:
    - HTML5
    - CSS3
    - Django Templates
  tools:
    - VS Code
    - Git
    - PowerShell / Command Prompt

installation:
  - step: Clone the repository
    command: git clone <repo_url>
  - step: Navigate into project folder
    command: cd movie_booking
  - step: Create virtual environment
    command: python -m venv .venv
  - step: Activate virtual environment
    powershell: .venv\Scripts\Activate.ps1
    cmd: .venv\Scripts\activate.bat
  - step: Install dependencies
    command: pip install -r requirements.txt
  - step: Apply migrations
    command: |
      python manage.py makemigrations
      python manage.py migrate
  - step: Create superuser for admin
    command: python manage.py createsuperuser
  - step: Run development server
    command: python manage.py runserver

usage:
  - step: Open your browser
    url: http://127.0.0.1:8000/
  - step: Browse available movies and book tickets
  - step: Access admin panel
    url: http://127.0.0.1:8000/admin/
    notes: Manage movies and view bookings

project_structure:
  - movie_booking/
    - manage.py
    - movie_booking/
      - __init__.py
      - settings.py
      - urls.py
      - wsgi.py
    - movies/
      - __init__.py
      - models.py
      - views.py
      - urls.py
      - admin.py
      - forms.py
      - templates/
        - movies/
          - base.html
          - movie_list.html
          - booking_form.html
          - booking_confirmation.html

notes:
  - Ensure `show_time` for movies is set in the future to appear in listings
  - Use `.venv` virtual environment for development
  - For production, set proper `ALLOWED_HOSTS` and secure `SECRET_KEY`
  - Seat availability and ticket pricing can be customized in the models

future_improvements:
  - User authentication for personalized bookings
  - Payment gateway integration
  - Seat selection UI
  - PDF ticket generation and email confirmation
  - Reporting dashboard for admin
