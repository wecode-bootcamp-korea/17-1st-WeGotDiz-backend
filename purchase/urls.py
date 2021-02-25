from django.urls  import path
from .views       import RewardListView, RewardOrderView

urlpatterns = [
   path('/rewardlist', RewardListView.as_view()),
   path('/rewardorder', RewardOrderView.as_view())
]