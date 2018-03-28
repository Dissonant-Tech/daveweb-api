from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import (Article, Category,
                     ArticleCard, BannerCard, QuoteCard, ImageCard)


@admin.register(Article)
class ArticleAdmin(MarkdownxModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleCard)
class ArticleCardAdmin(admin.ModelAdmin):
    pass


@admin.register(BannerCard)
class BannerCardAdmin(admin.ModelAdmin):
    pass


@admin.register(QuoteCard)
class QuoteCardAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageCard)
class ImageCardAdmin(admin.ModelAdmin):
    pass
