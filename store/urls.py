from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views import *

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('collections', CollectionViewSet)


urlpatterns = router.urls