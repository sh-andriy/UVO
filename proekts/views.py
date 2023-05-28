from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project, Category, Balance

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        projects = Project.objects.all()  # Retrieve all projects
        context = {
            'home_page': True,
            'projects': projects,  # Pass the projects to the template context
        }
        return render(request, 'home.html', context=context)
    else:
        return render(request, 'home.html')



@login_required
def add_project(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image-input")
        category_id = request.POST.get("select")
        reward = request.POST.get("coin")

        category = Category.objects.get(id=category_id)  # Retrieve the Category instance based on the selected ID
        project = Project(name=name, description=description, image=image, category=category, reward=reward)
        project.save()

        # Add reward amount to user's balance
        user = request.user
        balance = Balance.objects.get(user=user)
        balance.amount += int(reward)
        balance.save()

        messages.success(request, "Project added successfully!")
        return redirect("proekts:home")

    categories = Category.objects.order_by('name')
    context = {
        'categories': categories,
    }
    return render(request, "proekts/add_proekt.html", context=context)


# @login_required
# def edit_project(request, project_id):
#     project = Project.objects.get(id=project_id)
#
#     if request.method == 'POST':
#         # Process the submitted form data and update the project
#         project.title = request.POST.get('title')
#         project.description = request.POST.get('description')
#         # Update other project fields as needed
#         project.save()
#
#         messages.success(request, 'Project updated successfully.')
#         return redirect('home')
#
#     context = {
#         'project': project,
#     }
#     return render(request, 'edit_project.html', context=context)
#
#
# @login_required
# def delete_project(request, project_id):
#     project = Project.objects.get(id=project_id)
#     project.delete()
#
#     messages.success(request, 'Project deleted successfully.')
#     return redirect('home')

@login_required
def apply_for_project(request, project_id):
    project = Project.objects.get(id=project_id)

    # Add the reward amount to the user's balance
    user = request.user
    balance = Balance.objects.get(user=user)
    balance.amount += project.reward
    balance.save()

    messages.success(request, f"You have successfully applied for the project '{project.name}'.")
    return redirect("proekts:home")

