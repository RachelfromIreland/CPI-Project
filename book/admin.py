from django.contrib import admin
from .models import Booking
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_name', 'num_attending', 'date', 'time_slot', 'booking_date')
    list_filter = ('date', 'time_slot')
    search_fields = ('booking_name')
    ordering = ('date')

admin.site.register(Booking)