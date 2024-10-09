from django.urls import path
from . import views

urlpatterns = [
    path("student/home", views.home, name="student_home"),
    path("student/profile", views.profile, name="student_profile"),
    path("student/documents", views.documents, name="student_documents"),
    path("student/applications", views.applications, name="student_applications"),
]
