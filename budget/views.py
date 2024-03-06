from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def project_list(request):
    return render(request, 'budget/project-list.html')

def project_details(request, project_slug):
        project = get_object_or_404(Project, slug=project_slug)
        return render(request, 'budget/project-details.html',
                      {'project': project, 'expense_list': project.expenses.all()})

