from django.urls import path, include
from .views      import ProductListView, ProductlistQueryView
from .views      import ProductListView

urlpatterns = [
    path('/main', ProductListView.as_view()),    
    path('/main/<int:category_id>', ProductListView.as_view()),
    path('/main/query', ProductlistQueryView.as_view())
]
