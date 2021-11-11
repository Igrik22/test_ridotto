from django.urls import path
from core import views

urlpatterns = [
    path('', views.GeneralShopInfoView.as_view(), name='home'),
    path('shop/', views.ShopInfoCreateView.as_view(), name='create form'),
    path('customer/', views.CustomerCreateView.as_view(), name='create customer')
]