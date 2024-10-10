from django.shortcuts import render, redirect
from .models import Profile, Education, LanguageTest, Document
from .forms import ProfileForm, EducationForm, LanguageTestForm, DocumentForm
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
        try:
            Education.objects.create(user=request.user, **form.cleaned_data)
            messages.success(request, "Education details updated successfully.")
        except IntegrityError:
            messages.error(request, "This education detail already exists.")
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
    lng = LanguageTest.objects.get(id=pk)
    if lng.user != request.user:
        messages.error(request, "You are not authorized to delete this test score.")
        return redirect("student_profile_test_scores")
    lng.delete()
    messages.success(request, "Test score deleted successfully.")
    return redirect("student_profile_test_scores")


@login_required(login_url="login")
def edit_test_score(request, pk):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    test_score = LanguageTest.objects.filter(id=pk).first()
    if not test_score:
        messages.error(request, "Test score not found.")
        return redirect("student_profile_test_scores")
    form = LanguageTestForm(
        request.POST or None, request.FILES or None, instance=test_score
    )
    if request.method == "POST" and form.is_valid():
        try:
            form.save()
            test_document = form.cleaned_data.get("test_document")
            if test_document:
                form.instance.test_document = upload_to_bunnycdn(test_document)
                form.save()
            messages.success(request, "Test score updated successfully.")
            return redirect("student_profile_test_scores")
        except Exception as e:
            messages.error(
                request,
                "An error occurred while updating the test score. Please try again later.",
            )
    return render(request, "student/edit_test.html", {"form": form})


@login_required(login_url="login")
def documents(request):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")

    form = DocumentForm(request.POST or None, request.FILES or None)
    documents = Document.objects.filter(user=request.user)

    if request.method == "POST" and form.is_valid():
        try:
            document_file = request.FILES.get("document_file")
            if document_file:
                cdn_url = upload_to_bunnycdn(document_file)
                form.instance.document_file = cdn_url
            Document.objects.create(user=request.user, **form.cleaned_data)
            messages.success(request, "Document uploaded successfully.")
        except IntegrityError:
            messages.error(request, "This document already exists.")
        except Exception as e:
            messages.error(request, f"Error uploading document: {e}")

    context = {"form": form, "documents": documents}
    return render(request, "student/documents.html", context)


@login_required(login_url="login")
def delete_document(request, pk):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    doc = Document.objects.get(id=pk)
    if doc.user != request.user:
        messages.error(request, "You are not authorized to delete this document.")
        return redirect("student_documents")
    doc.delete()
    messages.success(request, "Document deleted successfully.")
    return redirect("student_documents")


@login_required(login_url="login")
def counsellor_documents(request):
    if request.user.role != "student":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("error")
    return render(request, "student/counsellor_documents.html")
