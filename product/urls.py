from django.urls import path, include

from user.views import SignInView, SignUpView
from .views      import (
    ProductDetailView, LikeView, MainView
)

urlpatterns = [
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/<int:product_id>/like', LikeView.as_view()),
    path('/main', MainView.as_view()),
    path('/main/<int:category_id>', MainView.as_view())
]