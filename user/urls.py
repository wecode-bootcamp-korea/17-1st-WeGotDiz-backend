from django.urls import path
from user.views import UserLikeView, UserFundView

urlpatterns = [
   path('/likelist', UserLikeView.as_view()), 
   path('/fundinglist', UserFundView.as_view())
]