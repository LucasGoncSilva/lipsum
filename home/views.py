from django.shortcuts import render


# Create your views here.
def index(request: object) -> object:
    if request.user.is_authenticated:
        return render(request, 'home/index.html')

    return render(request, 'home/landing.html')