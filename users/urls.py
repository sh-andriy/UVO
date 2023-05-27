from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("login/", views.sing_in, name="login"),
    path("register-volunteer/", views.sing_up_volunteer, name="register_volunteer"),
    path("logout/", views.sign_out, name="logout"),
]
