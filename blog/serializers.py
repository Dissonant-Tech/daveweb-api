import markdown
from .models import (Article, Category,
                     ArticleCard, BannerCard, QuoteCard, ImageCard)
from rest_framework import serializers


class MarkdownField(serializers.CharField):
    def to_representation(self, obj):
        return markdown.markdown(obj,
                                 extensions=['markdown.extensions.extra',
                                             'markdown.extensions.codehilite'])


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)
    author = serializers.StringRelatedField(many=False)
    content = MarkdownField()

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCardSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='article.title')
    text = MarkdownField()

    class Meta:
        model = ArticleCard
        fields = '__all__'


class BannerCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerCard
        fields = '__all__'


class QuoteCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteCard
        fields = '__all__'


class ImageCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCard
        fields = '__all__'
