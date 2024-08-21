from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BowlingAlley, Lane, Reservation
from .forms import ReservationForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Reservation
from .forms import ReservationForm
from twilio.rest import Client

def home(request):
    alleys = BowlingAlley.objects.all()
    return render(request, 'index.html', {'alleys': alleys})


def book_lane(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            message_body = f"""
            {reservation.user_name},

Twoja rezerwacja została potwierdzona!

Szczegóły:

Miejsce: {reservation.lane.bowling_alley.name}
Pokój: {reservation.lane.number}
Rozpoczęcie: {reservation.start_time}
Zakończenie: {reservation.end_time}

Jeśli miałbyś jakieś pytania napisz do nas.

Miłego dnia,
Zespół ResPlace
            """

            message = client.messages.create(
                body=message_body,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=reservation.phone_number,
            )

           
            return redirect('reservation_confirm', reservation_id=reservation.id)
    else:
        form = ReservationForm()
    return render(request, 'book_lane.html', {'form': form})


def reservation_confirm(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'reservation_confirm.html', {'reservation': reservation})
