from django.contrib import admin
# Register your models here.
from .models import *
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','cost']
    search_fields = ['name','cost']
    list_filter = ['cost']
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_filter = ['student_count']
    list_display = ['name','student_count']
    search_fields = ['name','student_count']
@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ['name','education','status','start','finish']
    list_filter = ['status','education','start','finish']
    search_fields = ['name','course']
admin.site.register(ClassRoom)