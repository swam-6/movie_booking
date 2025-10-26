from django.db import models
from django.utils import timezone

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in minutes")
    show_time = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['show_time']


class Booking(models.Model):
    TICKET_CHOICES = [
        ('SILVER', 'Silver'),
        ('GOLD', 'Gold'),
        ('PLATINUM', 'Platinum'),
    ]

    user_name = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='bookings')
    ticket_type = models.CharField(max_length=10, choices=TICKET_CHOICES)
    number_of_tickets = models.PositiveIntegerField()
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_name} - {self.movie.title}"

    class Meta:
        ordering = ['-booking_date']
