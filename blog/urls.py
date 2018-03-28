from django.conf.urls import url, include
from rest_framework import routers
from .views import (ArticleViewSet, CategoryViewSet, CardViewSet,
                    ArticleCardViewSet, BannerCardViewSet,
                    QuoteCardViewSet, ImageCardViewSet)

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'article-cards', ArticleCardViewSet)
router.register(r'banner-cards', BannerCardViewSet)
router.register(r'quote-cards', QuoteCardViewSet)
router.register(r'image-cards', ImageCardViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^cards/', CardViewSet.as_view())
]
