from django.urls import path
from store.views import *

urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>/', product_detail),
    path('collections/<int:pk>/', collection_detail, name="collection-detail"),
]