from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Livro
from fuzzywuzzy import process 

# Create your views here.
class LivroListView(ListView):
    model = Livro
    template_name = 'livros/livro_lista.html'
    context_object_name = 'livros'
    paginate_by = 10

    def get_queryset(self):
        orderby = self.request.GET.get('orderby', 'titulo')
        query = self.request.GET.get('q')
        queryset = super().get_queryset()
        if query:
            titulos = queryset.values_list('titulo', flat=True)
            titulos_proximos = process.extract(query, titulos, limit=10)
            titulos_proximos_nomes = [titulo[0] for titulo in titulos_proximos if titulo[1] > 80]
            queryset = queryset.filter(titulo__in=titulos_proximos_nomes)
        return queryset.order_by(orderby)

class LivroDetailView(DetailView):
    model = Livro
    template_name = 'livros/livro_detalhe.html'
    context_object_name = 'livro'