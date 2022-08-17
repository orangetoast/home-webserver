from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all().order_by("-end_date")

    return render(
        request,
        "project/index.html",
        {
            "projects": projects
        }
    )


def single_project_page(request, pk):
    project = Project.objects.get(pk=pk)

    return render(
        request,
        "project/single_project_page.html",
        {
            "project": project
        }
    )
