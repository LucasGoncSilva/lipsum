from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from .models import Card, LoginCredential, SecurityNote


# Create your views here.
def index(request):
    return render(request, 'secret/index.html')


# Credentials views
def credential_list_view(request) -> object:
    return render(request, 'secret/list_view.html', {
        'object_list': request.user.credentials.all(),
    })


def credential_detail_view(request: object, slug: str) -> object:
    try:
        credential: object = LoginCredential.objects.get(owner=request.user, slug=slug)
    except:
        raise Http404('The QuerySet for get method returned a number different of one object')

    return render(request, 'secret/Credential/detail_view.html', {
        'object': credential
    })


class CredentialCreateView(CreateView):
    model = LoginCredential
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(CredentialCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Adição'
        context['model'] = 'Credencial'
        return context


class CredentialUpdateView(UpdateView):
    model = LoginCredential
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(CredentialUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Edição'
        context['model'] = 'Credencial'
        return context


class CredentialDeleteView(DeleteView):
    model = LoginCredential
    template_name = 'secret/delete_view.html'
    success_url = '/secret/credentials'

    def get_context_data(self,**kwargs):
        context = super(CredentialDeleteView, self).get_context_data(**kwargs)
        context['action'] = 'Exclusão'
        context['model'] = 'Credencial'
        return context


# Cards views
def card_list_view(request) -> object:
    return render(request, 'secret/list_view.html', {
        'object_list': request.user.cards.all(),
    })


class CardDetailView(DetailView):
    model = Card
    template_name = 'secret/Card/detail_view.html'


class CardCreateView(CreateView):
    model = Card
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(CardCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Adição'
        context['model'] = 'Cartão'
        return context


class CardUpdateView(UpdateView):
    model = Card
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(CardUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Edição'
        context['model'] = 'Cartão'
        return context


class CardDeleteView(DeleteView):
    model = Card
    template_name = 'secret/delete_view.html'
    success_url = '/secret/credentials'

    def get_context_data(self,**kwargs):
        context = super(CardDeleteView, self).get_context_data(**kwargs)
        context['action'] = 'Exclusão'
        context['model'] = 'Cartão'
        return context


# Security Notes views
def note_list_view(request) -> object:
    return render(request, 'secret/list_view.html', {
        'object_list': request.user.notes.all(),
    })


class NoteDetailView(DetailView):
    model = SecurityNote
    template_name = 'secret/Note/detail_view.html'


class NoteCreateView(CreateView):
    model = SecurityNote
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(NoteCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Adição'
        context['model'] = 'Anotação'
        return context


class NoteUpdateView(UpdateView):
    model = SecurityNote
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(NoteUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Edição'
        context['model'] = 'Anotação'
        return context


class NoteDeleteView(DeleteView):
    model = SecurityNote
    template_name = 'secret/delete_view.html'
    success_url = '/secret/credentials'

    def get_context_data(self,**kwargs):
        context = super(NoteDeleteView, self).get_context_data(**kwargs)
        context['action'] = 'Exclusão'
        context['model'] = 'Anotação'
        return context