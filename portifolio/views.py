from django.shortcuts import render
from .models import ProjectModel

def home(request):

    projects = ProjectModel.objects.all()

    return render(request, 'portifolio/home.html', {"projects":projects})


def projeto(request, pk):

    project = ProjectModel.objects.get(pk=pk)

    return render(request, 'portifolio/projeto.html', {"project":project})
