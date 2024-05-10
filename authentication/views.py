# from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == "POST":
        form: LoginForm = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(
                    request,
                    "authentication/login.html",
                    {"form": form, "error_message": "Invalid credentials"},
                )
        else:
            form = LoginForm()
            return render(request, "authentication/login.html", {"form": form})
