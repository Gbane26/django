from rest_framework import viewsets
from rest_framework import filters

from .models import Categorie, SousCategorie, Article, Commentaire
from .serializers import CategorieSerializer, SousCategorieSerializer, ArticleSerializer, CommentaireSerializer


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class CategorieViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer


class SousCategorieViewSet(viewsets.ModelViewSet):
    queryset = SousCategorie.objects.all()
    serializer_class = SousCategorieSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer