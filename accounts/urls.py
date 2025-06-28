from django.urls import path
from .views import (
    ProfileView,
    ListCategory, DetailCategory,
    ListProduct, DetailProduct,
    ListUser, DetailUser,
    ListCart, DetailCart,
    RegistrationView, LoginView, LogoutView
)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('profile/',ProfileView.as_view(), name='profile'),

    path('categories/', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),

    path('products/', ListProduct.as_view(), name='products'),
    path('products/<str:pk>/', DetailProduct.as_view(), name='singleproduct'),

    path('users/', ListUser.as_view(), name='users'),
    path('users/<int:pk>/', DetailUser.as_view(), name='singleuser'),

    path('carts/', ListCart.as_view(), name='allcarts'),
    path('carts/<int:pk>/', DetailCart.as_view(), name='cartdetail'),
] 