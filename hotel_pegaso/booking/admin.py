from django.contrib import admin
from .models import Room,Tag,Booking,BookingUser


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_night', 'available_services')
    list_filter = ('price_per_night', 'services')
    search_fields = ('name', 'description')
    ordering = ('name',)
    
    def available_services(self, obj):
        return ", ".join([service.name for service in obj.services.all()])
    available_services.short_description = 'Servizi Disponibili'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'checkin_date', 'checkout_date', 'booking_code', 'timestamp')
    list_filter = ('checkin_date', 'checkout_date', 'room')
    search_fields = ('booking_code', 'user__email', 'room__name')
    ordering = ('-timestamp',)
    date_hierarchy = 'checkin_date'

@admin.register(BookingUser)
class BookingUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('email',)
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)