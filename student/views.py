from django.shortcuts import render


def home(request):
    return render(request, "student/home.html")


def profile(request):
    return render(request, "student/profile.html")


def applications(request):
    return render(request, "student/applications.html")


def documents(request):
    return render(request, "student/documents.html")
