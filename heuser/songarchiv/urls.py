from django.urls import path

from . import views
from .views import del_song

app_name = 'songarchiv'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/song/', views.add_song, name='add_song'),
    path('search/song/', views.search_song, name='search_song'),
    path('edit/song/<id>/', views.edit_song, name='edit_song'),
    path('song/<id>/', views.song, name='song'),
    path('del/song/<pk>', views.del_song.as_view(), name='del_song'),
    path('song_delete_done', views.song_delete_done, name='del_song_done'),
    path('autocomplete', views.autocomplete, name='autocomplete'),

    path('add/album/', views.add_album, name='add_album'),
    path('search/album/start', views.search_album_start, name='search_album_start'),
    path('search/album/', views.search_album, name='search_album'),
    path('edit/album/<id>/', views.edit_album, name='edit_album'),
    path('album/', views.album, name='album'),

    path('add/text/', views.add_text, name='add_text'),
    path('edit/text/<id>/', views.edit_text, name='edit_text'),
    path('text/<id>/', views.text, name='text'),
    path('print_text/', views.print_text, name='print_text'),
    path('print_chordpro/', views.print_chordpro, name='print_chordpro'),
    path('print_chords/', views.print_chords, name='print_chords'),
    path('print_nashville/', views.print_nashville, name='print_nashville'),

    path('impressum/', views.impressum, name='impressum'),
    path('datenschutz/', views.datenschutz, name='datenschutz'),
]