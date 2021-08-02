from django.urls import path
from products.views import ProductAPIView
app_name = "products"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('products/', ProductAPIView.as_view()),
]
