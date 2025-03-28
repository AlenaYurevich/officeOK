from django.urls import path
from . import views


urlpatterns = [
    # Главная страница товаров
    path('', views.product_list, name='product_list'),

    # Список товаров по категории (слаг)
    path('<slug:category_slug>/',
         views.product_list,
         name='product_list_by_category'),

    # Детальная страница товара (id + слаг)
    path('<int:pk>/<slug:slug>/',
         views.product_detail,
         name='product_detail'),
]
