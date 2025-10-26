 "Movie Booking System"

 
  description: >
    A simple Django-based web application to browse movies and book tickets. 
    Users can choose from Silver, Gold, and Platinum tickets. 
    The system includes an admin panel to manage movies and view bookings.
  version: "1.0.0"
  author: "Swaminadhan G"
  license: "MIT"

features:
  table:
    - feature: "View available movies with showtime, description, and duration"
    - feature: "Book tickets by selecting ticket type and number of tickets"
    - feature: "Confirmation page for bookings"
    - feature: "Admin panel to add, update, and manage movies and bookings"
    - feature: "Ticket type pricing support (Silver, Gold, Platinum)"
    - feature: "Basic seat availability management"
    - feature: "Responsive templates using simple CSS"

technologies:
  table:
    - category: "Backend"
      items: ["Django 4.x", "Python 3.11+"]
    - category: "Database"
      items: ["SQLite (default)"]
    - category: "Frontend"
      items: ["HTML5", "CSS3", "Django Templates"]
    - category: "Tools"
      items: ["VS Code", "Git", "PowerShell / Command Prompt"]

installation:
  table:
    - step: "Clone the repository"
      command: "git clone <repo_url>"
    - step: "Navigate into project folder"
      command: "cd movie_booking"
    - step: "Create virtual environment"
      command: "python -m venv .venv"
    - step: "Activate virtual environment"
      powershell: ".venv\\Scripts\\Activate.ps1"
      cmd: ".venv\\Scripts\\activate.bat"
    - step: "Install dependencies"
      command: "pip install -r requirements.txt"
    - step: "Apply migrations"
      command: |
        python manage.py makemigrations
        python manage.py migrate
    - step: "Create superuser for admin"
      command: "python manage.py createsuperuser"
    - step: "Run development server"
      command: "python manage.py runserver"

usage:
  table:
    - action: "Open Home Page"
      url: "http://127.0.0.1:8000/"
      notes: "Browse available movies and book tickets"
    - action: "Access Admin Panel"
      url: "http://127.0.0.1:8000/admin/"
      notes: "Manage movies and view bookings"

project_structure:
  table:
    - directory: "movie_booking/"
      contents: "manage.py, movie_booking/ (settings.py, urls.py, wsgi.py)"
    - directory: "movies/"
      contents: "models.py, views.py, urls.py, admin.py, forms.py, templates/movies/ (base.html, movie_list.html, booking_form.html, booking_confirmation.html)"

notes:
  table:
    - note: "Ensure `show_time` for movies is set in the future to appear in listings"
    - note: "Use `.venv` virtual environment for development"
    - note: "For production, set proper `ALLOWED_HOSTS` and secure `SECRET_KEY`"
    - note: "Seat availability and ticket pricing can be customized in the models"

future_improvements:
  table:
    - improvement: "User authentication for personalized bookings"
    - improvement: "Payment gateway integration"
    - improvement: "Seat selection UI"
    - improvement: "PDF ticket generation and email confirmation"
    - improvement: "Reporting dashboard for admin"
