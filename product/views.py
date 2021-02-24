import json
import datetime

from django.http      import JsonResponse, HttpResponse
from django.views     import View
from django.conf      import settings

from my_settings      import SECRET_KEY, ALGORITHM
from user.utils       import login_decorator
from user.models      import User, MakerInfo
from .models          import  (
    Category, Product, Reward,
    LikeUser, ProductContent, Collection
)

class ProductDetailView(View):
    
    def get(self, request, product_id):

        try:
            tab = request.GET.get('tab', '스토리')

            product = Product.objects.get(id=product_id)    
            today    = datetime.datetime.today()
            closing_date = product.closing_date

            results = {

                "id"            : product.id,
                "category"      : product.category_set.first().name,
                "title"         : product.title,
                "tab_names"     : [content.name for content in product.productcontent_set.all()],
                "thumbnail_url" : product.thumbnail_url,
                "description"   : product.description,
                "goal_amount"   : product.goal_amount,
                "opening_date"  : product.opening_date,
                "closing_date"  : closing_date,
                "days_left"     : (closing_date - today).days,
                "info_box"      : {
                        "achieved_rate"    : product.achieved_rate,
                        "total_amount"     : product.total_amount,
                        "total_supporters" : product.total_supporters
                    },
                "total_likes"   : product.total_likes,
                "tab"           : product.productcontent_set.get(name=tab).content, #html
                "maker_name"    : product.maker_info.name,
                "maker_image"   : product.maker_info.user_set.first().image,
                "levels"  : [
                    { 
                        "name"  : "평판",
                        "level" : product.maker_info.reputation_level
                    },
                    { 
                        "name"  : "소통",
                        "level" : product.maker_info.communication_level
                    },
                    { 
                        "name"  : "인기",
                        "level" : product.maker_info.popularity_level
                    }
                ]

            }

            return JsonResponse( {'data' : results}, status = 200 )

        except KeyError:
            return JsonResponse( {'message' : "INVALID_KEY"}, status = 400 )


class LikeView(View):

    @login_decorator
    def post(self, request, product_id):

        try:
            user_id     = request.user.id
            product     = Product.objects.get(id=product_id)
            total_likes = product.total_likes

            if LikeUser.objects.filter(product_id=product_id, user_id=user_id).exists():
                LikeUser.objects.get(product_id=product_id, user_id=user_id).delete()
                Product.objects.filter(id=product_id).update(total_likes = total_likes - 1)

                return JsonResponse({'message':'SUCCESS'}, status=204)

            LikeUser.objects.create(product_id=product_id, user_id=user_id)
            Product.objects.filter(id=product_id).update(total_likes = total_likes + 1)
            
            return JsonResponse({'message':'SUCCESS', 'total_likes': total_likes}, status=201)

        except KeyError: 
            return JsonResponse({'message':'KEY_ERROR', 'total_likes': total_likes}, status=400)


class CollectionView(View):

    def get(self, request):
        try:
            collections = Collection.objects.all()
            result      = []
    
            for collection in collections:
                projects = collection.product.all()[:2]

                planData = [
                    {
                        "planId"   : collection.id,
                        "planTitle": collection.name,
                        "products" : [
                            {
                                "id"       : project.id,
                                "text"     : project.title,
                                "percent"  : project.achieved_rate,
                                "category" : project.category_set.first().name,
                                "img"      : project.thumbnail_url
                            } 
                            for project in projects
                        ]
                    }
                ]

                result.append(planData)

            return JsonResponse( {'data' : result}, status = 200 )

        except KeyError:
            return JsonResponse( {'message' : "KEY_ERROR"}, status = 400 )