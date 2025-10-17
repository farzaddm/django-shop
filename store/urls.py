from django.urls import path
from store.views import *

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetailList.as_view()),
    path('collections/', CollectionList.as_view()),
    path('collections/<int:id>/', CollectionDetailList.as_view(), name="collection-detail"),
]