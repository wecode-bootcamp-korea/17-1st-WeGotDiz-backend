from django.urls import path
from .views      import (
    ProductDetailView, 
    LikeView,
    CollectionView
)

from user.views import SignInView, SignUpView

urlpatterns = [
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/<int:product_id>/like', LikeView.as_view()),
    path('/main', CollectionView.as_view())
]