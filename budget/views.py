from django.shortcuts import render, get_object_or_404
from .models import Project, Category
from django.views.generic import CreateView
from django.utils.text import slugify
from django.http import HttpResponseRedirect

# Create your views here.

def project_list(request):
    return render(request, 'budget/project-list.html')

def project_details(request, project_slug):
        project = get_object_or_404(Project, slug=project_slug)
        category_list = Category.objects.filter(project=project)
        #pass variable to html template here
        return render(request, 'budget/project-details.html',
                      {'project': project, 'expense_list': project.expenses.all(), 'category_list': category_list})

class ProjectCreateView(CreateView):
      model = Project
      template_name = 'budget/add-project.html'
      fields = ('name', 'budget')

      def form_valid(self, form):
            self.object = form.save(commit=False)
            self.object.save()

            categories = self.request.POST['categoriesString'].split(',')
            for category in categories:
                  Category.objects.create(
                        project = Project.objects.get(id=self.object.id),
                        name=category
                  ).save()

            return HttpResponseRedirect(self.get_success_url())
      
      def get_success_url(self):
            return slugify(self.request.POST['name'])

    