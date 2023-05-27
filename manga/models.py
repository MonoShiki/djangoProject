from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Genres(models.Model):
    name = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name


class Author(models.Model):
    f_name = models.CharField("Имя", max_length=50)
    s_name = models.CharField("Фамилия", max_length=50)
    nickname = models.CharField("Псевдоним", max_length=250)

    def __str__(self):
        return self.nickname


class Type(models.Model):
    name = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField('Название', max_length=50)
    full_title = models.CharField("Полное название", max_length=250)
    image = models.ImageField("Изображение", upload_to='images/', default="/images/dnote.jpg")
    description = models.TextField("Описание")
    last_update = models.DateField('Дата последней загрузки', default=timezone.now)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, default='')
    genres = models.ManyToManyField(Genres)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True, default='')


    def display_genres(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return [genre.name for genre in self.genres.all()]

    def display_score(self):
        """
        Creates a string for the Score. This is required to display genre in Admin.
        """
        list_of_scores = [score.score for score in self.scores.all()]
        if len(list_of_scores):
            c_s = str(sum(list_of_scores) / len(list_of_scores))
            return c_s[:3]
        else:
            return '0'

    def get_num_score(self):
        return float(self.display_score())

    def __str__(self):
        return self.title



class Tags(models.Model):
    tag = models.CharField('Название', max_length=50)
    description = models.TextField("Описание")
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='tags', null=True)

    def __str__(self):
        return self.tag


class Character(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='characters', null=True)
    description = models.TextField("Описание")
    first_volume_date = models.DateField(blank=True, null=True)


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(default=1, null=False)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='scores', null=True)
    add_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.score)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='comments', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
