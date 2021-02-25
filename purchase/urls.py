from django.urls  import path
from .views       import RewardListView, RewardOrderView
from user.views   import UserInfoView

urlpatterns = [
   path('/rewardlist', RewardListView.as_view()),
   path('/rewardorder', RewardOrderView.as_view()),
   path('/userinfo', UserInfoView.as_view())
]
