from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.book_list,name = 'book-list'),
    path('book/<int:id>/',views.book_detail,name = 'book-detail'),
    path('book/<int:id>/edit/', views.book_update, name='book-update'),
    path('book/<int:id>/delete/', views.book_delete, name='book-delete'),
    path('book/new/',views.book_create,name = 'book-create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)