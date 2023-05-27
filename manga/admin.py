from django.contrib import admin
from .models import Manga, Author, Genres, Comments, Score

# Register your models here.
admin.site.register(Manga)
admin.site.register(Author)
admin.site.register(Genres)
admin.site.register(Comments)
admin.site.register(Score)
