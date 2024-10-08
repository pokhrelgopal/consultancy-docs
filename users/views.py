from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .validation import Validation as v
from .models import User


def index(request):
    return render(request, "consultancy/index.html")


def login(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)

        if v.is_any_empty(email, password):
            messages.error(request, "All fields are required.")
            return render(request, "auth/login.html")

        if user is not None:
            auth_login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "auth/login.html")


@login_required(login_url="login")
def logout(request):
    auth_logout(request)
    return redirect("login")


def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if v.is_any_empty(full_name, email, password, confirm_password):
            messages.error(request, "All fields are required.")
            return render(request, "auth/register.html")

        if not v.match(password, confirm_password):
            messages.error(request, "Password does not match.")
            return render(request, "auth/register.html")

        if not v.is_valid_email(email):
            messages.error(request, "Invalid email.")
            return render(request, "auth/register.html")

        try:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already taken.")
                return render(request, "auth/register.html")
            user = User.objects.create_user(
                email=email, password=password, full_name=full_name
            )
            user.save()
            auth_login(request, user)
            return redirect("onboarding", pk=user.id)
        except Exception as e:
            messages.error(request, "Something went wrong.")
            return render(request, "auth/register.html")

    return render(request, "auth/register.html")


def onboarding(request, pk):
    user = User.objects.get(id=pk)
    if user != request.user:
        return redirect("login")
    return render(request, "consultancy/onboarding.html")
