from django.shortcuts import render, redirect
from users.models import User, Consultancy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import ConsultancyForm
from django.db.models import Q
from student.forms import ProfileForm
from student.models import Profile


def index(request):
    return render(request, "consultancy/index.html")


def error(request):
    return render(request, "error.html")


@login_required(login_url="login")
def dashboard(request):
    if request.user.role != "consultancy":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    consultancy = Consultancy.objects.values("slug").get(user=request.user)
    consultancy_url = (
        f"{request.build_absolute_uri('/')}auth/register/student/{consultancy['slug']}/"
    )
    context = {"consultancy_url": consultancy_url}
    return render(request, "dashboard/dashboard.html", context)


@login_required(login_url="login")
def manage_students(request):
    if request.user.role != "consultancy":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    students = (
        User.objects.select_related("associated_with")
        .filter(associated_with=request.user.consultancy, role="student")
        .values("id", "full_name", "email", "date_joined")
    )
    q = request.GET.get("q")
    if q:
        students = students.filter(
            Q(full_name__icontains=q) | Q(email__icontains=q)
        ).values("full_name", "email", "date_joined")
    context = {"students": students}
    return render(request, "dashboard/manage_students.html", context)


@login_required(login_url="login")
def student_detail(request, pk):
    if request.user.role != "consultancy":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    try:
        student = User.objects.get(pk=pk)
        form = ProfileForm(request.POST or None)
        user = student
        profile = Profile.objects.filter(user=user).first()
        if profile:
            form = ProfileForm(request.POST or None, instance=profile)
        if request.method == "POST" and form.is_valid():
            Profile.objects.update_or_create(user=user, defaults=form.cleaned_data)
            messages.success(request, "Profile updated successfully.")

        return render(
            request, "dashboard/student_detail.html", {"student": student, "form": form}
        )
    except User.DoesNotExist:
        messages.error(request, "Student not found.")
        return redirect("manage_students")


@login_required(login_url="login")
def student_application(request, pk):
    if request.user.role != "consultancy":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    student = User.objects.get(pk=pk)
    return render(request, "dashboard/student_application.html", {"student": student})


@login_required(login_url="login")
def student_documents(request, pk):
    if request.user.role != "consultancy":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    student = User.objects.get(pk=pk)
    return render(request, "dashboard/student_documents.html", {"student": student})


@login_required(login_url="login")
def manage_applications(request):
    if request.user.role != "consultancy":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    return render(request, "dashboard/manage_applications.html")


@login_required(login_url="login")
def plans(request):
    if request.user.role != "consultancy":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    return render(request, "dashboard/plans.html")


@login_required(login_url="login")
def settings(request):
    if request.user.role != "consultancy":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    consultancy = Consultancy.objects.get(user=request.user)
    if request.method == "POST":
        form = ConsultancyForm(request.POST, instance=consultancy)
        if form.is_valid():
            form.save()
            messages.success(request, "Settings updated successfully.")
            return redirect("settings")
        else:
            messages.error(request, "An error occurred while updating settings.")
            return redirect("settings")
    else:
        form = ConsultancyForm(instance=consultancy)

    return render(request, "dashboard/settings.html", {"form": form})
