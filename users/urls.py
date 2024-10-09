from django.urls import path
from . import views

urlpatterns = [
    path("auth/login/", views.login, name="login"),
    path("auth/register/", views.register, name="register"),
    path(
        "auth/register/student/<str:slug>/",
        views.student_register,
        name="student_register",
    ),
    path("auth/logout/", views.logout, name="logout"),
    path("consultancy/onboarding/<int:pk>/", views.onboarding, name="onboarding"),
]
