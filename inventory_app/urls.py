from django.urls import path
from . import views


urlpatterns = [
    path('items/', views.items_list, name='items'),
    path('item/<int:pk>/', views.item, name='show_one_item'),
]