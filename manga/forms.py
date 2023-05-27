from django.forms import ModelForm, TextInput, FileInput, Textarea, ModelChoiceField, ModelMultipleChoiceField, Form, \
    CheckboxSelectMultiple, HiddenInput, IntegerField

from .models import Manga, Author, Genres


class MangaFilterForm(Form):
    genres = ModelMultipleChoiceField(queryset=Genres.objects.all(), widget=CheckboxSelectMultiple, required=False)


class MangaForm(ModelForm):
    class Meta:
        model = Manga
        author = ModelChoiceField(queryset=Author.objects.all(), empty_label=None, to_field_name="author"),
        genres = ModelMultipleChoiceField(queryset=Genres.objects.all(), widget=CheckboxSelectMultiple, required=False, )
        fields = ['title', 'full_title', 'image', 'description', 'author', 'genres']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Название манги'
            }),
            'full_title': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Полное название манги'
            }),
            'image': FileInput(attrs={
                'class': "form-control",
                'placeholder': 'Картинка манги'
            }),
            'description': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Описание манги'
            }),
        }


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('f_name', 's_name', 'nickname')

    widgets = {
        'f_name': TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Имя'
        }),
        's_name': TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Фамилия'
        }),
        'nickname': TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Никнейм'
        }),
    }


class GenreForm(ModelForm):
    class Meta:
        model = Genres
        fields = ('name', 'description')
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Название'
            }),
            'description': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Описание'
            }),
        }


class CommentDeleteForm(Form):
    comment_id = IntegerField(widget=HiddenInput())
