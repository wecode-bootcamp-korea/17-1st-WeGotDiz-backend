from django.urls import path
from user.views import UserLikeView

urlpatterns = [
   path('/list', UserLikeView.as_view())   
]