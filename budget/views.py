from django.shortcuts import render

# Create your views here.

def project_list(request):
    return render(request, 'budget/project-list.html')

def project_details(request, project_slug):
    # fetch the current project
        return render(request, 'budget/project-details.html')

