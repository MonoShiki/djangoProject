# Generated by Django 4.2.1 on 2023-05-27 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('s_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('nickname', models.CharField(max_length=250, verbose_name='Псевдоним')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('full_title', models.CharField(max_length=250, verbose_name='Полное название')),
                ('image', models.ImageField(default='/images/dnote.jpg', upload_to='images/', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('last_update', models.DateField(default=django.utils.timezone.now, verbose_name='Дата последней загрузки')),
                ('author', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='manga.author')),
                ('genres', models.ManyToManyField(to='manga.genres')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('manga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='manga.manga')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=1)),
                ('add_at', models.DateTimeField(auto_now_add=True)),
                ('manga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='manga.manga')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='manga',
            name='type',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='manga.type'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('manga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='manga.manga')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('description', models.TextField(verbose_name='Описание')),
                ('first_volume_date', models.DateField(blank=True, null=True)),
                ('manga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='manga.manga')),
            ],
        ),
    ]
