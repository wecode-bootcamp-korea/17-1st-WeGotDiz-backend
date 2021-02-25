from django.urls import path, include
<<<<<<< HEAD
from .views      import ProductListView #CategoryView, CategoryDetailView, CategoryFilterView
urlpatterns = [
    path('/category', ProductListView.as_view()),
    path('/category/<int:category_id>', ProductListView.as_view()),
=======

from user.views import SignInView, SignUpView
from .views      import (
    ProductDetailView, LikeView, MainView
)

urlpatterns = [
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/<int:product_id>/like', LikeView.as_view()),
    path('/main', MainView.as_view()),
    path('/main/<int:category_id>', MainView.as_view())
>>>>>>> 905d93f2f515526447b3313e371e3c669fa8e59f
]