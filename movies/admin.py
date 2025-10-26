from django.contrib import admin
from .models import Movie, Booking

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'show_time')
    list_filter = ('show_time',)
    search_fields = ('title', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'movie', 'ticket_type', 'number_of_tickets', 'booking_date')
    list_filter = ('ticket_type', 'booking_date', 'movie')
    search_fields = ('user_name', 'movie__title')
    readonly_fields = ('booking_date',)
