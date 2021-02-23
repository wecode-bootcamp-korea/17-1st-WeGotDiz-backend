import json
import re
import bcrypt
import jwt

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
        fullname = user.fullname

        #TOTAL FUNDING< LIKES
            
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
        
        return JsonResponse({"fullname" : fullname, "result" : like_list}, status=200)

# http -v GET 127.0.0.1:8000/user/list "Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTF9.qUSca7Udz6mGqgfPdnrKAmldt76CiPFjrTU0g9c_qzQ"

class UserFundView(View):
    # @login_decorator
    def get(self, request):
        if not User.objects.filter(id=2):
        # if not User.objects.filter(id=request.user.id):
            return JsonResponse({"message" : "INVALID_USER"})
        
        user = User.objects.get(id=2)
        # user = User.objects.get(id=request.user.id)
        fullname = user.fullname

        #TOTAL FUNDING< LIKES

        funding_list = []

        # fundings = Order.objects.filter(user=request.user.id).prefetch_related('reward')

        fundings = Order.objects.filter(user=2).prefetch_related('reward')
        fundings = fundings.prefetch_related('product')

        for funding in fundings:
            funding_list.append(
                {
                    "fullname" : funding.fullname,
                    "product_title": funding.title 
                }
            )

        # fundings = 

        return JsonResponse({"fullname" : fullname, "result" : funding_list}, status=200)


        




            


