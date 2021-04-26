import logging
import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from .forms import IndexForm, SongForm, SearchAlbumForm, AlbumForm, SongTextForm
from .models import Song, Album, Song_Text, Album_song, Content_text

BASE_DIR = settings.BASE_DIR

logger = logging.getLogger(__name__)


def index(request):
    form = IndexForm()
    song_count = Song.objects.all().count()
    form.song_count = song_count
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};Index-site")
    return render(request, 'songarchiv/index.html', {'form': form})


def impressum(request):
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};Impressum")
    content = Content_text.objects.get(content_kurz='Impressum')
    return render(request, 'songarchiv/impressum.html', {'content': content})


def datenschutz(request):
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};Datenschutz")
    content = Content_text.objects.get(content_kurz='Datenschutz')
    return render(request, 'songarchiv/datenschutz.html', {'content': content})


def uebers_songarchiv(request):
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};Übers Songarchiv")
    content = Content_text.objects.get(content_kurz='oevver_dat_songarchiv')
    return render(request, 'songarchiv/uebers_songarchiv.html', {'content': content})

def cd_song_list(request, id):
    Album_songs = Album_song.objects.filter(album_id=id).order_by('position')
    for song in Album_songs:
        song.text = Song_Text.objects.get(song_id=song.song.id)
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};CD_Song_List")
    return render(request, 'songarchiv/cd_song_list.html', {'Album_songs': Album_songs})

@login_required
def add_song(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song_item = form.save(commit=False)
            song_item.save()
            logger.info(f"User-ID: {request.user.id:>2};add_song;{str(song_item.id)};song created")
            return redirect('/songarchiv/song/' + str(song_item.id) + '/')
            #return redirect(song.get_abolute_url(song_item))
    else:
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};add_song;;get-call")
        form = SongForm()
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};add_song;;SongForm called")
    return render(request, 'songarchiv/song_form.html', {'form': form})


def search_song(request):
    if request.method == "POST":
        title = request.POST['title']
        title = title.strip()
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};search_song;{title};POST-call with title")
        if title != '':
            song_list = Song.objects.filter(song_title__icontains=title, song_activ=True).order_by('song_title')
            if len(song_list) == 1:
                logger.info(f"{request.META.get('HTTP_X_REAL_IP')};search_song;{str(song_list[0].slug)};song with id called")
                return redirect('/songarchiv/song/' + str(song_list[0].slug) + '/')
            elif len(song_list) > 1:
                logger.info(f"{request.META.get('HTTP_X_REAL_IP')};search_song;{title};song_list called")
                return render(request, 'songarchiv/songs.html', {'song_list': song_list,
                                                                 'title': title,
                                                                 'method': 'contains'})
            else:
                form = IndexForm()
                form.info = "Leider unter dem Suchbegriff '" + title + "' nichts gefunden"
                logger.info(f"{request.META.get('HTTP_X_REAL_IP')};search_song;{title}; nothing found with title")
                return render(request, 'songarchiv/index.html', {'form': form})
        else:
            form = IndexForm()
            form.info = "Bitte einen Suchbegriff eingeben"
            logger.info(f"{request.META.get('HTTP_X_REAL_IP')};search_song;;no search-string given")
            return render(request, 'songarchiv/index.html', {'form': form})

    elif request.method == "GET":
        title = request.GET['title']
        order = request.GET.get('order', '')
        method = request.GET.get('method', 'startswith')

        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};search_song;Titel: {title}, order: {order}, method: {method};GET-call with title")


        if title == "all":
            if order == 'song_title':
                order = ['song_title', 'album']
            elif order == 'album':
                order = ['album__album_title', 'song_title']
            else:
                order = ['song_title']
            song_list = Song.objects.filter(song_activ=True).order_by(*order)
        else:
            if order == 'song_title':
                order = ['song_title', 'album']
            elif order == 'album':
                order = ['album__album_title', 'song_title']
            else:
                order = ['song_title']
            if method == "contains":
                song_list = Song.objects.filter(song_title__icontains=title, song_activ=True).order_by(*order)
            else:
                song_list = Song.objects.filter(song_title__istartswith=title, song_activ=True).order_by(*order)

        #assert False
        if len(song_list) == 1:
            logger.info(f"{request.META.get('HTTP_X_REAL_IP')};search_song;{str(song_list[0].slug)};GET-call song with id called")
            return redirect('/songarchiv/song/' + str(song_list[0].slug) + '/')
        elif len(song_list) > 1:
            logger.info(f"{request.META.get('HTTP_X_REAL_IP')};search_song;{title};GET-call song_list called")
            return render(request, 'songarchiv/songs.html', {'song_list': song_list,
                                                             'title': title,
                                                             'method': method})
        else:
            form = IndexForm
            logger.info(f"{request.META.get('HTTP_X_REAL_IP')};search_song;{title};nothing found with title")
            return render(request, 'songarchiv/index.html', {'form': form})
    else:
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};search_song;;no searchword given")
        form = IndexForm
        return render(request, 'songarchiv/index.html', {'form': form})


def autocomplete(request):
    if request.method =='GET':
        title = request.GET['term']
        title = title.strip()
        qs = Song.objects.filter(song_title__icontains=title, song_activ=True).order_by('song_title')
        titles = list()
        for title in qs:
            titles.append(title.song_title)
        return JsonResponse(titles, safe=False)
    form = IndexForm
    return render(request, 'songarchiv/index.html', {'form': form})


@login_required
def edit_song(request, id=None):
    item = get_object_or_404(Song, id=id)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            logger.info(f"{request.user.id:>2};edit_song;{str(item.id)}; song changed and saved")
            return redirect('/songarchiv/song/' + str(item.id) + '/')
    else:
        form = SongForm(request.POST or None, instance=item)
        form.id = item.id
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};edit_song;;call edit_song get-call")
        return render(request, 'songarchiv/song_form.html', {'form': form})


def song(request, slug):
    try:
        if slug.isnumeric():
            song_result = Song.objects.get(id=slug)
        else:
            song_result = Song.objects.get(slug=slug)

        id = song_result.id
        try:
            song_text_result = Song_Text.objects.get(song_id=id)
        except Song_Text.DoesNotExist:
            song_text_result = None
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};song;{str(id)};call song")
        return render(request, 'songarchiv/song.html', {'song': song_result, 'text': song_text_result})
    except ObjectDoesNotExist:
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};song;{str(slug)};call song Object with ID don't exist")
        return redirect('/songarchiv/')


class del_song(DeleteView):
    model = Song
    template_name = 'songarchiv/song_delete_confirm.html'
    context_object_name = 'song'
    success_url = reverse_lazy('songarchiv:del_song_done')


def song_delete_done(request):
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};song_delete_done")
    return render(request, 'songarchiv/song_delete_done.html')

# **************************************************************************************************

@login_required
def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album_item = form.save(commit=False)
            album_item.save()
            logger.info(f"{request.user.id:>2};add_album;{str(album_item.id)};album with id created")
            return redirect('/songarchiv/album/')
    else:
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};add_album;;with get-call")
        form = AlbumForm()
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};add_album;;AlbumForm called")
    return render(request, 'songarchiv/album_form.html', {'form': form})


#wird wahrscheinlich nicht mehr gebraucht
def search_album_start(request):
    form = SearchAlbumForm()
    return render(request, 'songarchiv/album_search.html', {'form': form})


#wird wahrscheinlich nicht mehr gebraucht
def search_album(request):
    if request.method == "POST":
        title = request.POST['album_title']
        album_list = Album.objects.filter(album_title__icontains=title)
        if len(album_list) == 1:
            logger.info(f"{request.META.get('HTTP_X_REAL_IP')};search_album;str(album_list[0].id);Suche nach album-ID")
            return redirect('/songarchiv/album/' + str(album_list[0].id) + '/')
        elif len(album_list) > 1:
            return render(request, 'songarchiv/albums.html', {'album_list': album_list})
        else:
            return render(request, 'songarchiv/album.html', {'album_list': album_list})
    else:
        return render(request, 'songarchiv/index.html')


@login_required
def edit_album(request, id=None):
    item = get_object_or_404(Album, id=id)
    form = AlbumForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        logger.info(f"{request.user.id:>2};edit_album;{str(item.id)};album changed and saved")
        return redirect('/songarchiv/')
    form.id = item.id
    form.change = True
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};edit_album;{str(form.id)};AlbumForm for id called")
    return render(request, 'songarchiv/album_form.html', {'form': form})


def album(request):
    try:
        album_result = Album.objects.filter(album_single__exact=1).order_by('-album_year')
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};album;;list of albums called")
        return render(request, 'songarchiv/album.html', {'album': album_result})
    except ObjectDoesNotExist:
        return redirect('/songarchiv/')


def single(request):
    try:
        album_result = Album.objects.filter(album_single__exact=2).order_by('-album_year')
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};single;;list of singles called")
        return render(request, 'songarchiv/single.html', {'album': album_result})
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
            logger.info(f"{request.user.id:>2};add_text;{str(text_item.id)};songtext  with id saved")
            return redirect('/songarchiv/')
    else:
        song_result = Song.objects.get(id=request.GET.get('id'))
        logger.info(f"{request.user.id:>2};add_text;{str(id)};SongtextForm for id called")
        form = SongTextForm(initial={'song': song_result})
    return render(request, 'songarchiv/text_form.html', {'form': form})


@login_required
def edit_text(request, id=None):
    item = get_object_or_404(Song_Text, id=id)
    form = SongTextForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        logger.info(f"{request.user.id:>2};edit_text;{str(item.id)};songtext with id changed and saved")
        return redirect('/songarchiv/text/' + str(item.song_id))
    form.id = item.id
    logger.info(f"{request.user.id:>2};edit_text;{str(form.id)};text_form for id called")
    return render(request, 'songarchiv/text_form.html', {'form': form})


def text(request, slug):
    try:
        if request.user_agent.is_mobile:
            user_agent = 'mobile'
        else:
            user_agent = 'non-mobile'

        if slug.isnumeric():
            text_result = Song_Text.objects.get(song_id=slug)
        else:
            text_result = Song_Text.objects.get(slug=slug)

        id = text_result.song_id

        #text_result = Song_Text.objects.get(song_id=id)
        song_result = Song.objects.get(id=id)
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};text;{str(slug)};songtext with id and UserAgent {user_agent} called")
        return render(request, 'songarchiv/text.html', {'text': text_result, 'song': song_result, 'user_agent': user_agent})
    except ObjectDoesNotExist:
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};text;;object does not exist")
        return redirect('/songarchiv/add/text/?id=' + id)

# **************************************************************************************************

def print_text(request):
    slug = request.GET.get('slug')
    result_text = Song_Text.objects.get(slug=request.GET.get('slug'))
    result_song = Song.objects.get(id=result_text.song_id)

    filename = result_song.song_artist.replace(" ", "_") + "_" +  result_song.song_title.replace(" ", "_") + "_text.pdf"

    html_string = render_to_string('pdf_templates/print_text.html', {'result_text': result_text,
                                                                     'result_song': result_song})

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf(stylesheets=[CSS(settings.STATIC_ROOT + '/songarchiv/print_song.css')])
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + filename
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};print_text;{str(slug)};songtext with id as pdf created")

    return response


def print_chordpro(request):
    slug = request.GET.get('slug')
    result_text = Song_Text.objects.get(slug=request.GET.get('slug'))
    result_song = Song.objects.get(id=result_text.song_id)

    filename = result_song.song_artist.replace(" ", "_") + "_" +  result_song.song_title.replace(" ", "_") + "_chordpro.pdf"

    html_string = render_to_string('pdf_templates/print_chordpro.html', {'result_text': result_text, 'result_song': result_song})

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf(stylesheets=[CSS(settings.STATIC_ROOT + '/songarchiv/print_song.css')])
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + filename
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};print_chordpro;{str(slug)};songtext with id as pdf created")

    return response


def print_chords(request):
    slug = request.GET.get('slug')
    result_text = Song_Text.objects.get(slug=request.GET.get('slug'))
    result_song = Song.objects.get(id=result_text.song_id)

    filename = result_song.song_artist.replace(" ", "_") + "_" +  result_song.song_title.replace(" ", "_") + "_chords.pdf"
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + filename

    html_string = render_to_string('pdf_templates/print_chords.html', {'result_text': result_text,
                                                                       'result_song': result_song})
    font_config = FontConfiguration()

    HTML(string=html_string).write_pdf(response,
                                       font_config=font_config,
                                       stylesheets=[CSS(settings.STATIC_ROOT + '/songarchiv/print_song.css')])

    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};print_chords;{str(slug)};songtext with id as pdf created")

    return response


def print_nashville(request):
    slug = request.GET.get('slug')
    result_text = Song_Text.objects.get(slug=request.GET.get('slug'))
    #result_text = Song_Text.objects.get(id=request.GET.get('id'))
    result_song = Song.objects.get(id=result_text.song_id)

    filename = result_song.song_artist.replace(" ", "_") + "_" +  result_song.song_title.replace(" ", "_") + "_nashville.pdf"

    html_string = render_to_string('pdf_templates/print_nashville.html', {'result_text': result_text, 'result_song': result_song})

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf(stylesheets=[CSS(settings.STATIC_ROOT + '/songarchiv/print_song.css')])
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + filename
    logger.info(f"{request.META.get('HTTP_X_REAL_IP')};print_nashville;{str(slug)};songtext with id as pdf created")

    return response


# **************************************************************************************************

def videostaendchen(request):
    tag_list = []
    tag_dict = dict()
    song_list = Song.objects.all()

    for song in song_list:
        if song.song_tag:
            tag_split = song.song_tag.split()
            for tag in tag_split:
                tag_list.append(tag)

    tag_list.sort()

    for e in tag_list:
        tag_dict[e] = tag_list.count(e)

    #print(tag_list)
    #print(tag_dict)
    #tag_list = list(dict.fromkeys(tag_list))
    #tag_list.sort()

    return render(request, 'songarchiv/videostaendchen.html', {'tag_dict': tag_dict})

def staendchenlist(request):
    if request.method == "GET":
        song_list = Song.objects.filter(song_tag__contains=request.GET.get('tag'))

        return render(request, 'songarchiv/videostaendchenliste.html', {'song_list': song_list, 'kategorie': request.GET.get('tag')})
    else:
        form = IndexForm()
        song_count = Song.objects.all().count()
        form.song_count = song_count
        logger.info(f"{request.META.get('HTTP_X_REAL_IP')};Index-site")
        return render(request, 'songarchiv/index.html', {'form': form})

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
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'file',
            'filename': BASE_DIR + '/songarchiv.log',
            'maxBytes': 1024*1024*1,
            'backupCount': 10,
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
        'songarchiv': {
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
