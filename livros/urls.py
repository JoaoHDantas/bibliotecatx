from django.urls import path
from . import views
from django.views.generic import ListView
from .views import LivroListView

urlpatterns = [
    path('', LivroListView.as_view(), name='livros'),
    path('<int:pk>/', views.LivroDetailView.as_view(), name='livro_detalhe'),
]