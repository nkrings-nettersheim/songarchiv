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

    song_tag = forms.CharField(required=False,
                                 max_length=500,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'autofocus': 'autofocus',
                                         'placeholder': 'Tags eingeben ...'
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

    song_spotify_iframe = forms.CharField(required=False,
                                   max_length=250,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Link zu Spotify ...'
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
                                          'placeholder': 'Link zu Amazon-Music ...'
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

    song_cover = forms.CharField(required=False,
                                  max_length=150,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Name der Cover-Datei ...'
                                      }
                                  )
                                  )

    song_youtube = forms.CharField(required=False,
                                  max_length=500,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Link zu Youtube ...'
                                      }
                                  )
                                  )

    song_youtube_2 = forms.CharField(required=False,
                                  max_length=500,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Link zu Youtube ...'
                                      }
                                  )
                                  )

    song_youtube_3 = forms.CharField(required=False,
                                  max_length=500,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Link zu Youtube ...'
                                      }
                                  )
                                  )

    song_amazon_sale = forms.CharField(required=False,
                                  max_length=250,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Link zum Amazon Shop ...'
                                      }
                                  )
                                  )

    song_background = forms.CharField(required=False,
                                      widget=forms.Textarea(
                                          attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Hintergrund zum Song ...'
                                          }
                                      )
                                      )
    song_activ = forms.CheckboxInput(
                            )


    album = forms.ModelChoiceField(required=False, queryset=Album.objects.all().order_by('album_title'))

    class Meta:
        model = Song
        fields = ['song_title',
                  'song_tag',
                  'song_artist',
                  'song_music',
                  'song_lyrics',
                  'song_year',
                  'song_publisher',
                  'song_producer',
                  'song_spotify_iframe',
                  'song_spotify',
                  'song_amazon',
                  'song_itunes',
                  'song_snippet',
                  'song_cover',
                  'song_youtube',
                  'song_youtube_2',
                  'song_youtube_3',
                  'song_amazon_sale',
                  'song_background',
                  'song_activ',
                  'album'
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


    album_cover = forms.CharField(required=False,
                                  max_length=250,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Album-Cover eingeben ...'
                                      }
                                  )
                                  )






    album_spotify = forms.CharField(required=False,
                                  max_length=500,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Album-Spotify eingeben ...'
                                      }
                                  )
                                  )


    album_amazon_selling = forms.CharField(required=False,
                                  max_length=1000,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Amazon Link zum Shop eingeben ...'
                                      }
                                  )
                                  )

    class Meta:
        model = Album
        fields = [
            'album_title',
            'album_year',
            'album_cover',
            'album_cover_image',
            'album_spotify',
            'album_amazon_selling',
            'album_single'
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
