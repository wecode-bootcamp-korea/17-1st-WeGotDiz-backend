from django.urls import path, include
from .views      import CategoryView, CategoryDetailView

urlpatterns = [
        path('/category', CategoryView.as_view()),
        path('/category/<int:Category_id>', CategoryDetailView.as_view())

]
