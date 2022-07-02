from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.forms import Form, CharField, TextInput, EmailField, PasswordInput
from captcha.fields import CaptchaField

from .models import User


# Create your views here.
class RegisterForm(Form):
    username: object = CharField(
        label='',
        max_length=50,
        required=True,
        widget = TextInput(
            attrs = {
                'placeholder': 'Username (nome de usuário)*',
                'class': 'py-2',
                'style': 'text-align: center;',
                'autofocus': 'autofocus'
            }
        ),
        help_text='50 caracteres ou menos. Letras, números e @/./+/-/_ apenas.',
    )
    first_name: object = CharField(
        label='',
        max_length=32,
        required=True,
        widget = TextInput(
            attrs = {
                'placeholder': 'Nome*',
                'class': 'py-2',
                'style': 'text-align: center;',
            }
        ),
    )
    last_name: object = CharField(
        label='',
        max_length=150,
        required=True,
        widget = TextInput(
            attrs = {
                'placeholder': 'Sobrenome*',
                'class': 'py-2',
                'style': 'text-align: center;',
            }
        ),
    )
    email: object = EmailField(
        label='',
        required=True,
        widget = TextInput(
            attrs = {
                'placeholder': 'Email*',
                'class': 'mt-3 py-2',
                'style': 'text-align: center;'
            }
        )
    )
    password: object = CharField(
        label = '',
        required = True,
        widget = PasswordInput(
            attrs = {
                'placeholder': 'Senha*',
                'class': 'mt-3 py-2',
                'style': 'text-align: center;'
            }
        )
    )
    password2: object = CharField(
        label = '',
        required = True,
        widget = PasswordInput(
            attrs = {
                'placeholder': 'Confirmação de senha*',
                'class': 'mt-3 mb-5 py-2',
                'style': 'text-align: center;'
            }
        )
    )
    captcha: object = CaptchaField()


class LogInForm(Form):
    username = CharField(
        label = '',
        required = True,
        widget = TextInput(
            attrs = {
                'placeholder': 'Username*',
                'class': 'py-2',
                'style': 'text-align: center;',
                'autofocus': 'autofocus'
            }
        )
    )
    password: object = CharField(
        label = '',
        required = True,
        widget = PasswordInput(
            attrs = {
                'placeholder': 'Pass*',
                'class': 'mt-3 py-2',
                'style': 'text-align: center;'
            }
        )
    )
    # TODO: add MFA


def register_view(req: HttpRequest) -> HttpResponse:
    if req.user.is_authenticated:
        return HttpResponseRedirect(reverse('home:index'))

    elif req.method == 'POST':
        form: Form = RegisterForm(req.POST)

        if form.is_valid():
            password: str = form.cleaned_data.get('password')
            password2: str = form.cleaned_data.get('password2')

            if not password or not password2 or password != password2:
                messages.error(req, 'Senhas não compatíveis')
                return render(req, 'accounts/register.html', {'form': form})

            username: str = form.cleaned_data.get('username')
            email: str = form.cleaned_data.get('email')

            if User.objects.filter(username=username).exists():
                messages.error(req, 'Username indisponível')
                return render(req, 'accounts/register.html', {'form': form})

            if User.objects.filter(email=email).exists():
                messages.error(req, 'E-mail indisponível')
                return render(req, 'accounts/register.html', {'form': form})

            first_name: str = form.cleaned_data.get('first_name')
            last_name: str = form.cleaned_data.get('last_name')

            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )

            return HttpResponseRedirect(reverse('accounts:login'))

        return render(req, 'accounts/register.html', {'form': form})

    form: Form = RegisterForm()
    return render(req, 'accounts/register.html', {'form': form})


def login_view(req: HttpRequest) -> HttpResponse:
    if req.user.is_authenticated:
        return HttpResponseRedirect(reverse('home:index'))

    elif req.method == 'POST':
        form: Form = LogInForm(req.POST)

        if form.is_valid():
            username: str = form.cleaned_data.get('username').strip()
            password: str = form.cleaned_data.get('password').strip()
            
            user: User = authenticate(username=username, password=password)

            if user is not None:
                login(req, user)
                return HttpResponseRedirect(reverse('home:index'))

            messages.error(req, 'Username e/ou senha inválida')
            return render(req, 'accounts/login.html', {
                'form': form
            })

        return render(req, 'accounts/login.html', {
            'form': form
        })

    return render(req, 'accounts/login.html', {
        'form': LogInForm()
    })


@login_required
def logout_view(req: HttpRequest) -> HttpResponseRedirect:
    if req.method == 'POST':
        logout(req)
        return HttpResponseRedirect(reverse('accounts:login'))

    return render(req, 'accounts/logout.html')
