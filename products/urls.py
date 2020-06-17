from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products-index'),
    path('new', views.new, name='new-product'),
    path('<int:product_id>', views.new, name='products-edit'),
]