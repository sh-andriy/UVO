from django.urls import path
from . import views

app_name = 'proekts'

urlpatterns = [
    path('', views.home, name='home'),
]
