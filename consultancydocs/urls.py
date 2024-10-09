from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("error/", views.error, name="error"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/manage/students/", views.manage_students, name="manage_students"),
    path(
        "dashboard/manage/applications/",
        views.manage_applications,
        name="manage_applications",
    ),
    path("dashboard/plans/", views.plans, name="plans"),
    path("dashboard/settings/", views.settings, name="settings"),
]