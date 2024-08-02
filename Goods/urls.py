from django.urls import path, include
from Goods import views

urlpatterns = [
    path('', views.main, name='index'),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
    path('cart/', include('Goods.user.urls')),
    path('wish/', include('Goods.wish.urls')),
    path('banner/', include('Goods.banner.urls')),
    path('info', views.createInfo, name='info')
]