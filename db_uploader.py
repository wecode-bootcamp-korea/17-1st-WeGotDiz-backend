import collections
import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WeGotDiz.settings")
django.setup()


from product.models import (
    Category,
    Product,
    Reward,
    Collection,
    LikeUser,
    ProductContent
    #CategoryProduct,
    #CollectionProduct
)

from user.models import User, MakerInfo

# 카테고리 업로드
CSV_PATH = "./csv/category.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            category_id = row[0]
            name = row[1]
            image = row[2]
            print(category_id, name, image)
            
            Category.objects.create(name = name, image = image)


# maker_info 파일 업데이트
CSV_PATH = "./csv/makers_info.csv"
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
CSV_PATH = "./csv/users.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        if row[0]:
            user_id    = row[0]
            fullname   = row[1]
            email      = row[2]
            password   = row[3]
            maker_info = row[4]
            image      = row[5]
            
            maker_info = MakerInfo.objects.get(name=maker_info).id
            print(user_id, fullname, email, password, maker_info, image)
            User.objects.create(
                    fullname   = fullname,
                    image      = image,
                    email      = email,
                    password   = password,
                    maker_info_id = maker_info
                    )


# 연습용 product 파일 업로드
CSV_PATH = "./csv/product_practice.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            Product_id       = row[0]
            title            = row[1]
            thumbnail_url    = row[2]
            description      = row[3]
            goal_amount      = row[4]
            total_amount     = row[5]
            achieved_rate    = row[6]
            total_likes      = row[7]
            total_supporters = row[8]
            opening_date     = row[9]
            closing_Date     = row[10]
            maker_info       = row[11]

            print(Product_id, title, thumbnail_url, description, goal_amount, total_amount, achieved_rate, total_likes, total_supporters, opening_date, closing_Date, maker_info)
            
            maker_info = MakerInfo.objects.get(name = maker_info).id
            Product.objects.create(
                    title            = title, 
                    thumbnail_url    = thumbnail_url, 
                    description      = description,
                    goal_amount      = goal_amount,
                    total_amount     = total_amount,
                    achieved_rate    = achieved_rate,
                    total_likes      = total_likes,
                    total_supporters = total_supporters,
                    opening_date     = opening_date,
                    closing_date     = closing_Date,
                    maker_info_id    = maker_info)

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

            print(collection_id, name, start_date, end_date)
            Collection.objects.create(
                    name       = name,
                    start_date = start_date,
                    end_date   = end_date
                    )


# Reward 파일 업로드
CSV_PATH = './csv/Reward.csv'
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            reword_id     = row[0]
            name          = row[1]
            price         = row[2]
            combination   = row[3]
            stock         = row[4]
            quantity_sold = row[5]
            product       = row[6]


            product = Product.objects.get(title=product).id
 
            print(reword_id, name, price, combination, stock, quantity_sold, product)
            Reward.objects.create(
                    name = name,
                    price = price,
                    combination =combination,
                    stock = stock,
                    quantity_sold =quantity_sold,
                    product_id = product
                    )

"""
# catgory_product 파일 업로드
CSV_PATH = './csv/categories_product.csv'
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            category_product_id = row[0]
            category            = row[1]
            product             = row[2]
            print('********************************************')

            category = Category.objects.get(name=category).id
            product  = Product.objects.get(title=product).id

            print(category, product)
            CategoryProduct.objects.create(
                    category_id = category,
                    product_id  = product
                    )


# collection_product 파일 업로드
CSV_PATH = './csv/collection_product.csv'
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            collection_product_id   =  row[0]
            collection              =  row[1]
            product                 =  row[2]

            collection = Collection.objects.get(name=collection).id
            product    = Product.objects.get(title=product).id

            print(collection_product_id, collection, product)

            CollectionProduct.objects.create(
                    collection_id = collection,
                    product_id    = product
                    )
"""









