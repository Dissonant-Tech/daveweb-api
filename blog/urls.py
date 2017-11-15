from django.conf.urls import url, include
from rest_framework import routers
from .views import ArticleViewSet, CategoryViewSet, CardViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'cards', CardViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
