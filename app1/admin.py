from django.contrib import admin
from app1.models import user_data, complaint, schemes, notice, appointment

@admin.register(user_data)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'adhar', 'address', 'password', 'image')

@admin.register(complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'subject', 'message', 'image')

@admin.register(schemes)
class SchemesAdmin(admin.ModelAdmin):
    list_display = ('s_id', 's_name', 's_detail')

@admin.register(notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('n_name', 'n_date', 'n_detail')

@admin.register(appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'purpose', 'date', 'time', 'action')

# Register your models here.