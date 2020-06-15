from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='expenses-index'),
    path('new', views.new, name='expenses-new'),
    path('<int:expense_id>', views.new, name='expenses-edit'),
]