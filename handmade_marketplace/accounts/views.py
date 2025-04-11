from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User

class CustomLoginView(LoginView):
    template_name = "registration/login.html"  # Ensure this matches the template location
    success_url = reverse_lazy("home")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                login(request, user)  # Automatically log in the user after registration
                return redirect("home")  # Redirect to home page
        else:
            messages.error(request, "Passwords do not match")

    return render(request, "registration/register.html")  # Correct template path
