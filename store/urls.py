from django.urls import path
from store.views import *

urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>/', product_detail),
    path('collections/', collection_list),
    path('collections/<int:id>/', collection_detail, name="collection-detail"),
]