import json
import bcrypt
import jwt

from django.http              import HttpResponse, JsonResponse
from django.views             import View

from datetime                 import date, datetime
from .models                  import Category, Product, Reward, Collection, LikeUser, ProductContent


class CategoryView(View):
    def get(self, request):
        try:
            product = Product.object.all()
            product_list = [{
                'category_image'   : product.category_set.all()[0].image,
                'title'            : product.title,
                'goal_amout'       : product.goal_amount,
                'toal_amount'      : product.total_amount,
                'achieved_rate'    : product.achieved_rate,
                'total_supporters' : product.total_supporters,
                'closing_date'     : product.closing_date,
                'thumbnail'        : product.thumbnail_url,
                'category'         : product.category_set.all()[0].name,
                'id'               : product.id
                } for product in product]
            return JsonResponse({"MESSAGE" : "SUCCESS", "data" : {'product'  : product_list}}, status=200)
        except KeyError:
            return JsonResponse({"MESSAGE" : "INVALIED_KEY"}, status=400)


class CategoryDetailView(View):
    def get(self, request, Category_id):
        try:
            category_id = request.GET.get('category', None)
            data = Category.objects.get(id=category_id)
            relatd_product = data.product.all()
        
            product_list = [{
                'category_image'   : data.image,
                'title'            : product.title,
                'goal_amout'       : product.goal_amount,
                'toal_amount'      : product.total_amount,
                'achieved_rate'    : product.achieved_rate,
                'total_supporters' : product.total_supporters,
                'closing_date'     : product.closing_date,
                'thumbnail'        : product.thumbnail_url,
                'category'         : data.name,
                'id'               : product.id
                } for product in relatd_product]
            return JsonResponse({"MESSAGE" : "SUCCESS", "data" : {'product'  : product_list}}, status=200)
        except KeyError:
            return JsonResponse({"MESSAGE" : "INVALIED_KEY"}, status=400)





        
