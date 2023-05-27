from django.urls import path
from . import views

urlpatterns = [
    path("",views.manga_home,name="manga_home"),
    path("create",views.create,name="manga_create"),
    path("create_genre",views.create_genre,name="genre_create"),
    path("create_author",views.create_author,name="author_create"),
    path("<int:pk>",views.MangaDetailView.as_view(),name="manga-detail"),
    path('<int:pk>/delete/', views.manga_delete, name='manga_delete'),
    path('<int:pk>/update/', views.MangaUpdateView.as_view(), name='manga_update'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),

]