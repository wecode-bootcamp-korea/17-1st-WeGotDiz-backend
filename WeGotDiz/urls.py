from django.urls import path, include

urlpatterns = [
    path('user', include('user.urls')),
    path('product', include('product.urls')),
    path('product/<int:product_id>/purchase', include('purchase.urls')),
    path('product/<int:product_id>', include('community.urls'))
]