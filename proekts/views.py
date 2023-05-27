from django.shortcuts import render

# Create your views here.


def home(request):

    context = {}
    if request.user.is_authenticated:

        context = {
            'home_page': True,
        }

    return render(request, 'home.html', context=context)


def add_proekt(request):
    context = {
        'add_proekt_page': True,
    }
    return render(request, 'proekts/add_proekt.html', context=context)
