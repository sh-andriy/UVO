from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    login,
    logout,
    authenticate,
    password_validation
)

from .models import User
# from .models import Balance


def sing_in(request):
    if request.user.is_authenticated:
        return redirect("proekts:home")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in as " + email)
            return redirect("proekts:home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request=request, template_name="accounts/login.html", context={"login_page": True})


def sing_up_volunteer(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['name']
        surname = request.POST['surname']
        phone_number = request.POST['phone']
        skills = request.POST['skills']

        if User.objects.filter(email=email).exists():
            messages.error(request, "The email is already in use.")
            return redirect("users:register_volunteer")

        try:
            password_validation.validate_password(password)
        except ValidationError as error_messages:
            messages.error(request, error_messages.messages[0])
            return redirect("users:register_volunteer")

        user = User.objects.create_user(
            email=email,
            password=password,
            name=first_name,
            surname=surname,
            phone_number=phone_number,
            skills=skills,
        )

        # balance = Balance(
        #     user=user
        # )
        # balance.save()

        login(request, user)

        messages.success(request, "Welcome, home :)")

        return redirect("proekts:home")

    return render(request, "accounts/register_volunteer.html", context={"login_page": True})


def sing_up_organiser(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['name']
        surname = request.POST['surname']
        phone_number = request.POST['phone']

        if User.objects.filter(email=email).exists():
            messages.error(request, "The email is already in use.")
            return redirect("user")

        try:
            password_validation.validate_password(password)
        except ValidationError as error_messages:
            messages.error(request, error_messages.messages[0])
            return redirect("users:register_volunteer")

        user = User.objects.create_user(
            email=email,
            password=password,
            name=first_name,
            surname=surname,
            phone_number=phone_number,
        )

        # balance = Balance(
        #     user=user
        # )
        # balance.save()

        login(request, user)

        messages.success(request, "Welcome, home :)")

        return redirect("proekts:home")

    return render(request, "accounts/register_organisator.html", context={"login_page": True})


# def update_user(request):
#     if request.user.is_authenticated:
#         user = request.user
#         if request.method == "POST":
#             if 'update-data' in request.POST:
#                 email = request.POST.get('email')
#                 update = False
#                 if email != user.email:
#                     if User.objects.filter(email=email).exists():
#                         messages.error(request, "Sorry email already in use, let's try another one")
#                         return redirect("accounts:update")
#                     user.email = email
#                     update = True
#
#                 if update:
#                     user.save()
#                     messages.success(request, "Your account has been updated successfully!")
#                 return redirect("accounts:update")
#
#             elif 'update-password' in request.POST:
#                 old_password = request.POST.get('old_password')
#                 new_password1 = request.POST.get('new_password1')
#                 new_password2 = request.POST.get('new_password2')
#                 if not user.check_password(old_password):
#                     messages.error(request, "Please enter your old password correctly..")
#                     return redirect("accounts:update")
#                 elif new_password1 != new_password2:
#                     messages.error(request, "The new passwords do not match..")
#                     return redirect("accounts:update")
#                 else:
#                     user.set_password(new_password1)
#                     user.save()
#                     messages.success(request, "Your password has been updated successfully")
#                     return redirect("quizzes:home")
#         else:
#             return render(request, "accounts/user_profile.html", context={'user': user, 'account_page': True})
#     else:
#         return redirect('quizzes:home')

@login_required
def profile(request):
    context = {
        'user_profile_page': True,
    }
    return render(request, 'accounts/user_profile.html', context=context)


@login_required
def sign_out(request):
    logout(request)
    return redirect("proekts:home")
