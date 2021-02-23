from django.urls import path
from user.views import UserLikeView, UserFundView

urlpatterns = [
   path('/likelist', UserLikeView.as_view()),   # mypage로 바꿔라 나중에;
   path('/fundinglist', UserFundView.as_view())
]