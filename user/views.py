import json
import datetime
import bcrypt
import jwt

from json.decoder                      import JSONDecodeError
from django.http                       import JsonResponse, HttpResponse
from django.views                      import View
from django.core.validators            import validate_email
from django.core.exceptions            import ValidationError

from .models                           import User
from product.models                    import Product, LikeUser, Reward
from purchase.models                   import RewardOrder, Order

from .utils                            import login_decorator
from my_settings                       import SECRET_KEY, ALGORITHM

from .validators                       import validate_password


MINIMUM_PASSWORD_LENGTH  = 8

class SignUpView(View):

    def post(self,request):
        try:
            data         = json.loads(request.body)

            email        = data['email']
            full_name    = data['fullname']
            password     = data['password']
            maker_info   = data.get('maker_info')

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "EMAIL_EXISTS"}, status=400)

            if not (email and full_name and password):
                return JsonResponse({"message" : "REQUIRED_FIELD"}, status=400)

            if len(password) < MINIMUM_PASSWORD_LENGTH:
                return JsonResponse({"message" : "PASSWORD_MUST_BE_LONGER_THAN_EIGHT_LETTERS"}, status=400)

            validate_email(email)

            validate_password(password)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                fullname    = full_name,
                email       = email,
                password    = hashed_password,
                maker_info  = maker_info
            )

            return JsonResponse({"message" : "SUCCESS"}, status=201)
            
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        except ValidationError:
            return JsonResponse({"message" : "VALIDATION_ERROR"}, status=400)

class SignInView(View):

    def post(self, request):
        data = json.loads(request.body)

        try:
            email     = data.get('email', None)
            password  = data.get('password', None)

            if not (email and password):
                return JsonResponse({"message" : "REQUIRED_FIELD"}, status=400)

            if not User.objects.filter(email=email):
                return JsonResponse({"message" : "INVALID_USER"}, status=401)

            user = User.objects.get(email=email)

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                access_token = jwt.encode({"id" : user.id}, SECRET_KEY, algorithm=ALGORITHM)
                return JsonResponse({"message" : "SUCCESS", "TOKEN" : access_token}, status=200)

            return JsonResponse({"message" : "UNAUTHORIZED_APPROACH"}, status=401)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

class UserLikeView(View):
    @login_decorator
    def get(self, request):
        user_info = [
            {
                "id"            : request.user.id,
                "userName"      : request.user.fullname
            }
        ]
        
        likes = LikeUser.objects.filter(user=request.user.id)
        
        like_list = [{
            "product_id"            : like.product.id,
            "product_title"         : like.product.title,
            "product_image"         : like.product.thumbnail_url,
            "product_maker_info"    : like.product.maker_info.name,
            "product_total_amount"  : like.product.total_amount,  
            "product_achieved_rate" : like.product.achieved_rate, 
            "product_category"      : [category.name for category in like.product.category_set.all()]

        } for like in likes]
        
        return JsonResponse({"data" : {'user_info' : user_info, 'like_list' : like_list}}, status=200)

class UserFundView(View):
    @login_decorator
    def get(self, request):
        user_info = [
            {
                "id"            : request.user.id,
                "userName"      : request.user.fullname
            }
        ]
    
        funding_list = [ 
            {
                "product_image"          : reward.product.thumbnail_url,
                "product_date_countdown" : str((datetime.datetime.today() - reward.product.closing_date.replace(tzinfo=None)).days),
                "product_total_amount"   : reward.product.total_amount,
                "product_achieved_rate"  : reward.product.achieved_rate,
                "product_title"          : reward.product.title,
                "product_maker_info"     : reward.product.maker_info.name,
                "product_category"       : [category.name for category in reward.product.category_set.all()]
            }
            for order in request.user.order_set.all()
            for reward in order.reward.all()]

        return JsonResponse({"data" : {'user_info' : user_info, 'funding_list' : funding_list}}, status=200)

class UserInfoView(View):
    @login_decorator  
    def get(self, request, product_id): 
        user_info = {
            'email' : request.user.email,
            'name' : request.user.fullname
        }
        return JsonResponse({'user_info' : user_info}, status=200)
