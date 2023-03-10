from django.shortcuts import render
# For Multilanguage
from django.utils import translation
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
# ####################
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from .models import *
class DirectorViewset(ModelViewSet):
    queryset =  Director.objects.all()
    serializer_class = DirectorSerializer
class ManagerViewset(ModelViewSet):
    queryset =  Manager.objects.all()
    serializer_class = ManagerSerializer
class TeacherViewset(ModelViewSet):
    queryset =  Teacher.objects.all()
    serializer_class =TeacherSerializer
    