from rest_framework import viewsets
from drf_multiple_model.views import FlatMultipleModelAPIView
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from .models import (Article, Category,
                     ArticleCard, BannerCard, QuoteCard, ImageCard)
from .serializers import (ArticleSerializer, CategorySerializer,
                          ArticleCardSerializer, BannerCardSerializer,
                          QuoteCardSerializer, ImageCardSerializer)


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


class CardViewSet(FlatMultipleModelAPIView):
    """
    API endpoint that allows all types of cards to be viewed or edited.
    """
    pagination_class = MultipleModelLimitOffsetPagination
    add_model_type = True
    sorting_field = '-created_at'

    querylist = [
        {
            'queryset': ArticleCard.objects.all(),
            'serializer_class': ArticleCardSerializer
        },
        {
            'queryset': BannerCard.objects.all(),
            'serializer_class': BannerCardSerializer
        },
        {
            'queryset': QuoteCard.objects.all(),
            'serializer_class': QuoteCardSerializer
        },
        {
            'queryset': ImageCard.objects.all(),
            'serializer_class': ImageCardSerializer
        }
    ]


class ArticleCardViewSet(viewsets.ModelViewSet):
    queryset = ArticleCard.objects.all()
    serializer_class = ArticleCardSerializer
    ordering_fields = ('created_at')


class BannerCardViewSet(viewsets.ModelViewSet):
    queryset = BannerCard.objects.all()
    serializer_class = BannerCardSerializer
    ordering_fields = ('created_at')


class QuoteCardViewSet(viewsets.ModelViewSet):
    queryset = QuoteCard.objects.all()
    serializer_class = QuoteCardSerializer
    ordering_fields = ('created_at')


class ImageCardViewSet(viewsets.ModelViewSet):
    queryset = ImageCard.objects.all()
    serializer_class = ImageCardSerializer
    ordering_fields = ('created_at')
