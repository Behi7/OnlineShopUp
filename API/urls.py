from . import views
from django.urls import path

urlpatterns = [
    path('product', views.ProductListViews.as_view()),
    path('product/<int:pk>', views.ProducDetailViews.as_view()),
    path('category', views.CategoryListViews.as_view()),
    path('category/<int:pk>/', views.CategoryDetailViews.as_view()),
    path('login', views.LoginView.as_view()),
    path('register', views.UserCreateView.as_view())
]