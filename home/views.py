from django.shortcuts import render


# Create your views here.
def index(request: object) -> object:
    if request.user.is_authenticated:
        return render(request, 'home/index.html', {
        'credentials': request.user.credentials.all()[:4],
        'cards': request.user.cards.all()[:4],
        'notes': request.user.notes.all()[:4]
    })

    return render(request, 'home/landing.html')
