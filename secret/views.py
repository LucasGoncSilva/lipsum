from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator


from .models import Card, LoginCredential, SecurityNote


# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    return render(request, 'secret/index.html')


# Credentials views
@login_required(login_url='/accounts/login')
def credential_list_view(request) -> object:
    return render(request, 'secret/list_view.html', {
        'object_list': request.user.credentials.all(),
        'model_name': 'Credenciais'
    })


@login_required(login_url='/accounts/login')
def credential_detail_view(request: object, slug: str) -> object:
    try:
        credential: object = LoginCredential.objects.get(owner=request.user, slug=slug)
    except:
        raise Http404('The QuerySet for get method returned a number different of one object')

    return render(request, 'secret/Credential/detail_view.html', {
        'object': credential
    })


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class CredentialCreateView(CreateView):
    model = LoginCredential
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(CredentialCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Adição'
        context['model'] = 'Credencial'
        return context


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class CredentialUpdateView(UpdateView):
    model = LoginCredential
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(CredentialUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Edição'
        context['model'] = 'Credencial'
        return context


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
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
@login_required(login_url='/accounts/login')
def card_list_view(request) -> object:
    return render(request, 'secret/list_view.html', {
        'object_list': request.user.cards.all(),
        'model_name': 'Cartões'
    })


@login_required(login_url='/accounts/login')
def card_detail_view(request: object, slug: str) -> object:
    try:
        card: object = Card.objects.get(owner=request.user, slug=slug)
    except:
        raise Http404('The QuerySet for get method returned a number different of one object')

    return render(request, 'secret/Card/detail_view.html', {
        'object': card
    })


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class CardCreateView(CreateView):
    model = Card
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(CardCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Adição'
        context['model'] = 'Cartão'
        return context


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class CardUpdateView(UpdateView):
    model = Card
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(CardUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Edição'
        context['model'] = 'Cartão'
        return context


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
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
@login_required(login_url='/accounts/login')
def note_list_view(request) -> object:
    return render(request, 'secret/list_view.html', {
        'object_list': request.user.notes.all(),
        'model_name': 'Anotações'
    })


@login_required(login_url='/accounts/login')
def note_detail_view(request: object, slug: str) -> object:
    try:
        note: object = SecurityNote.objects.get(owner=request.user, slug=slug)
    except:
        raise Http404('The QuerySet for get method returned a number different of one object')

    return render(request, 'secret/Note/detail_view.html', {
        'object': note
    })


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class NoteCreateView(CreateView):
    model = SecurityNote
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(NoteCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Adição'
        context['model'] = 'Anotação'
        return context


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class NoteUpdateView(UpdateView):
    model = SecurityNote
    template_name = 'secret/create_view.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super(NoteUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Edição'
        context['model'] = 'Anotação'
        return context


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class NoteDeleteView(DeleteView):
    model = SecurityNote
    template_name = 'secret/delete_view.html'
    success_url = '/secret/credentials'

    def get_context_data(self,**kwargs):
        context = super(NoteDeleteView, self).get_context_data(**kwargs)
        context['action'] = 'Exclusão'
        context['model'] = 'Anotação'
        return context
