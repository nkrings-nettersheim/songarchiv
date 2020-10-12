from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('bhcount/', views.BHCountListView.as_view(), name='bhcount'),
    path('bhtextcount/', views.BHTextCountListView.as_view(), name='bhtextcount'),
    path('text/', views.TextListView.as_view(), name='text'),
    path('chordpro/', views.ChordproListView.as_view(), name='chordpro'),
    path('chords/', views.ChordsListView.as_view(), name='chords'),
    path('nashville/', views.NashvilleListView.as_view(), name='nashville'),
    path('standard/', views.StandardListView.as_view(), name='standard'),
    path('publisher/', views.PublisherListView.as_view(), name='publisher'),
    path('producer/', views.ProducerListView.as_view(), name='producer'),
]