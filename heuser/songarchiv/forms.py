import datetime
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Song, Album, Song_Text


class IndexForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autofocus': 'autofocus',
            'placeholder': 'Titel eingeben ...'
        }
    ),
        required=False
    )


class SongForm(forms.ModelForm):
    song_title = forms.CharField(required=True,
                                 max_length=150,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'autofocus': 'autofocus',
                                         'placeholder': 'Songtitel eingeben ...'
                                     }
                                 )
                                 )

    song_artist = forms.CharField(required=True,
                                  max_length=150,
                                  initial='Björn Heuser',
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Künstler eingeben ...'
                                      }
                                  )
                                  )

    song_music = forms.CharField(required=False,
                                 max_length=150,
                                 initial='Björn Heuser',
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'placeholder': 'Wer hat die Musik geschrieben?'
                                     }
                                 )
                                 )

    song_lyrics = forms.CharField(required=False,
                                  max_length=150,
                                  initial='Björn Heuser',
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Wer hat den Text geschrieben?'
                                      }
                                  )
                                  )

    song_year = forms.DateField(required=True,
                                initial='1900-01-01',
                                widget=forms.DateInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Erscheinungsjahr ...'
                                    }
                                )
                                )

    song_publisher = forms.CharField(required=False,
                                     max_length=150,
                                     initial='HEUSERMUSIK, GMO Publishing',
                                     widget=forms.TextInput(
                                         attrs={
                                             'class': 'form-control',
                                             'placeholder': 'Verlag ...'
                                         }
                                     )
                                     )

    song_producer = forms.CharField(required=False,
                                    max_length=150,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Produzent ...'
                                        }
                                    )
                                    )

    song_spotify = forms.CharField(required=False,
                                   max_length=150,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Link zu Spotify ...'
                                       }
                                   )
                                   )

    song_amazon = forms.CharField(required=False,
                                  max_length=150,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Link zu Amazon ...'
                                      }
                                  )
                                  )

    song_itunes = forms.CharField(required=False,
                                  max_length=150,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Link zu iTunes ...'
                                      }
                                  )
                                  )
#    song_snippet = forms.FileField()
#    song_snippet = forms.CharField(required=False,
#                                  max_length=150,
#                                  widget=forms.TextInput(
#                                      attrs={
#                                          'class': 'form-control',
#                                          'placeholder': 'Name Snippet Datei ...'
#                                      }
#                                  )
#                                  )

    song_background = forms.CharField(required=False,
                                      widget=forms.Textarea(
                                          attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Hintergrund zum Song ...'
                                          }
                                      )
                                      )

    class Meta:
        model = Song
        fields = ['song_title',
                  'song_artist',
                  'song_music',
                  'song_lyrics',
                  'song_year',
                  'song_publisher',
                  'song_producer',
                  'song_spotify',
                  'song_amazon',
                  'song_itunes',
                  'song_snippet',
                  'song_background'
                  ]


class SearchAlbumForm(forms.Form):
    album_title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autofocus': 'autofocus',
            'placeholder': 'Teil des Album-Titel eingeben ...'
        }
    ),
        required=False
    )


class AlbumForm(forms.ModelForm):
    album_title = forms.CharField(required=True,
                                  max_length=250,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'autofocus': 'autofocus',
                                          'placeholder': 'Album-Titel eingeben ...'
                                      }
                                  )
                                  )

    album_year = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Erscheinungsjahr eingeben ...'
        }
    ),
        required=False
    )

    class Meta:
        model = Album
        fields = [
            'album_title',
            'album_year'
        ]


class SongTextForm(forms.ModelForm):
    text_text = forms.CharField(required=False,
                                widget=CKEditorWidget(config_name='text'))

    text_standard_german = forms.CharField(required=False,
                                  widget=CKEditorWidget(config_name='text'))

    text_chordpro = forms.CharField(required=False,
                                  widget=CKEditorWidget(config_name='text'))

    text_chords = forms.CharField(required=False,
                                  widget=CKEditorWidget(config_name='chords'))

    text_nashville = forms.CharField(required=False,
                                     widget=CKEditorWidget(config_name='chords'))

    class Meta:
        model = Song_Text
        fields = [
            'text_text',
            'text_standard_german',
            'text_chordpro',
            'text_chords',
            'text_nashville',
            'song'
        ]
