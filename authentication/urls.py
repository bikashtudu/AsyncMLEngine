from django.urls import path, re_path
from .views import login_view, registration_view, logout_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("signup/", registration_view, name="register"),
    path("logout/", logout_view, name="logout"),
]
