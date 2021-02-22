from django.urls import path
from user.views import UserLikeView

urlpatterns = [
   path('/list', UserLikeView.as_view())   # mypage로 바꿔라 나중에;
]