from django.shortcuts import render

# View per la homepage
def index(request):
    return render(request, 'index.html')

# View per la pagina di prenotazione
def booking_view(request):
    return render(request, 'booking.html')

# View per la pagina delle camere disponibili
def rooms(request):
    return render(request, 'rooms.html')

# View per la gestione delle prenotazioni
def manage_booking(request):
    return render(request, 'manage-booking.html')
