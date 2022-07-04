from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Attempt


# Create your views here.
def honeypot(req: HttpRequest, path: str=None) -> HttpResponse:
    if req.method == 'POST':
        x_forwarded_for = req.META.get('HTTP_X_FORWARDED_FOR')

        ip: str = x_forwarded_for.split(',')[0] if x_forwarded_for else req.META.get('REMOTE_ADDR')

        username: str = req.POST.get('username')
        password: str = req.POST.get('password')
        url: str = req.get_full_path().split('=')[1]

        Attempt.objects.create(IP=ip, username=username, password=password, url=url)

        return render(req, 'honeypot/loop.html', {'next': url})

    return render(req, 'honeypot/honeypot.html', {'next': req.path})
