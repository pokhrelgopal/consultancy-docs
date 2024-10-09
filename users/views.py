from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .validation import Validation as v
from .models import User, Consultancy
from .forms import ConsultancyForm


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
            if user.role == "consultancy":
                if (
                    not Consultancy.objects.select_related("user")
                    .filter(user=user)
                    .exists()
                ):
                    return redirect("onboarding", pk=user.id)
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
        role = request.POST.get("role")

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
                email=email.strip(),
                password=password,
                full_name=full_name.strip(),
                role=role,
            )
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect("login")
        except Exception as e:
            print(e)
            messages.error(request, "Something went wrong.")
            return render(request, "auth/register.html")

    return render(request, "auth/register.html")


def student_register(request, slug):
 
    if request.user.is_authenticated:
        return redirect("index")
    try:
        consultancy = Consultancy.objects.values("id", "name", "slug").get(slug=slug)
    except Consultancy.DoesNotExist:
        return redirect("index")
    return render(request, "auth/student_register.html", {"consultancy": consultancy})


@login_required
def onboarding(request, pk):
    user = get_object_or_404(User, id=pk)
    if user != request.user:
        return redirect("login")
    if Consultancy.objects.select_related("user").filter(user=user).exists():
        return redirect("index")
    form = ConsultancyForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        consultancy = form.save(commit=False)
        consultancy.user = user
        consultancy.save()
        return redirect("index")

    return render(request, "consultancy/onboarding.html", {"form": form})
