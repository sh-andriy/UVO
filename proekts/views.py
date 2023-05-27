from django.shortcuts import render

# Create your views here.


def home(request):

    context = {}
    if request.user.is_authenticated:

        context = {
            'home_page': True,
        }

    return render(request, 'home.html', context=context)