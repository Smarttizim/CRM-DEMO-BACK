from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
class DirectorForm(UserCreationForm):
    class Meta:
        model = Director
        fields = "__all__"
class ManagerForm(UserCreationForm):
    class Meta:
        model = Manager
        fields = "__all__"
class TeacherForm(UserCreationForm):
    subject = forms.CharField(max_length=150)
    description =  forms.Textarea()
    class Meta:
        model = Teacher
        fields = "__all__"
