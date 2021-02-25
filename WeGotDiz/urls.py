from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    path('user', include('user.urls')),
    path('product', include('product.urls')),
    path('product/<int:product_id>/purchase', include('purchase.urls')),
]
=======
    path('product', include('product.urls')),   
    path('user', include('user.urls'))
]
>>>>>>> 905d93f2f515526447b3313e371e3c669fa8e59f
