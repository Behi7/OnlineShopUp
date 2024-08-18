from . import views
from django.urls import path

urlpatterns = [
    path('product', views.ProductListViews.as_view()),
    path('product/<int:pk>', views.ProducDetailViews.as_view()),
    path('category', views.CategoryListViews.as_view()),
    path('category/<int:pk>/', views.CategoryDetailViews.as_view()),
    path('log-in', views.log_in),
    path('register', views.UserCreateView.as_view()),
    path('cart', views.cartGet),
    path('add-product', views.add_to_cart),
    path('remowe-product', views.delete_to_cart),
    path('log-out', views.LogoutView.as_view())
    ]