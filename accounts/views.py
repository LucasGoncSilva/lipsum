from time import sleep
from random import uniform

from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django import forms
from captcha.fields import CaptchaField

from .models import User


# Create your views here.
class RegisterForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=50,
        required=True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Username (nome de usuário)*',
                'class': 'py-2',
                'style': 'text-align: center;',
                'autofocus': 'autofocus'
            }
        ),
        help_text='50 caracteres ou menos. Letras, números e @/./+/-/_ apenas.',
    )
    first_name = forms.CharField(
        label='',
        max_length=32,
        required=True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Nome*',
                'class': 'py-2',
                'style': 'text-align: center;',
            }
        ),
    )
    last_name = forms.CharField(
        label='',
        max_length=150,
        required=True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Sobrenome*',
                'class': 'py-2',
                'style': 'text-align: center;',
            }
        ),
    )
    email = forms.EmailField(
        label='',
        required=True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Email*',
                'class': 'mt-3 py-2',
                'style': 'text-align: center;'
            }
        )
    )
    password = forms.CharField(
        label = '',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Senha*',
                'class': 'mt-3 py-2',
                'style': 'text-align: center;'
            }
        )
    )
    password2 = forms.CharField(
        label = '',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Confirmação de senha*',
                'class': 'mt-3 mb-5 py-2',
                'style': 'text-align: center;'
            }
        )
    )
    captcha = CaptchaField()


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


def register_view(request: object) -> object:
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')

            if password and password2 and password == password2:
                username = form.cleaned_data.get('username')

                if not User.objects.filter(username=username).exists():
                    first_name = form.cleaned_data.get('first_name')
                    last_name = form.cleaned_data.get('last_name')
                    email = form.cleaned_data.get('email')

                    User.objects.create_user(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password
                    )

                    return HttpResponseRedirect(reverse('accounts:login'))

                messages.error(request, 'Username indisponível')
                return render(request, 'accounts/register.html', {'form': form})

            messages.error(request, 'Senhas não compatíveis')
            return render(request, 'accounts/register.html', {'form': form})

        return render(request, 'accounts/register.html', {'form': form})

    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


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
                sleep(uniform(.3, .53))
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
