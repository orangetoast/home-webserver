from django.urls import path
from projects import views

urlpatterns = [
    path("", views.index),
    path("<int:pk>/", views.single_project_page),
]
