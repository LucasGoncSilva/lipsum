from django.urls import path

from . import views as v


app_name = 'secret'

urlpatterns = [
    path('', v.index, name='index'),
    # Credentials views
    path('credentials', v.CredentialListView.as_view(), name='credential_list_view'),
    path('credentials/new', v.CredentialCreateView.as_view(), name='credential_create_view'),
    path('credentials/<int:pk>', v.CredentialDetailView.as_view(), name='credential_detail_view'),
    path('credentials/<int:pk>/edit', v.CredentialUpdateView.as_view(), name='credential_update_view'),
    path('credentials/<int:pk>/delete', v.CredentialDeleteView.as_view(), name='credential_delete_view'),
    # Cards views
    path('cards', v.CardListView.as_view(), name='card_list_view'),
    path('cards/new', v.CardCreateView.as_view(), name='card_create_view'),
    path('cards/<int:pk>', v.CardDetailView.as_view(), name='card_detail_view'),
    path('cards/<int:pk>/edit', v.CardUpdateView.as_view(), name='card_update_view'),
    path('cards/<int:pk>/delete', v.CardDeleteView.as_view(), name='card_delete_view'),
    # Security Notes views
    path('notes', v.NoteListView.as_view(), name='note_list_view'),
    path('notes/new', v.NoteCreateView.as_view(), name='note_create_view'),
    path('notes/<int:pk>', v.NoteDetailView.as_view(), name='note_detail_view'),
    path('notes/<int:pk>/edit', v.NoteUpdateView.as_view(), name='note_update_view'),
    path('notes/<int:pk>/delete', v.NoteDeleteView.as_view(), name='note_delete_view'),
]