from django.contrib import admin

# Register your models here.
from .models import StudentPayment
@admin.register(StudentPayment)
class StudentPaymentAdmin(admin.ModelAdmin):
    list_filter = ['date']
    list_display = ['student','user','cost','date']
    list_per_page = 10
