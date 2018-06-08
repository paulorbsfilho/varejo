from django.urls import path
from django.contrib import admin

from core import views

admin.autodiscover()

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
]