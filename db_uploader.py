import collections
import os
import django
import csv
import sys
# import dateutil.parser
from datetime import datetime
#from django.utils.dateparse import parse_datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WeGotDiz.settings")
django.setup()

from product.models import (
        Category,
        Product,
        Reward,
        Collection,
        LikeUser,
        # ProductContent,
        # CategoryProduct,
        # CollectionProduct
        )

from user.models import User, MakerInfo
from purchase.models import Address, Order, RewardOrder

# 카테고리 업로드
CSV_PATH = "./csv/category.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            category_id = row[0]
            name        = row[1]
            image       = row[2]
            
            Category.objects.create(name = name, image = image)

# maker_info 파일 업데이트
CSV_PATH = "./csv/maker_info.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            maker_info_id       = row[0]
            name                = row[1]
            reputation_level    = row[2]
            communication_level = row[3]
            popularity_level    = row[4]
            print(maker_info_id, name, reputation_level, communication_level, popularity_level)
            
            MakerInfo.objects.create(
                    name = name,
                    reputation_level    = reputation_level,
                    communication_level = communication_level,
                    popularity_level    = popularity_level
                    )

# user csv 파일 업데이트
CSV_PATH = "./csv/user.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        if row[0]:
            user_id       = row[0]
            fullname      = row[1]
            email         = row[2]
            password      = row[3]
            maker_info_id = row[4]
            image         = row[5]
            
            maker_info = MakerInfo.objects.get(id=maker_info_id)

            User.objects.create(
                    fullname   = fullname,
                    image      = image,
                    email      = email,
                    password   = password,
                    maker_info_id = maker_info.id
                    )

# 연습용 product 파일 업로드
CSV_PATH = "./csv/product.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            product_id       = row[0]
            category_id      = row[1]
            title            = row[2]
            thumbnail_url    = row[3]
            description      = row[4]
            goal_amount      = row[5]
            total_amount     = row[6]
            achieved_rate    = row[7]
            total_supporters = row[8]
            opening_date     = row[9]
            closing_date     = row[10]
            total_likes      = row[11]
            maker_info_id    = row[12]
            
            maker_info = MakerInfo.objects.get(id=maker_info_id)

            Product.objects.create(
                    title            = title, 
                    thumbnail_url    = thumbnail_url, 
                    description      = description,
                    goal_amount      = goal_amount,
                    total_amount     = total_amount,
                    achieved_rate    = achieved_rate,
                    total_supporters = total_supporters,
                    opening_date     = datetime.strptime(opening_date,'%Y-%m-%d %H:%M:%S'),
                    closing_date     = datetime.strptime(closing_date,'%Y-%m-%d %H:%M:%S'),
                    total_likes      = total_likes,
                    maker_info_id    = maker_info.id)

        # for category_id in row[1]:
        #     for product_id in row[0]:

            product = Product.objects.get(id=product_id)
            category = Category.objects.filter(id=category_id).first()
            print('***********************************')
            print(category)
            print('***********************************')
            print(category.product.all())
            category.product.add(product)

# collection 업로드
CSV_PATH = './csv/collection.csv'
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            collection_id  = row[0]
            name           = row[1]
            start_date     = row[2]
            end_date       = row[3]

            Collection.objects.create(
                    name       = name,
                    start_date = start_date,
                    end_date   = end_date
                    )


# Reward 파일 업로드
CSV_PATH = './csv/reward.csv'
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            reward_id     = row[0]
            name          = row[1]
            price         = row[2]
            combination   = row[3]
            stock         = row[4]
            quantity_sold = row[5]
            product_id    = row[6]

            product = Product.objects.get(id=product_id)
 
            Reward.objects.create(
                    name          = name,
                    price         = price,
                    combination   = combination,
                    stock         = stock,
                    quantity_sold = quantity_sold,
                    product_id    = product.id
                    )

# address 파일 업로드
CSV_PATH = './csv/address.csv'
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            address_id  = row[0]
            address     = row[1]
            user_id     = row[2]

            Address.objects.create(
                    address = address,
                    user_id = user_id
                    )

# order 파일 업로드
CSV_PATH = './csv/order.csv'
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            order_id       = row[0]
            fullname       = row[1]
            contact_number = row[2]
            delivery_note  = row[3]
            total_amount   = row[4]
            delivery_fee   = row[5]
            donation       = row[6]
            address_id     = row[7]

            address = Address.objects.get(id=address_id)

            print(order_id, fullname, address_id)
            Order.objects.create(
                    fullname = fullname,
                    contact_number = contact_number,
                    delivery_note = delivery_note,
                    total_amount = total_amount,
                    delivery_fee = delivery_fee,
                    donation = donation,
                    address_id  = address.id
                    )

# reward_order 파일 업로드
CSV_PATH = './csv/reward_order.csv'
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            reward_order_id = row[0]
            reward_id       = row[1]
            order_id        = row[2]
            quantity        = row[3]

            reward = Reward.objects.get(id=reward_id)
            order  = Order.objects.get(id=order_id)

            print(reward_id, order_id, quantity)
            RewardOrder.objects.create(
                    reward_id = reward_id,
                    order_id  = order_id,
                    quantity  = quantity 
                    )
            








