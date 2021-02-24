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
    def get(self, request, category_id=0):
        today = datetime.today()

        products = Product.objects.filter() if category_id == 0 \
            else Product.objects.filter(category__id=category_id)

        category = Category.objects.filter().first() if category_id == 0\
                else Category.objects.filter(product__id=category_id).first()
        
        product_list = [{
            'category_image'   : category.image,
            'title'            : product.title,
            'goal_amout'       : product.goal_amount,
            'toal_amount'      : product.total_amount,
            'achieved_rate'    : product.achieved_rate,
            'total_supporters' : product.total_supporters,
            'closing_date'     : str((product.closing_date - today).days),
            'thumbnail'        : product.thumbnail_url,
            'category'         : category.name,
            'category_id'      : category.id,
            'id'               : product.id,
            'maker_info_name'  : product.maker_info.name,
            } for product in products]
        
        return JsonResponse({"MESSAGE" : "SUCCESS", "DATA" : product_list}, status=200)


# 쿼리문으로 코드 줄이기
class ProductlistQueryView(View):
    def get(self, request):
        data  = request.GET.get('category', 0)
        endYN = request.GET.get('endYN', 1)
        #order = request.GET.get('order', 'recommend')
        today = datetime.today()
        
        products = Product.objects.filter() if data ==0\
                else Product.objects.filter(category__id=data)

        category = Category.objects.filter().first() if data == 0\
                else Category.objects.filter(product__id=data).first()

        closing_date = (products.first().closing_date - datetime.today()).days

        products = products.filter(closing_date__lt) if endYN == 2 else products.filter(closing_date < 10)


        
        product_list = [{
            'category_image'   : category.image,
            'title'            : product.title,
            'goal_amout'       : product.goal_amount,
            'toal_amount'      : product.total_amount,
            'achieved_rate'    : product.achieved_rate,
            'total_supporters' : product.total_supporters,
            'closing_date'     : str((product.closing_date - today).days),
            'thumbnail'        : product.thumbnail_url,
            'category'         : category.name,
            'category_id'      : category.id,
            'id'               : product.id,
            'maker_info_name'  : product.maker_info.name
            } for product in products]
        
        return JsonResponse({"MESSAGE" : "SUCCESS", "DATA" : product_list}, status=200)

