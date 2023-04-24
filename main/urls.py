from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("home/", views.ProductList.as_view(), name="home"),
    path("product_detail/<int:pk>", views.ProductDetail.as_view(), name="product_detail"),
    path("account/", views.AccountView.as_view(), name="account"),
    path("cart/", views.Cart.as_view(), name="cart"),
]