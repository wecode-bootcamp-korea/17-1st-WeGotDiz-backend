import json

from json.decoder import JSONDecodeError
from datetime     import datetime

from django.views import View
from django.http  import JsonResponse

from user.models      import User, MakerInfo
from product.models   import Product, Reward
from purchase.models  import Order, RewardOrder
from community.models import Comment
from user.utils       import login_decorator

class CommentView(View):
    def get(self, request, product_id): 
        try:
            product  = Product.objects.get(id=product_id)
            comments = Comment.objects.filter(product=product)

            userlist = [reward_order.order.user 
                for reward in product.reward_set.all() 
                for reward_order in reward.rewardorder_set.all()
            ]

            comment_list = []
            for comment in comments:
                user_funded = 'funded' if comment.user in userlist else 'not_funded'

                comment_list.append(
                        {
                        'name'        : comment.user.fullname,
                        'text'        : comment.text, 
                        'created_at'  : comment.created_at.strftime('%Y-%m-%d'),
                        'user_funded' : user_funded,
                        'parent'      : comment.parent
                        }
                )
            return JsonResponse({'message': "SUCCESS", 'comment_list': comment_list}, status=200)

        except KeyError:
            return JsonResponse({'message': "KEY_ERROR"}, status = 401)

    @login_decorator
    def post(self, request, product_id): 
        try:
            data   = json.loads(request.body)
            user   = request.user
            text   = data['text']
            parent = data.get('parent')
            
            product  = Product.objects.get(id=product_id)
            
            Comment.objects.create(
                user    = user,
                text    = text,
                product = product,
                parent  = parent
            )
            return JsonResponse({'message': "POST_SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({'message': "KEY_ERROR"}, status = 400)