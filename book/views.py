from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

# Create your views here.
def book_party(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
#           booking.customer = request.user
            if Booking.objects.filter(date=booking.date, time_slot=booking.time_slot).exists():
                messages.error(request, 'This time slot is already booked.')
            else:
                booking.save()
                messages.success(request, 'Party booked successfully!')
                return redirect('booking:party_list')
    else:
        form = BookingForm()
    return render(request, 'book/book_party.html', {'form': form})