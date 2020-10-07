from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('emptytext/', views.empty_text, name='empty_text'),
    path('emptychords/', views.empty_chords, name='empty_chords'),
    path('emptychordpro/', views.empty_chordpro, name='empty_chordpro'),
    path('emptynashville/', views.empty_nashville, name='empty_nashville'),
    path('emptystandard/', views.empty_standard, name='empty_standard'),
    path('chordpro/', views.ChordproListView.as_view(), name='chordpro'),
    path('chords/', views.ChordsListView.as_view(), name='chords'),
    path('nashville/', views.NashvilleListView.as_view(), name='nashville'),
    path('standard/', views.StandardListView.as_view(), name='standard'),
]