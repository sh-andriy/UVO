from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("login/", views.sing_in, name="login"),
    path("register/", views.sing_up, name="register"),
    path("logout/", views.sign_out, name="logout"),
]
