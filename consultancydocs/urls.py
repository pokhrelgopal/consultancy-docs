from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("onboarding/<int:pk>/", views.onboarding, name="onboarding"),
]
