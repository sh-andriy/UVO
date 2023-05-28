from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project, Category

# Create your views here.


def home(request):

    context = {}
    if request.user.is_authenticated:

        context = {
            'home_page': True,
        }

    return render(request, 'home.html', context=context)


@login_required
def add_project(request):
    if request.method == "POST":
        name = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image-input")
        category_id = request.POST.get("select")
        reward = request.POST.get("coin")

        category = Category.objects.get(id=category_id)  # Retrieve the Category instance based on the selected ID
        project = Project(name=name, description=description, image=image, category=category, reward=reward)
        project.save()

        messages.success(request, "Project added successfully!")
        return redirect("proekts:home")

    categories = Category.objects.order_by('name')
    context = {
        'categories': categories,
    }
    return render(request, "proekts/add_proekt.html", context=context)


@login_required
def edit_project(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        # Process the submitted form data and update the project
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        # Update other project fields as needed
        project.save()

        messages.success(request, 'Project updated successfully.')
        return redirect('home')

    context = {
        'project': project,
    }
    return render(request, 'edit_project.html', context=context)


@login_required
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()

    messages.success(request, 'Project deleted successfully.')
    return redirect('home')

