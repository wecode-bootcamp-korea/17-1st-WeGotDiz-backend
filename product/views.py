import json
import bcrypt
import jwt

from datetime                 import date, datetime
from django.http              import HttpResponse, JsonResponse
from django.views             import View
from django.db.models         import Q

from .models                  import (
        Category, 
        Product, 
        Reward, 
        Collection, 
        LikeUser, 
        ProductContent)

class ProductListView(View):
    def get(self, request, category_id=0):
        today = datetime.today()

        products = Product.objects.filter() if category_id == 0 \
            else Product.objects.filter(category__id=category_id)

        product_list = [{
            'category_image'   : [category.image for category in product.category_set.all()],
            'title'            : product.title,
            'goal_amout'       : product.goal_amount,
            'toal_amount'      : product.total_amount,
            'achieved_rate'    : product.achieved_rate,
            'total_supporters' : product.total_supporters,
            'closing_date'     : str((product.closing_date - today).days),
            'thumbnail'        : product.thumbnail_url,
            'category'         : [category.name for category in product.category_set.all()],
            'category_id'      : [category.id for category in product.category_set.all()],
            'id'               : product.id,
            'maker_info_name'  : product.maker_info.name,
            } for product in products]
        
        return JsonResponse({"MESSAGE" : "SUCCESS", "DATA" : product_list}, status=200)
