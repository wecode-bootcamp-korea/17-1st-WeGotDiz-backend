import json
import re
import bcrypt
import jwt

from django.http                       import JsonResponse, HttpResponse
from django.views                      import View
from django.db.models                  import Q

from user.models                       import User
from product.models                    import LikeUser

from .utils                            import login_decorator
from my_settings                       import SECRET_KEY, ALGORITHM

# funding view, like_view

class UserLikeView(View):
    @login_decorator
    def get(self, request):

        if not User.objects.filter(id=request.user.id):
        # if not User.objects.filter(id=2):
            return JsonResponse({"message" : "INVALID_USER"})
        
        user = User.objects.get(id=request.user.id)
        # user = User.objects.get(id=2)
        information = {
            # 'id' : user.id,
            'fullname' : user.fullname,
            'email' : user.email,
            # 'password' : user.password,
            'maker_info' : user.maker_info
        }
    

        account_user   = request.user
        # account_user = User.objects.get(id=2)
        
        likes = LikeUser.objects.filter(user=request.user.id) # 유저가 좋아한 상품들을 라이크유저 테이블에서 가져옴
        # likes = LikeUser.objects.get(user=account_user)

        # print('===================================================')
        # print(likes.product.id)
        # print(likes.product.maker_info.id)
        # print(likes.product.total_amount)
        # print(likes.product.achieved_rate)
        # a = likes.product.category_set
        # print(a[0].name)
        # print('===================================================')

        # q[0].product.category_set.all()[0].name
        # 스택오버플로우
        # queryset = YourModel.objects.filter(some__filter="some value").values()
        # return JsonResponse({"models_to_return": list(queryset)})


        # likes = LikeUser.objects.filter(user=2)
        # like_list = [{
        #     "user" : account_user.id,
        #     "product_id" : like.product.id,
        #     "product__title" : like.product.title,
        #     "product__image" : like.product.thumbnail_url,
        #     "product__maker_info" : like.product.maker_info.id,
        #     "product__total_amount" : like.product.total_amount,
        #     "product__achieved_rate" : like.product.achieved_rate,
        #     "product__category" :  like.product.category_set.first()
        # }
        # for like in likes]

    

        likes = LikeUser.objects.filter(user=request.user.id)
        like_list = []

        for like in likes:
                all_categories = like.product.category_set.all()

                for category in all_categories: # JSON serialize error가 또 나옴...
                    each_category = category.name
                    print('======================================')
                    print(each_category)
                    print('======================================')

                    like_list.append(
                        {
                            "user" : account_user.id,
                            "product_id" : like.product.id,
                            "product__title" : like.product.title,
                            "product__image" : like.product.thumbnail_url,
                            "product__maker_info" : like.product.maker_info.id,
                            "product__total_amount" : like.product.total_amount,
                            "product__achieved_rate" : like.product.achieved_rate,
                            "product__category" :  each_category
                        }
                    )
        

        return JsonResponse({"information" : information, "result" : like_list}, status=200)



            


