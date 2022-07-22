from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpRequest, HttpResponse

# from account.models import User

from .models import Card, LoginCredential, SecurityNote


# Create your views here.
@login_required(login_url='/conta/entrar')
def index(req: HttpRequest) -> HttpResponse:
    return render(req, 'secret/index.html')


# Credentials views
@login_required(login_url='/conta/entrar')
def credential_list_view(req: HttpRequest) -> HttpResponse:
    return render(req, 'secret/list_view.html', {
        'object_list': req.user.credentials.all(),
        'model_name': 'Credenciais'
    })


@login_required(login_url='/conta/entrar')
def credential_detail_view(req: HttpRequest, slug: str) -> HttpResponse:
    credential = get_object_or_404(
        LoginCredential,
        owner=req.user,
        slug=slug
    )

    return render(req, 'secret/Credential/detail_view.html', {
        'object': credential
    })


@method_decorator(login_required(login_url='/conta/entrar'), name='dispatch')
class CredentialCreateView(CreateView):
    model = LoginCredential
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CredentialCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Adição'
        context['model'] = 'Credencial'

        return context

    def post(self, req):
        if LoginCredential.objects.filter(owner=req.user, slug=req.POST.get('slug')).exists():
            messages.error(req, 'O serviço e apelido inseridos já foram utilizados juntos por você. Tente outro apelido')
            return super().get(req)

        return super().post(req)


@method_decorator(login_required(login_url='/conta/entrar'), name='dispatch')
class CredentialUpdateView(UpdateView):
    model = LoginCredential
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CredentialUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Edição'
        context['model'] = 'Credencial'

        return context

    def post(self, req, *args, **kwargs):
        if LoginCredential.objects.filter(owner=req.user, slug=req.POST.get('slug')).exists():
            messages.error(req, 'O serviço e apelido inseridos já foram utilizados juntos por você. Tente outro apelido')
            return super().get(req)

        return super().post(req, *args, **kwargs)


@method_decorator(login_required(login_url='/conta/entrar'), name='dispatch')
class CredentialDeleteView(DeleteView):
    model = LoginCredential
    template_name = 'secret/delete_view.html'
    success_url = '/segredos/credenciais'

    def get_context_data(self, **kwargs):
        context = super(CredentialDeleteView, self).get_context_data(**kwargs)
        context['action'] = 'Exclusão'
        context['model'] = 'Credencial'
        return context


# Cards views
@login_required(login_url='/conta/entrar')
def card_list_view(req) -> HttpResponse:
    return render(req, 'secret/list_view.html', {
        'object_list': req.user.cards.all(),
        'model_name': 'Cartões'
    })


@login_required(login_url='/conta/entrar')
def card_detail_view(req: HttpRequest, slug: str) -> HttpResponse:
    card = get_object_or_404(
        Card,
        owner=req.user,
        slug=slug
    )

    return render(req, 'secret/Card/detail_view.html', {
        'object': card
    })


@method_decorator(login_required(login_url='/conta/entrar'), name='dispatch')
class CardCreateView(CreateView):
    model = Card
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CardCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Adição'
        context['model'] = 'Cartão'

        return context

    def post(self, req):
        if Card.objects.filter(owner=req.user, slug=req.POST.get('slug')).exists():
            messages.error(req, 'O banco e apelido inseridos já foram utilizados juntos por você. Tente outro apelido')
            return super().get(req)

        return super().post(req)


@method_decorator(login_required(login_url='/conta/entrar'), name='dispatch')
class CardUpdateView(UpdateView):
    model = Card
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CardUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Edição'
        context['model'] = 'Cartão'

        return context

    def post(self, req, *args, **kwargs):
        if Card.objects.filter(owner=req.user, slug=req.POST.get('slug')).exists():
            messages.error(req, 'O banco e apelido inseridos já foram utilizados juntos por você. Tente outro apelido')
            return super().get(req)

        return super().post(req, *args, **kwargs)


@method_decorator(login_required(login_url='/conta/entrar'), name='dispatch')
class CardDeleteView(DeleteView):
    model = Card
    template_name = 'secret/delete_view.html'
    success_url = '/segredos/cartoes'

    def get_context_data(self, **kwargs):
        context = super(CardDeleteView, self).get_context_data(**kwargs)
        context['action'] = 'Exclusão'
        context['model'] = 'Cartão'
        return context


# Security Notes views
@login_required(login_url='/conta/entrar')
def note_list_view(req) -> HttpResponse:
    return render(req, 'secret/list_view.html', {
        'object_list': req.user.notes.all(),
        'model_name': 'Anotações'
    })


@login_required(login_url='/conta/entrar')
def note_detail_view(req: HttpRequest, slug: str) -> HttpResponse:
    note = get_object_or_404(
        SecurityNote,
        owner=req.user,
        slug=slug
    )

    return render(req, 'secret/Note/detail_view.html', {
        'object': note
    })


@method_decorator(login_required(login_url='/conta/entrar'), name='dispatch')
class NoteCreateView(CreateView):
    model = SecurityNote
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NoteCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Adição'
        context['model'] = 'Anotação'

        return context

    def post(self, req):
        if SecurityNote.objects.filter(owner=req.user, slug=req.POST.get('slug')).exists():
            messages.error(req, 'O título inserido já foi utilizado por você. Tente outro.')
            return super().get(req)

        return super().post(req)


@method_decorator(login_required(login_url='/conta/entrar'), name='dispatch')
class NoteUpdateView(UpdateView):
    model = SecurityNote
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NoteUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Edição'
        context['model'] = 'Anotação'

        return context

    def post(self, req, *args, **kwargs):
        if SecurityNote.objects.filter(owner=req.user, slug=req.POST.get('slug')).exists():
            messages.error(req, 'O banco e apelido inseridos já foram utilizados juntos por você. Tente outro apelido')
            return super().get(req)

        return super().post(req, *args, **kwargs)


@method_decorator(login_required(login_url='/conta/entrar'), name='dispatch')
class NoteDeleteView(DeleteView):
    model = SecurityNote
    template_name = 'secret/delete_view.html'
    success_url = '/segredos/anotacoes'

    def get_context_data(self, **kwargs):
        context = super(NoteDeleteView, self).get_context_data(**kwargs)
        context['action'] = 'Exclusão'
        context['model'] = 'Anotação'
        return context
