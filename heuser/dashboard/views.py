from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from songarchiv.models import Song, Album, Song_Text

@login_required
def index(request):
    results = {}
    results['bhcount'] = Song.objects.all().count()
    results['bhtextcount'] = Song_Text.objects.all().count()
    results['publisher'] = Song.objects.filter(song_publisher__exact='').count()
    results['producer'] = Song.objects.filter(song_producer__exact='').count()
    results['text'] = Song_Text.objects.filter(text_text__exact='').count()
    results['chords'] = Song_Text.objects.filter(text_chords__exact='').count()
    results['chordpro'] = Song_Text.objects.filter(text_chordpro__exact='').count()
    results['nashville'] = Song_Text.objects.filter(~Q(text_chords__exact='')).filter(text_nashville__exact='').count()
    results['standard'] = Song_Text.objects.filter(text_standard_german__exact='').count()
    return render(request, 'index.html', {'results': results})


@login_required
def empty_text(request):
    song_text = Song_Text.objects.filter(text_text__exact='')
    song_text.part = "Text only"
    return render(request, 'dashboard/empty_text.html', {'song_text': song_text})


@login_required
def empty_chords(request):
    song_text = Song_Text.objects.filter(text_chords__exact='')
    song_text.part = "Chords"
    return render(request, 'dashboard/empty_text.html', {'song_text': song_text})


@login_required
def empty_chordpro(request):
    song_text = Song_Text.objects.filter(text_chordpro__exact='')
    song_text.part = "Chordpro"
    return render(request, 'dashboard/empty_text.html', {'song_text': song_text})


@login_required
def empty_nashville(request):
    song_text = Song_Text.objects.filter(~Q(text_chords__exact='')).filter(text_nashville__exact='').values('id', 'song_id')
    song_text.part = "Nashville"
    return render(request, 'dashboard/empty_text.html', {'song_text': song_text})


@login_required
def empty_standard(request):
    song_text = Song_Text.objects.filter(text_standard_german__exact='').values('id', 'song_id')
    song_text.part = "Standard German"
    return render(request, 'dashboard/empty_text.html', {'song_text': song_text})


class BHCountListView(LoginRequiredMixin, ListView):
    model = Song
    context_object_name = 'my_song_list'
    queryset = Song.objects.all()
    template_name = 'dashboard/song_list.html'


class BHTextCountListView(LoginRequiredMixin, ListView):
    model = Song_Text
    context_object_name = 'my_song_list'
    queryset = Song_Text.objects.all()
    template_name = 'dashboard/song_text_list.html'


class PublisherListView(LoginRequiredMixin, ListView):
    model = Song
    context_object_name = 'my_song_list'
    queryset = Song.objects.filter(song_publisher__exact='')
    template_name = 'dashboard/song_list.html'


class ProducerListView(LoginRequiredMixin, ListView):
    model = Song
    context_object_name = 'my_song_list'
    queryset = Song.objects.filter(song_producer__exact='')
    template_name = 'dashboard/song_list.html'


class TextListView(LoginRequiredMixin, ListView):
    model = Song_Text
    context_object_name = 'my_song_list'
    queryset = Song_Text.objects.filter(text_text__exact='')
    template_name = 'dashboard/song_text_list.html'


class ChordproListView(LoginRequiredMixin, ListView):
    model = Song_Text
    context_object_name = 'my_song_list'
    queryset = Song_Text.objects.filter(text_chordpro__exact='')
    template_name = 'dashboard/song_text_list.html'


class ChordsListView(LoginRequiredMixin, ListView):
    model = Song_Text
    context_object_name = 'my_song_list'
    queryset = Song_Text.objects.filter(text_chords__exact='')
    template_name = 'dashboard/song_text_list.html'


class NashvilleListView(LoginRequiredMixin, ListView):
    model = Song_Text
    context_object_name = 'my_song_list'
    queryset = Song_Text.objects.filter(~Q(text_chords__exact='')).filter(text_nashville__exact='')
    template_name = 'dashboard/song_text_list.html'


class StandardListView(LoginRequiredMixin, ListView):
    model = Song_Text
    context_object_name = 'my_song_list'
    queryset = Song_Text.objects.filter(text_standard_german__exact='')
    template_name = 'dashboard/song_text_list.html'
