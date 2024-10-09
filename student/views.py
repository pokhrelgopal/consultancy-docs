from django.shortcuts import render, redirect
from .models import Profile, Education, LanguageTest
from .forms import ProfileForm, EducationForm, LanguageTestForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from core.utils import upload_to_bunnycdn


@login_required(login_url="login")
def home(request):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    profile_complete = Profile.objects.filter(user=request.user).exists()

    context = {"is_profile_complete": profile_complete}
    return render(request, "student/home.html", context)


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
def educational(request):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    form = EducationForm(request.POST or None)
    educations = Education.objects.filter(user=request.user).values(
        "level", "university_name", "end_date", "id"
    )
    if request.method == "POST" and form.is_valid():
        Education.objects.create(user=request.user, **form.cleaned_data)
        messages.success(request, "Education details updated successfully.")
    context = {"form": form, "educations": educations}
    return render(request, "student/educational.html", context)


@login_required(login_url="login")
def edit_education(request, pk):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    education = Education.objects.filter(id=pk).first()
    if not education:
        messages.error(request, "Education not found.")
        return redirect("student_profile_educational")
    form = EducationForm(request.POST or None, instance=education)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education updated successfully.")
        return redirect("student_profile_educational")
    return render(request, "student/edit_education.html", {"form": form})


@login_required(login_url="login")
def delete_education(request, pk):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    Education.objects.filter(id=pk).delete()
    messages.success(request, "Education deleted successfully.")
    return redirect("student_profile_educational")


@login_required(login_url="login")
def test_scores(request):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    form = LanguageTestForm(request.POST or None, request.FILES or None)
    test_scores = LanguageTest.objects.filter(user=request.user).values(
        "test", "score", "id"
    )
    if request.method == "POST" and form.is_valid():
        try:
            test_document = form.cleaned_data.get("test_document")
            if test_document:
                form.instance.test_document = upload_to_bunnycdn(test_document)
            LanguageTest.objects.create(user=request.user, **form.cleaned_data)
            messages.success(request, "Test score updated successfully.")
        except IntegrityError:
            messages.error(request, "Test score already exists.")
    context = {"form": form, "test_scores": test_scores}
    return render(request, "student/test_scores.html", context)


@login_required(login_url="login")
def delete_test_score(request, pk):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    LanguageTest.objects.filter(id=pk).delete()
    messages.success(request, "Test score deleted successfully.")
    return redirect("student_profile_test_scores")


@login_required(login_url="login")
def edit_test_score(request, pk):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")

    # Retrieve the test score record
    test_score = LanguageTest.objects.filter(id=pk).first()
    if not test_score:
        messages.error(request, "Test score not found.")
        return redirect("student_profile_test_scores")

    # Initialize form with POST and FILES data or the current instance
    form = LanguageTestForm(
        request.POST or None, request.FILES or None, instance=test_score
    )

    if request.method == "POST" and form.is_valid():
        try:
            # First save the form without uploading the file
            form.save()

            # Only upload the document if the form save was successful
            test_document = form.cleaned_data.get("test_document")
            if test_document:
                # Upload the document and update the form instance
                form.instance.test_document = upload_to_bunnycdn(test_document)
                form.save()  # Save again to update the document field

            messages.success(request, "Test score updated successfully.")
            return redirect("student_profile_test_scores")

        except Exception as e:
            # Handle any exception that occurs during form saving
            messages.error(
                request,
                "An error occurred while updating the test score. Please try again later.",
            )
            # Optionally log the exception
            # logger.error(f"Error during updating test score: {str(e)}")

    return render(request, "student/edit_test.html", {"form": form})
