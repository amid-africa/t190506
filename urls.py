from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.CreateProductView.as_view(), name='create_product'),
    path('pricelist/', views.CreatePricelistView.as_view(), name='create_pricelist'),
    path('pricelistproduct/<int:pk>/', views.PricelistProductView.as_view(), name='pricelist_add_product')
]
