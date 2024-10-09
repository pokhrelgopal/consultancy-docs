from django.shortcuts import render, redirect
from users.models import User, Consultancy
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "consultancy/index.html")

def error(request):
    return render(request, "error.html")

@login_required(login_url="login")
def dashboard(request):
    consultancy = Consultancy.objects.values("slug").get(user=request.user)
    consultancy_url = (
        f"{request.build_absolute_uri('/')}auth/register/student/{consultancy['slug']}/"
    )
    context = {"consultancy_url": consultancy_url}
    return render(request, "dashboard/dashboard.html", context)


@login_required(login_url="login")
def manage_students(request):
    return render(request, "dashboard/manage_students.html")


@login_required(login_url="login")
def manage_applications(request):
    return render(request, "dashboard/manage_applications.html")


@login_required(login_url="login")
def plans(request):
    return render(request, "dashboard/plans.html")


@login_required(login_url="login")
def settings(request):
    return render(request, "dashboard/settings.html")
