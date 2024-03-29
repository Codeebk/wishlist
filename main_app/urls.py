from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('create/', views.ItemCreate.as_view(), name='items_create'),
#     path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
# ]

urlpatterns = [
  path('', views.home, name='home'),
  path('items/', views.items_index, name='index'),
  path('items/<int:item_id>/', views.items_detail, name='detail'),
  path('create/', views.ItemCreate.as_view(), name='items_create'),
  path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
]