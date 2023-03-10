from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','phone','parent','birth']
    list_filter = ['added']
    search_fields =  ['name','phone','parent','birth']
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        print(obj.user.role)
        if obj.user.role == 'MANAGER' or obj.user.role=='DIRECTOR':
            super().save_model(request, obj, form, change)
@admin.register(Davomat)
class DavomatAdmin(admin.ModelAdmin):
    list_display = ['student','date','info']
    list_filter = ['date','status']
    list_per_page = 10
    search_fields = ['student','description']
    # def save_model(self, request, obj, form, change):
    #     print(obj.user.role)
    #     if obj.user.role == 'MANAGER' or obj.user.role=='DIRECTOR':
    #         super().save_model(request, obj, form, change)
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_filter = ['test_kodi']
    list_display = ['test_kodi','fan_nomi','talaba']
    search_fields = ['test_kodi','fan_nomi','talaba','telefon_raqam']
    list_per_page = 10