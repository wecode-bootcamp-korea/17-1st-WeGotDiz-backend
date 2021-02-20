import json
import re
import bcrypt
import jwt

from django.http                       import JsonResponse, HttpResponse
from django.views                      import View
from django.db.models                  import Q

from user.models                       import (
    User
)

from utils                             import login_decorator
from my_settings                       import SECRET_KEY, ALGORITHM

class UserView(View): 
    @login_decorator
    def get(self, request): #개인회원, 일반 투자자 하드코딩 가능한지 여쭤보기
        user = User.objects.get(id=request.user.id)

        information = {
            'id' : user.id,
            'name' : user.fullname,
            'email' : user.email,
            'image' : user.image,
            'password' : user.password,
        }

class UserLikeView:
    @login_decorator
    def get(self, request):
        account_user   = request.user
        # like           = request.GET.get('like')

        likes = LikeUser.objects.filter(user=request.user.id)
        for like in likes:


