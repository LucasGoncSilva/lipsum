from django.shortcuts import render

from .models import Attempt


# Create your views here.
def honeypot(request: object, path: str=None) -> None:
    if request.method == 'POST':
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        username = request.POST.get('username')
        password = request.POST.get('password')
        url = request.get_full_path().split('=')[1]

        attempt = Attempt.objects.create(IP=ip, username=username, password=password, url=url)
        attempt.save()

        return render(request, 'honeypot/loop.html', {'next': url})

    return render(request, 'honeypot/honeypot.html', {'next': request.path})