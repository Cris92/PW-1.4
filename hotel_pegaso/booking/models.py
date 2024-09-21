from django.db import models
from django.utils import timezone
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    services = models.ManyToManyField(Tag, related_name='rooms')
    image = models.ImageField(upload_to='rooms/', default='rooms/default_image.jpg')
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)  # Valutazione da 0 a 10

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])

    def get_star_rating(self):
        """Ritorna una lista di stelle con 'full', 'half', o 'empty' in base alla valutazione."""
        full_stars = int(self.rating // 2)
        half_star = int((self.rating % 2) >= 1)
        empty_stars = 5 - (full_stars + half_star)
        return ['full'] * full_stars + ['half'] * half_star + ['empty'] * empty_stars

    def get_rating_text(self):
        """Ritorna il testo corrispondente alla valutazione."""
        if self.rating >= 9:
            return "Eccezionale"
        elif self.rating >= 8:
            return "Ottimo"
        elif self.rating >= 7:
            return "Buono"
        elif self.rating >= 6:
            return "Discreto"
        elif self.rating >= 5:
            return "Sufficiente"
        else:
            return "Scarso"


class BookingUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    user = models.ForeignKey(BookingUser, on_delete=models.CASCADE,null=True)  # Se vuoi collegare a un utente
    booking_code = models.CharField(max_length=20, unique=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Booking {self.booking_code} for {self.room.name} from {self.checkin_date} to {self.checkout_date}'
