from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime,timedelta
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.http import JsonResponse

import uuid
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# View per la homepage
def index(request):
    return render(request, 'index.html')

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})
def select_dates(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    
    if request.method == 'GET':
        return render(request, 'select_dates.html', {'room': room})
    
def room_detail(request, pk):
    room = Room.objects.get(pk=pk)
    return render(request, 'room.html', {'room': room})

def select_dates(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    bookings = Booking.objects.filter(room=room)
    
    # Genera una lista di date non disponibili
    unavailable_dates = []
    for booking in bookings:
        current_date = booking.checkin_date
        while current_date <= booking.checkout_date:
            unavailable_dates.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=1)

    if request.method == 'GET':
        return render(request, 'select_dates.html', {'room': room, 'unavailable_dates': unavailable_dates})

def confirm_booking(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')

    # Calcolo del prezzo totale
    checkin_date = datetime.strptime(checkin, '%Y-%m-%d')
    checkout_date = datetime.strptime(checkout, '%Y-%m-%d')
    days = (checkout_date - checkin_date).days
    total_price = days * room.price_per_night

    context = {
        'room': room,
        'checkin': checkin,
        'checkout': checkout,
        'total_price': total_price
    }
    return render(request, 'confirm_booking.html', context)

def complete_booking(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')

    # Generazione di un codice di prenotazione univoco
    booking_code = get_random_string(8)

    # Creazione della prenotazione
    Booking.objects.create(
        room=room,
        checkin_date=datetime.strptime(checkin, '%Y-%m-%d'),
        checkout_date=datetime.strptime(checkout, '%Y-%m-%d'),
        booking_code=booking_code,
    )

    context = {
        'room': room,
        'checkin': checkin,
        'checkout': checkout,
        'booking_code': booking_code
    }

    return render(request, 'complete_booking.html', context)

def generate_pdf(request, booking_code):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "Conferma Prenotazione")
    p.drawString(100, 730, f"Codice Prenotazione: {booking_code}")
    p.drawString(100, 710, "Grazie per aver prenotato con noi!")
    p.showPage()
    p.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Prenotazione_{booking_code}.pdf"'
    return response

def manage_booking(request):
    if request.method == 'POST':
        booking_code = request.POST.get('booking_code')
        try:
            booking = Booking.objects.get(booking_code=booking_code)
            return redirect('edit_booking_view', booking_id=booking.id)
        except Booking.DoesNotExist:
            return render(request, 'manage_booking.html', {'error': 'Codice prenotazione non valido.'})

    return render(request, 'manage_booking.html')

def edit_booking_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    room = booking.room  # La stanza associata alla prenotazione
    bookings = Booking.objects.filter(room=room)
    
    # Genera una lista di date non disponibili
    unavailable_dates = []
    for booking_iteration in bookings:
        if booking_iteration.id != booking_id:
            current_date = booking_iteration.checkin_date
            while current_date <= booking_iteration.checkout_date:
                unavailable_dates.append(current_date.strftime('%Y-%m-%d'))
                current_date += timedelta(days=1)

    return render(request, 'edit_booking.html', {'checkin_date':booking.checkin_date.strftime('%Y-%m-%d'),'checkout_date':booking.checkout_date.strftime('%Y-%m-%d'),'booking': booking, 'unavailable_dates': unavailable_dates})

def edit_booking_post(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    room = booking.room  # La stanza associata alla prenotazione
    print (request.method)
    print (request.POST)
    action = request.POST.get('action')
    if request.method == 'POST':
        try:
            if action == 'delete':
                booking.delete()
                return JsonResponse({'status': 'success', 'action': 'deleted'})

            elif action == 'update':
                checkin = request.POST.get('checkin_date')
                checkout = request.POST.get('checkout_date')

                new_checkin_date = datetime.strptime(checkin, '%Y-%m-%d').date()
                new_checkout_date = datetime.strptime(checkout, '%Y-%m-%d').date()

                # Verifica le date non disponibili
                conflicting_bookings = Booking.objects.filter(
                    room=room,
                    checkin_date__lt=new_checkout_date,
                    checkout_date__gt=new_checkin_date
                ).exclude(id=booking.id)

                if conflicting_bookings.exists():
                    return JsonResponse({'status': 'error', 'message': 'Le date selezionate non sono disponibili per questa stanza.'})

                # Se non ci sono conflitti, aggiorna la prenotazione
                booking.checkin_date = new_checkin_date
                booking.checkout_date = new_checkout_date
                booking.save()

                # Genera il PDF
                pdf_url = f"/booking/{booking.booking_code}/download_pdf/"

                return JsonResponse({'status': 'success', 'action': 'updated', 'pdf_url': pdf_url})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Metodo non consentito'}, status=405)