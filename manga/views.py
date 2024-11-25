from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.forms import ModelMultipleChoiceField, ModelChoiceField
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from c_auth.forms import CommentForm, ScoreForm
from .forms import MangaForm, MangaFilterForm, GenreForm, AuthorForm
from .models import Manga, Genres, Author , Score , Comments



# Create your views here.

def manga_home(request):
    objects = Manga.objects.order_by('title')
    form = MangaFilterForm()
    if "filter" in request.GET:
        form = MangaFilterForm(request.GET)
        genres = request.GET.getlist('genres')
        for genre in genres:
            objects = objects.filter(genres__id__in=genre)


    return render(request, 'manga/index.html', {'form': form,"objects":objects})


@login_required()
def create(request):
    err = ""
    if request.method == "POST":
        form = MangaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            err = "Форма была неверной"

    form = MangaForm()
    data = {"form": form, "err": err}
    return render(request, 'manga/create.html', data)


@login_required()
def create_author(request):
    err = ""
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            err = "Форма была неверной"

    form = AuthorForm()
    data = {"form": form, "err": err}
    return render(request, 'manga/create_author.html', data)


@login_required()
def create_genre(request):
    err = ""
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            err = "Форма была неверной"

    form = GenreForm()
    data = {"form": form, "err": err}
    return render(request, 'manga/create_genre.html', data)


class MangaDetailView(DetailView):
    model = Manga
    template_name = 'manga/manga.html'
    context_object_name = 'manga'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if str(self.request.user) != "AnonymousUser":
            try:
                context['user_score'] = Score.objects.get(user=self.request.user, manga=self.get_object())
            except:
                context['user_score'] = 'None'
        else:
            context['user_score'] = 'None'
        context['user'] = self.request.user
        context['comment_form'] = CommentForm()
        context['score_form'] = ScoreForm()
        context['manga'] = self.object
        comments = self.object.comments.order_by('-created_at')
        paginator = Paginator(comments, 4)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['comments'] = page_obj
        context['score'] = self.object.display_score()
        context['genres'] = self.object.display_genres()
        return context

    def post(self, request, *args, **kwargs):
        if 'comment' in request.POST:
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.user = 1
                    comment.manga = self.get_object()
                    comment.save()
        if str(request.user) != "AnonymousUser":
            if 'user_score' in request.POST:
                form = ScoreForm(request.POST)
                if form.is_valid():
                    score = form.save(commit=False)
                    try:
                        user_score = Score.objects.get(user=request.user, manga=self.get_object())
                        user_score.score = score.score
                        user_score.save()
                    except Score.DoesNotExist:
                        score.user = request.user
                        score.manga = self.get_object()
                        score.save()
        return super().get(request, *args, **kwargs)


@login_required()
def manga_delete(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    manga.delete()
    return redirect('manga_home')


class MangaUpdateView(UpdateView):
    model = Manga
    author = ModelChoiceField(queryset=Author.objects.all(), empty_label=None, to_field_name="author"),
    genres = ModelMultipleChoiceField(queryset=Genres.objects.all())
    fields = ['title', 'full_title', 'image', 'description', 'author', 'genres']
    template_name = 'manga/manga_update_form.html'
    success_url = reverse_lazy('manga_home')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comments, id=comment_id, user=request.user)
    manga = comment.manga.id
    comment.delete()
    return redirect('manga-detail', pk=manga)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comments, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('manga-detail', pk=comment.manga.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'manga/edit_comment.html', {'form': form})
