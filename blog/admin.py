from django.contrib import admin
from .models import Article, Category, Card


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass
