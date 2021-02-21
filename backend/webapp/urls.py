"""webapp URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
import iscrizioni.views

admin.site.site_header = f'Manager eventi rev.{settings.APP_VERSION}'
admin.site.index_title = 'Amministrazione eventi'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('csrf/', iscrizioni.views.csrf),
    path('confirm/<str:token>/', iscrizioni.views.confirm_email),
    path('api/list/', iscrizioni.views.list_eventi),
    path('api/events/<slug:slug>/', iscrizioni.views.campi_form),
    path('api/events/<slug:slug>/subscribe/', iscrizioni.views.subscribe),
    # TODO email verification?
]
