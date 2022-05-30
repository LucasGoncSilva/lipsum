from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from .models import Card, LoginCredential, SecurityNote


# Create your views here.
def index(request):
    return render(request, 'secret/index.html')


# Credentials views
class CredentialListView(ListView):
    model = LoginCredential
    template_name = 'secret/list_view.html'

    def get_context_data(self,**kwargs):
        context = super(CredentialListView, self).get_context_data(**kwargs)
        context['model_name'] = 'Credenciais'
        return context


class CredentialDetailView(DetailView):
    model = LoginCredential
    template_name = 'secret/Credential/detail_view.html'


class CredentialCreateView(CreateView):
    model = LoginCredential
    template_name = 'secret/Credential/create_view.html'


class CredentialUpdateView(UpdateView):
    model = LoginCredential
    template_name = 'secret/Credential/update_view.html'


class CredentialDeleteView(DeleteView):
    model = LoginCredential
    template_name = 'secret/Credential/delete_view.html'


# Cards views
class CardListView(ListView):
    model = Card
    template_name = 'secret/list_view.html'

    def get_context_data(self,**kwargs):
        context = super(CardListView, self).get_context_data(**kwargs)
        context['model_name'] = 'Cartões'
        return context


class CardDetailView(DetailView):
    model = Card
    template_name = 'secret/Card/detail_view.html'


class CardCreateView(CreateView):
    model = Card
    template_name = 'secret/Card/create_view.html'


class CardUpdateView(UpdateView):
    model = Card
    template_name = 'secret/Card/update_view.html'


class CardDeleteView(DeleteView):
    model = Card
    template_name = 'secret/Card/delete_view.html'


# Security Notes views
class NoteListView(ListView):
    model = SecurityNote
    template_name = 'secret/list_view.html'

    def get_context_data(self,**kwargs):
        context = super(NoteListView, self).get_context_data(**kwargs)
        context['model_name'] = 'Anotações'
        return context


class NoteDetailView(DetailView):
    model = SecurityNote
    template_name = 'secret/Note/detail_view.html'


class NoteCreateView(CreateView):
    model = SecurityNote
    template_name = 'secret/Note/create_view.html'


class NoteUpdateView(UpdateView):
    model = SecurityNote
    template_name = 'secret/Note/update_view.html'


class NoteDeleteView(DeleteView):
    model = SecurityNote
    template_name = 'secret/Note/delete_view.html'