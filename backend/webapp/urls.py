"""webapp URL Configuration"""
from django.contrib import admin
from django.urls import path
import iscrizioni.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/list/', iscrizioni.views.list_eventi),
    path('api/events/<slug:slug>/', iscrizioni.views.campi_form),
    path('api/events/<slug:slug>/subscribe/', iscrizioni.views.subscribe),
    # TODO email verification?
]
