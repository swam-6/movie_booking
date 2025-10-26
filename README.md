#project:
  name: "Movie Booking"
  description: 
    A **Django-based Movie Booking System** that allows users to browse movies,
    select ticket types (Silver, Gold, Platinum), book tickets, and view booking
    confirmations. The system includes an admin panel to manage movies and bookings.
  version: "1.0.0"
  author: "Swaminadhan G"
  license: "MIT"

features:
  - "Browse available movies with showtime, description, and duration."
  - "Book tickets by selecting ticket type and number of tickets."
  - "View booking confirmation after successful booking."
  - "Admin panel to manage movies and bookings."
  - "Support for Silver, Gold, and Platinum ticket types."
  - "Basic seat availability management."
  - "Responsive design using HTML and CSS templates."

technologies:
  backend:
    - "Django 4.x"
    - "Python 3.11+"
  database:
    - "SQLite (default)"
  frontend:
    - "HTML5"
    - "CSS3"
    - "Django Templates"
  tools:
    - "VS Code"
    - "Git"
    - "PowerShell / Command Prompt"

installation:
  steps:
    - description: "Clone the repository"
      command: "git clone <repo_url>"
    - description: "Navigate to project folder"
      command: "cd movie_booking"
    - description: "Create virtual environment"
      command: "python -m venv .venv"
    - description: "Activate virtual environment"
      powershell: ".venv\\Scripts\\Activate.ps1"
      cmd: ".venv\\Scripts\\activate.bat"
    - description: "Install dependencies"
      command: "pip install -r requirements.txt"
    - description: "Apply database migrations"
      command: |
        python manage.py makemigrations
        python manage.py migrate
    - description: "Create superuser for admin access"
      command: "python manage.py createsuperuser"
    - description: "Run development server"
      command: "python manage.py runserver"

usage:
  table:
    - action: "Access Home Page"
      url: "http://127.0.0.1:8000/"
      description: "Browse available movies and book tickets."
    - action: "Book Tickets"
      url: "http://127.0.0.1:8000/"
      description: "Select movie, ticket type, enter user details, and confirm booking."
    - action: "Admin Panel"
      url: "http://127.0.0.1:8000/admin/"
      description: "Manage movies, view all bookings, and update data."

project_structure:
  table:
    - directory: "movie_booking/"
      contents: "manage.py, movie_booking/ (settings, urls, wsgi)"
    - directory: "movies/"
      contents: "models.py, views.py, urls.py, admin.py, forms.py, templates/movies/"

notes:
  - "Ensure movie show_time is in the future to appear in listings."
  - "Use `.venv` virtual environment for development."
  - "For production, configure `ALLOWED_HOSTS` and secure `SECRET_KEY`."
  - "Seat availability and ticket pricing can be customized in the models."

future_improvements:
  - "Add user authentication for personalized booking history."
  - "Integrate payment gateway for online booking."
  - "Implement interactive seat selection."
  - "Generate PDF tickets and send email confirmation."
  - "Add reporting dashboard for admin analytics."
