from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item-list'),
    path('reorder/', views.reorder_items, name='reorder-items'),
]
