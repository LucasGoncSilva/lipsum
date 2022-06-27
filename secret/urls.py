from django.urls import path

from . import views as v


app_name = 'secret'

urlpatterns = [
    path('', v.index, name='index'),
    # Credentials views
    path('credenciais/', v.credential_list_view, name='credential_list_view'),
    path('credenciais/nova', v.CredentialCreateView.as_view(), name='credential_create_view'),
    path('credenciais/<slug:slug>', v.credential_detail_view, name='credential_detail_view'),
    path('credenciais/<slug:slug>/editar', v.CredentialUpdateView.as_view(), name='credential_update_view'),
    path('credenciais/<slug:slug>/deletar', v.CredentialDeleteView.as_view(), name='credential_delete_view'),
    # Cards views
    path('cartoes/', v.card_list_view, name='card_list_view'),
    path('cartoes/novo', v.CardCreateView.as_view(), name='card_create_view'),
    path('cartoes/<slug:slug>', v.card_detail_view, name='card_detail_view'),
    path('cartoes/<slug:slug>/editar', v.CardUpdateView.as_view(), name='card_update_view'),
    path('cartoes/<slug:slug>/deletar', v.CardDeleteView.as_view(), name='card_delete_view'),
    # Security Notes views
    path('anotacoes/', v.note_list_view, name='note_list_view'),
    path('anotacoes/nova', v.NoteCreateView.as_view(), name='note_create_view'),
    path('anotacoes/<slug:slug>', v.note_detail_view, name='note_detail_view'),
    path('anotacoes/<slug:slug>/editar', v.NoteUpdateView.as_view(), name='note_update_view'),
    path('anotacoes/<slug:slug>/deletar', v.NoteDeleteView.as_view(), name='note_delete_view'),
]
