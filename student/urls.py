from django.urls import path
from . import views

urlpatterns = [
    path("student/home", views.home, name="student_home"),
    path("student/documents", views.documents, name="student_documents"),
    path("student/applications", views.applications, name="student_applications"),
    path("student/profile/personal", views.profile, name="student_profile"),
    path(
        "student/profile/education",
        views.educational,
        name="student_profile_educational",
    ),
    path(
        "student/profile/education/delete/<int:pk>",
        views.delete_education,
        name="delete_education",
    ),
    path(
        "student/profile/education/edit/<int:pk>",
        views.edit_education,
        name="edit_education",
    ),
    path(
        "student/profile/test-scores",
        views.test_scores,
        name="student_profile_test_scores",
    ),
    path(
        "student/profile/test-scores/delete/<int:pk>",
        views.delete_test_score,
        name="delete_test_score",
    ),
    path(
        "student/profile/test-scores/edit/<int:pk>",
        views.edit_test_score,
        name="edit_test_score",
    ),
]
