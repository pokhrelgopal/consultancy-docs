from django.shortcuts import render, redirect
from users.models import User


def index(request):
    return render(request, "consultancy/index.html")


def onboarding(request, pk):
    user = User.objects.get(id=pk)
    if user != request.user:
        return redirect("login")
    return render(request, "consultancy/onboarding.html")
