from django.shortcuts import render

# Create your views here.


def merry_christmas(request):
    context = {

    }
    return render(request, 'app_merry_christmas/index.html', context)
