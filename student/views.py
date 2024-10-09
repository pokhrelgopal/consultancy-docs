from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url="login")
def home(request):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    profile_complete = Profile.objects.filter(user=request.user).exists()

    context = {"is_profile_complete": profile_complete}
    return render(request, "student/home.html", context)


@login_required(login_url="login")
def profile(request):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    form = ProfileForm(request.POST or None)
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    if profile:
        form = ProfileForm(request.POST or None, instance=profile)
    if request.method == "POST" and form.is_valid():
        Profile.objects.update_or_create(user=user, defaults=form.cleaned_data)
        messages.success(request, "Profile updated successfully.")
    return render(request, "student/profile.html", {"form": form})


@login_required(login_url="login")
def applications(request):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    return render(request, "student/applications.html")


@login_required(login_url="login")
def documents(request):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    return render(request, "student/documents.html")
