# from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
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
                    "user/login.html",
                    {"form": form, "error_message": "Invalid credentials"},
                    status=400,
                )
        else:
            return render(request, "user/login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "user/login.html", {"form": form})


def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(
                request,
                "user/registration.html",
                {"form": form, "error_message": form.errors},
                status=400,
            )
    else:
        form = RegistrationForm()
        return render(
            request,
            "user/registration.html",
            {"form": form},
        )


def logout_view(request):
    logout(request)
    return redirect("home")
