from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("error/", views.error, name="error"),
    path("consultancy/dashboard/", views.dashboard, name="dashboard"),
    path(
        "consultancy/dashboard/manage/students/",
        views.manage_students,
        name="manage_students",
    ),
    path(
        "consultancy/dashboard/student/<int:pk>/",
        views.student_detail,
        name="student_detail",
    ),
    path(
        "consultancy/dashboard/student/<int:pk>/application/",
        views.student_application,
        name="admin_student_application",
    ),
    path(
        "consultancy/dashboard/student/<int:pk>/documents/",
        views.student_documents,
        name="admin_student_documents",
    ),
    path(
        "dashboard/manage/applications/",
        views.manage_applications,
        name="manage_applications",
    ),
    path("consultancy/dashboard/plans/", views.plans, name="plans"),
    path("consultancy/dashboard/settings/", views.settings, name="settings"),
]
