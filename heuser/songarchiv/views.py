import io
import os
import logging

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .forms import IndexForm, SongForm, SearchAlbumForm, AlbumForm, SongTextForm
from .models import Song, Album, Song_Text
from django.conf import settings

BASE_DIR = settings.BASE_DIR

logger = logging.getLogger(__name__)


def index(request):
    form = IndexForm()
    song_count = Song.objects.all().count()
    form.song_count = song_count
    return render(request, 'songarchiv/index.html', {'form': form})


def impressum(request):
    return render(request, 'songarchiv/impressum.html')


def datenschutz(request):
    return render(request, 'songarchiv/datenschutz.html')


@login_required
def add_song(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song_item = form.save(commit=False)
            song_item.save()
            #            logger.info('{:>2}'.format(request.user.id) + ' add_doctor: Arzt mit Namen: ' + str(
            #                doctor_item.doctor_name1) + ' angelegt')
            return redirect('/songarchiv/song/' + str(song_item.id) + '/')
    else:
        logger.info('add_song: Formular zur Bearbeitung/Erfassung der Song-Daten')
        form = SongForm()
    return render(request, 'songarchiv/song_form.html', {'form': form})


def search_song(request):
    if request.method == "POST":
        title = request.POST['title']
        logger.debug('search_song: POST Anfrage erhalten ' + title)
        if title != '':
            song_list = Song.objects.filter(song_title__icontains=title).order_by('song_title')
            if len(song_list) == 1:
                logger.info('search_song: Suche nach Song-ID: ' + str(song_list[0].id))
                return redirect('/songarchiv/song/' + str(song_list[0].id) + '/')
            elif len(song_list) > 1:
                return render(request, 'songarchiv/songs.html', {'song_list': song_list})
            else:
                form = IndexForm()
                form.info = "Leider unter dem Suchbegriff '" + title + "' nichts gefunden"
                return render(request, 'songarchiv/index.html', {'form': form})
        else:
            form = IndexForm()
            form.info = "Bitte einen Suchbegriff eingeben"
            return render(request, 'songarchiv/index.html', {'form': form})

    elif request.method == "GET":
        logger.debug('search_song: GET Anfrage erhalten')
        title = request.GET['title']
        logger.debug('search_song: GET Anfrage mit "' + title + '"')
        song_list = Song.objects.filter(song_title__istartswith=title).order_by('song_title')
        if len(song_list) == 1:
            logger.info('search_song: Suche nach Song-ID: ' + str(song_list[0].id))
            return redirect('/songarchiv/song/' + str(song_list[0].id) + '/')
        elif len(song_list) > 1:
            return render(request, 'songarchiv/songs.html', {'song_list': song_list})
        else:
            form = IndexForm
            return render(request, 'songarchiv/index.html', {'form': form})
    else:
        logger.debug('search_song: Keinen Suchbegriff eingegeben')
        form = IndexForm
        return render(request, 'songarchiv/index.html', {'form': form})


@login_required
def edit_song(request, id=None):
    # request.session.set_expiry(settings.SESSION_EXPIRE_SECONDS)
    item = get_object_or_404(Song, id=id)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            #assert False
            form.save()
            logger.info('{:>2}'.format(request.user.id) + ' edit_song: ' + str(item.id) + ' Daten werden gespeichert')
            return redirect('/songarchiv/song/' + str(item.id) + '/')
    else:
        form = SongForm(request.POST or None, instance=item)
        form.id = item.id
        return render(request, 'songarchiv/song_form.html', {'form': form})


def song(request, id=id):
    try:
        song_result = Song.objects.get(id=id)
        logger.debug('song: Song mit der ID: ' + id + ' aufgerufen')
        return render(request, 'songarchiv/song.html', {'song': song_result})
    except ObjectDoesNotExist:
        return redirect('/songarchiv/')


# **************************************************************************************************

@login_required
def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album_item = form.save(commit=False)
            album_item.save()
            #            logger.info('{:>2}'.format(request.user.id) + ' add_doctor: Arzt mit Namen: ' + str(
            #                doctor_item.doctor_name1) + ' angelegt')
            return redirect('/songarchiv/album/' + str(album_item.id) + '/')
    else:
        logger.info('add_album: Formular zur Bearbeitung/Erfassung der Song-Daten')
        form = AlbumForm()
    return render(request, 'songarchiv/album_form.html', {'form': form})


def search_album_start(request):
    # request.session.set_expiry(settings.SESSION_EXPIRE_SECONDS)
    logger.debug('Suchmaske Album geladen')
    form = SearchAlbumForm()
    return render(request, 'songarchiv/album_search.html', {'form': form})


def search_album(request):
    if request.method == "POST":
        title = request.POST['album_title']
        album_list = Album.objects.filter(album_title__icontains=title)
        if len(album_list) == 1:
            logger.info('search_album: Suche nach album-ID: ' + str(album_list[0].id))
            return redirect('/songarchiv/album/' + str(album_list[0].id) + '/')
        elif len(album_list) > 1:
            return render(request, 'songarchiv/albums.html', {'album_list': album_list})
        else:
            return render(request, 'songarchiv/album.html', {'album_list': album_list})
    else:
        logger.debug('search_album: Keinen Suchbegriff eingegeben')
        return render(request, 'songarchiv/index.html')


@login_required
def edit_album(request, id=None):
    # request.session.set_expiry(settings.SESSION_EXPIRE_SECONDS)
    item = get_object_or_404(Album, id=id)
    form = AlbumForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        # logger.info('{:>2}'.format(request.user.id) + ' edit_doctor: ' + str(item.id) + ' Daten werden gespeichert')
        return redirect('/songarchiv/album/' + str(item.id) + '/')
    # logger.debug('edit_doctor: Bearbeitungsformular aufgerufen ID: ' + id)
    form.id = item.id
    return render(request, 'songarchiv/album_form.html', {'form': form})


def album(request, id=id):
    try:
        album_result = Album.objects.get(id=id)
        logger.debug('album: album mit der ID: ' + id + ' aufgerufen')
        return render(request, 'songarchiv/album.html', {'album': album_result})
    except ObjectDoesNotExist:
        return redirect('/songarchiv/')


# **************************************************************************************************

@login_required
def add_text(request):
    if request.method == "POST":
        form = SongTextForm(request.POST)
        if form.is_valid():
            text_item = form.save(commit=False)
            text_item.save()
            return redirect('/songarchiv/')
    else:
        logger.info('add_text: Formular zur Bearbeitung/Erfassung der Song-Daten')
        song_result = Song.objects.get(id=request.GET.get('id'))
        form = SongTextForm(initial={'song': song_result})
    return render(request, 'songarchiv/text_form.html', {'form': form})


@login_required
def edit_text(request, id=None):
    item = get_object_or_404(Song_Text, id=id)
    form = SongTextForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/songarchiv/text/' + str(item.song_id))
    form.id = item.id
    return render(request, 'songarchiv/text_form.html', {'form': form})


def text(request, id=id):
    try:
        text_result = Song_Text.objects.get(song_id=id)
        song_result = Song.objects.get(id=id)
        logger.debug('text: text mit der ID: ' + id + ' aufgerufen')
        return render(request, 'songarchiv/text.html', {'text': text_result, 'song': song_result})
    except ObjectDoesNotExist:
        return redirect('/songarchiv/add/text/?id=' + id)


# **************************************************************************************************

LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-23s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': BASE_DIR + '/songarchiv.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
        'reports': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
        'django.security.*': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        }
    }
})
