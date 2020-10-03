from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from songarchiv.models import Song, Album, Song_Text

@login_required
def index(request):
    results = {}
    results['bh_count'] = Song.objects.all().count()
    results['song_text_count'] = Song_Text.objects.all().count()
    results['emptytext'] = Song_Text.objects.filter(text_text__exact='').count()
    results['emptychords'] = Song_Text.objects.filter(text_chords__exact='').count()
    results['emptychordpro'] = Song_Text.objects.filter(text_chordpro__exact='').count()
    results['emptynashville'] = Song_Text.objects.filter(text_nashville__exact='').count()
    results['emptystandard'] = Song_Text.objects.filter(text_standard_german__exact='').count()
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
    song_text = Song_Text.objects.filter(text_nashville__exact='').values('id', 'song_id')
    song_text.part = "Nashville"
    return render(request, 'dashboard/empty_text.html', {'song_text': song_text})


@login_required
def empty_standard(request):
    song_text = Song_Text.objects.filter(text_standard_german__exact='').values('id', 'song_id')
    song_text.part = "Standard German"
    return render(request, 'dashboard/empty_text.html', {'song_text': song_text})
