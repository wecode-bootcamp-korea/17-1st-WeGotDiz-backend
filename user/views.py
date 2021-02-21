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

# funding view, like_view

class UserLikeView:
    @login_decorator
    def get(self, request):

        if not User.objects.filter(id=request.user.id):
            return JsonResponse({"message" : "INVALID_USER"})
        
        user = User.objects.get(id=request.user.id)

        information = {
            'id' : user.id,
            'name' : user.fullname,
            'email' : user.email,
            'image' : user.image,
            'password' : user.password,
        }

        account_user   = request.user
        # like           = request.GET.get('like')
        
        likes = LikeUser.objects.filter(user=request.user.id) # 유저가 좋아한 상품들을 라이크유저 테이블에서 가져옴
        like_list = [{
            "user" : account_user.id,
            # "product_id" : likes[0].product_id,
            "product__title" : likes[0].product.title,
            "product__maker_info" : likes[0].product.maker_info,
            "product__total_amount" : likes[0].product.total_amount,
            "product__achieved_rate" : likes[0].product.achieved_rate,
            "product__category" :  # 카테고리 가져오기 - prefetch_related
        }
        for like in likes]
        return JsonResponse({"result" : like_list}, status=200)



            


