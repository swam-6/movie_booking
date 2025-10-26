# movies/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Movie, Booking  # ✅ Import Booking here
from .forms import BookingForm

def movie_list(request):
    """
    Display all movies in the system.
    """
    # Show all movies (future or past)
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def booking_form(request, movie_id):
    """
    Display and process the booking form for a selected movie.
    """
    movie = get_object_or_404(Movie, id=movie_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.movie = movie
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    
    return render(request, 'movies/booking_form.html', {'form': form, 'movie': movie})

def booking_confirmation(request, booking_id):
    """
    Display booking confirmation page for a given booking.
    """
    booking = get_object_or_404(Booking, id=booking_id)  # ✅ Booking is now defined
    return render(request, 'movies/booking_confirmation.html', {'booking': booking})
