import json
import bcrypt
import jwt

from datetime                 import date, datetime
from django.http              import HttpResponse, JsonResponse
from django.views             import View

from .models                  import (
        Category, 
        Product, 
        Reward, 
        Collection, 
        LikeUser, 
        ProductContent)


class ProductListView(View):
    def get(self, request, category_id=None):
        today = datetime.today()
        if category_id== None: 
            products = Product.objects.all()
        
            product_list = [{
                'category_image'   : product.category_set.first().image,
                'title'            : product.title,
                'goal_amout'       : product.goal_amount,
                'toal_amount'      : product.total_amount,
                'achieved_rate'    : product.achieved_rate,
                'total_supporters' : product.total_supporters,
                'closing_date'     : str((product.closing_date - today).days),
                'thumbnail'        : product.thumbnail_url,
                'category'         : product.category_set.first().name,
                'id'               : product.id,
                'maker_info_name'  : product.maker_info.name
                } for product in products]
        
            return JsonResponse({"MESSAGE" : "SUCCESS", "DATA" : product_list}, status=200)

        data = Category.objects.get(id=category_id)
        related_products = data.product.all()
        product_list = [{
            'category_image'   : data.image,
            'title'            : product.title,
            'goal_amout'       : product.goal_amount,
            'toal_amount'      : product.total_amount,
            'achieved_rate'    : product.achieved_rate,
            'total_supporters' : product.total_supporters,
            'closing_date'     : str((product.closing_date-today).days),
            'thumbnail'        : product.thumbnail_url,
            'category'         : data.name,
            'category_id'      : data.id,
            'product_id'       : product.id,
            'maker_info_name'  : product.maker_info.name
            } for product in related_products]
            
        return JsonResponse({"MESSAGE" : "SUCCESS", "DATA" : product_list}, status=200)
        
