<<<<<<< HEAD
=======
from django.urls import path

from user.views  import SignUpView, SignInView

urlpatterns = [
   path('/signup', SignUpView.as_view()),
   path('/signin', SignInView.as_view())
]
>>>>>>> 905d93f2f515526447b3313e371e3c669fa8e59f
