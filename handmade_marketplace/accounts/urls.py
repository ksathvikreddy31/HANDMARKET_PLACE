
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, register_view  # No login_view needed

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),  # Correct login path

    #  path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", register_view, name="register"),  # Correct register path
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),  # Logout and redirect to login
]

