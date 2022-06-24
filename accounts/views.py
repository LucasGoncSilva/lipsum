from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django import forms

from .models import User


# Create your views here.
class LogInForm(forms.Form):
    email = forms.CharField(
        label = '',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Email*',
                'class': 'py-2',
                'style': 'text-align: center;',
                'autofocus': 'autofocus'
            }
        )
    )
    password = forms.CharField(
        label = '',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Pass*',
                'class': 'mt-3 py-2',
                'style': 'text-align: center;'
            }
        )
    )
    # TODO: add MFA and captcha


# TODO: add registration page


def login_view(request: object) -> object:
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home:index'))

    elif request.method == 'POST':
        form = LogInForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email').strip()
            password = form.cleaned_data.get('password').strip()

            try:
                username = User.objects.get(email=email).username
            except User.DoesNotExist:
                messages.error(request, 'Email e/ou senha inválida.')
                return render(request, 'accounts/login.html', {
                    'form': form
                })
            
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home:index'))

            messages.error(request, 'Email e/ou senha inválida')
            return render(request, 'accounts/login.html', {
                'form': form
            })

    return render(request, 'accounts/login.html', {
        'form': LogInForm()
    })


@login_required
def logout_view(request: object) -> object:
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('accounts:login'))

    return render(request, 'accounts/logout.html')
