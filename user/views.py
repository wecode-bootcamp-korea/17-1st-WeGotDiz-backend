import json
import re
import bcrypt
import jwt
import datetime

from django.http                       import JsonResponse, HttpResponse
from django.views                      import View
from django.db.models                  import Q

from user.models                       import User
from product.models                    import Product, LikeUser, Reward
from purchase.models                   import RewardOrder, Order

from .utils                            import login_decorator
from my_settings                       import SECRET_KEY, ALGORITHM

# funding view, like_view

class UserLikeView(View):
    @login_decorator
    def get(self, request):

        if not User.objects.filter(id=request.user.id):
            return JsonResponse({"message" : "INVALID_USER"})
        
        user = User.objects.get(id=request.user.id)
                    
        likes = LikeUser.objects.filter(user=request.user.id) 

        like_list = []

        for like in likes:
                all_categories = like.product.category_set.all()

                for category in all_categories: 
                    each_category = category.name

                    like_list.append(
                        {
                            # "user" : request.user.id, 이게 꼭 필요항가?
                            "product_id" : like.product.id,
                            "product_title" : like.product.title,
                            "product_image" : like.product.thumbnail_url,
                            "product_maker_info" : like.product.maker_info.name,
                            "product_total_amount" : like.product.total_amount,  
                            "product_achieved_rate" : like.product.achieved_rate, 
                            "product_category" :  each_category
                        }
                    )

                    # 한번에 드리기 -> data + list 작업 수행해라 허민지여... 
                    data = [
                                {
                                    "id" : user.id,
                                    "fullname" : user.fullname
                                }
                            ]
        
        return JsonResponse({"data" : data, "like_list" : like_list}, status=200)

# http -v GET 127.0.0.1:8000/user/list "Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTF9.qUSca7Udz6mGqgfPdnrKAmldt76CiPFjrTU0g9c_qzQ"

# "data": {
#   "user_info" :   [{
#     "id": 1,
#     "userName":"위갓디즈",
#   }]

class UserFundView(View):
    # @login_decorator
    def get(self, request):
        if not User.objects.filter(id=1):
        # if not User.objects.filter(id=request.user.id):
            return JsonResponse({"message" : "INVALID_USER"})
        
        #TOTAL FUNDING< LIKES

        user = User.objects.get(id=1)
        # user = User.objects.get(id=request.user.id)

        data = []

        for order in user.order_set.all():
            #order objects
            for reward in order.reward.all():
                closing_date = datetime.datetime.today() - reward.product.closing_date
                #reward objects
                data = [
                    {
                        "id" : user.id,
                        "fullname" : user.fullname,
                        "product_image" : reward.product.thumbnail_url,
                        "product_date_countdown" : closing_date.days,
                        "product_total_amount" : reward.product.total_amount,
                        "product_achieved_rate" : reward.product.achieved_rate,
                        "product_title" : reward.product.title,
                        "product_maker_info" : reward.product.maker_info.name,
                        "product_category" : reward.product.category_set.all()[0].name,
                    }
                ]

                return JsonResponse({"data" : data, "result" : funding_list}, status=200)

        
        # http -v GET 127.0.0.1:8000/user/fundinglist

# class UserInfoView(View):
#     @login_decorator  
#     def get(self, request, product_id): 
#         user  = request.user
#         user_info = {
#             'email' = user.email,
#             'name' = user.fullname
#         }
#     return JsonResponse({'user_info' : user_info}, status=200)
     




            


