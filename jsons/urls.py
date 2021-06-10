from django.urls import path, include
from .views import *
urlpatterns = [
    path('',  GiftshopList, name='giftshop-list'),
    path('detail/<int:pk>/',  GiftshopDetail, name='giftshop-detail'),
    path('create/',  GiftshopCreate, name='giftshop-create'),
    # path('giftshop-update/<int:pk>/',  GiftshopUpdate, name='giftshop-update'),
    path('delete/<int:pk>/',  GiftshopDelete, name='giftshop-delete'),
    path('<int:pk>/citizens/<int:cid>/',  GiftshopUpdate, name='giftshop-update'),
]
