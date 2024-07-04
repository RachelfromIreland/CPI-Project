from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


# Create your views here.
# Party booking
@login_required
def book_party(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.customer = request.user
            if Booking.objects.filter(date=new_booking.date, time_slot=new_booking.time_slot).exists():
                messages.error(request, 'This time slot is already booked.')
            else:
                new_booking.save()
                messages.success(request, 'Party booked successfully!')
                return redirect('book:party_list')
    else:
        form = BookingForm()
    return render(request, 'book/book_party.html', {'form': form})


# Party list
@login_required
def party_list(request):
    bookings = Booking.objects.filter(customer=request.user)
    return render(request, 'book/party_list.html', {'bookings': bookings})


# Edit booking
@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('book:party_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'book/edit_booking.html', {'form': form, 'booking': booking})


# Delete booking
@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('book:party_list')

    return render(request, 'book/delete_booking.html', {'booking': booking})
