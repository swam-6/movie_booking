# Movie Booking System

A simple **Django-based web application** to browse movies and book tickets.  
Users can choose from **Silver, Gold, and Platinum tickets**.  
The system includes an **admin panel** to manage movies and view bookings.

---

## Version
**1.0.0**

## Author
**Swaminadhan G**

## License
**MIT**

---

## Features

| Feature |
|---------|
| View available movies with showtime, description, and duration |
| Book tickets by selecting ticket type and number of tickets |
| Confirmation page for bookings |
| Admin panel to add, update, and manage movies and bookings |
| Ticket type pricing support (Silver, Gold, Platinum) |
| Basic seat availability management |
| Responsive templates using simple CSS |

---

## Technologies

| Category | Tools |
|----------|-------|
| Backend  | Django 4.x, Python 3.11+ |
| Database | SQLite (default) |
| Frontend | HTML5, CSS3, Django Templates |
| Tools    | VS Code, Git, PowerShell / Command Prompt |

---

## Installation

| Step | Command |
|------|---------|
| Clone the repository | `git clone <repo_url>` |
| Navigate into project folder | `cd movie_booking` |
| Create virtual environment | `python -m venv .venv` |
| Activate virtual environment (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Activate virtual environment (CMD) | `.venv\Scripts\activate.bat` |
| Install dependencies | `pip install -r requirements.txt` |
| Apply migrations | ```python python manage.py makemigrations python manage.py migrate ``` |
| Create superuser for admin | `python manage.py createsuperuser` |
| Run development server | `python manage.py runserver` |

---

## Usage

| Action | URL | Notes |
|--------|-----|-------|
| Open Home Page | [http://127.0.0.1:8000/](http://127.0.0.1:8000/) | Browse available movies and book tickets |
| Access Admin Panel | [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) | Manage movies and view bookings |

---

## Project Structure

| Directory | Contents |
|-----------|---------|
| movie_booking/ | `manage.py`, `movie_booking/` (settings.py, urls.py, wsgi.py) |
| movies/ | models.py, views.py, urls.py, admin.py, forms.py, templates/movies/ (base.html, movie_list.html, booking_form.html, booking_confirmation.html) |

---

## Notes
- Ensure `show_time` for movies is set in the future to appear in listings.  
- Use `.venv` virtual environment for development.  
- For production, set proper `ALLOWED_HOSTS` and secure `SECRET_KEY`.  
- Seat availability and ticket pricing can be customized in the models.

---

## Future Improvements
- User authentication for personalized bookings  
- Payment gateway integration  
- Interactive seat selection UI  
- PDF ticket generation and email confirmation  
- Reporting dashboard for admin
