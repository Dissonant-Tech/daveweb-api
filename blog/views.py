from rest_framework import viewsets
from .models import Article, Category, Card
from .serializers import ArticleSerializer, CategorySerializer, CardSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows article categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
