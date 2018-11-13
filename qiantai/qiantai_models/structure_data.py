# coding:utf-8
from user.user_model.rw_sql import read_sql,write_sql
from edianzu.setMongodb import db

def structure_data():
    # 开始查询构造数据：

    # 1、获取所有类别

    # 商品数据
    goods = db.goods_headerimg
    # 种类数据
    category = db.category_brand

    genre_sql = '''select * from category where is_del="%s";''' % (0)
    genre_all = read_sql(genre_sql)

    all_info = []
    shop_list = []
    if len(genre_all) >= 3:

        for genre in genre_all[:3]:
            # genre_info = {'genre_name':genre[1],}
            # 种类图片
            img = list(category.find({'category_id': genre[0]}))[0]['category_img']
            # 查询种类下面的商品
            goods_sql = '''select * from goods where category=%s;''' % int(genre[0])
            goods_gds = read_sql(goods_sql)

            if len(goods_gds) <= 6 or len(goods_gds) > 0:
                for goods_goods in goods_gds:
                    shop_list.append({'shop_id': goods_goods[0],
                                      'shop_img': list(goods.find({'goods_id': goods_goods[0]}))[0]['img_list'][0],
                                      'shop_content': goods_goods[3],
                                      'shop_price': goods_goods[4]}.copy())

            elif len(goods_gds) > 6:
                for goods_goods in goods_gds[:6]:
                    shop_list.append({'shop_id': goods_goods[0],
                                      'shop_img': list(goods.find({'goods_id': goods_goods[0]}))[0]['img_list'][0],
                                      'shop_content': goods_goods[3],
                                      'shop_price': goods_goods[4]}.copy())
            else:
                pass

            all_info.append({
                'genre_name': genre[1],
                'genre_img': img,
                'genre_id': genre[0],
                'shop_list': shop_list
            })
            shop_list = []

    elif len(genre_all) < 3:
        for genre in genre_all[:3]:
            # genre_info = {'genre_name':genre[1],}
            # 种类图片
            img = list(category.find({'category_id': genre[0]}))[0]['category_img']
            # 查询种类下面的商品
            goods_sql = '''select * from goods where category=%s and status = 1;''' % int(genre[0])
            goods_gds = read_sql(goods_sql)

            if len(goods_gds) <= 6 or len(goods_gds) > 0:
                for goods_goods in goods_gds:
                    shop_list.append({'shop_id': goods_goods[0],
                                      'shop_img': list(goods.find({'goods_id': goods_goods[0]}))[0]['img_list'][0],
                                      'shop_content': goods_goods[3],
                                      'shop_price': goods_goods[4]}.copy())

            elif len(goods_gds) > 6:
                for goods_goods in goods_gds[:6]:
                    shop_list.append({'shop_id': goods_goods[0],
                                      'shop_img': list(goods.find({'goods_id': goods_goods[0]}))[0]['img_list'][0],
                                      'shop_content': goods_goods[3],
                                      'shop_price': goods_goods[4]}.copy())
            else:
                pass

            all_info.append({
                'genre_name': genre[1],
                'genre_img': img,
                'genre_id': genre[0],
                'shop_list': shop_list
            })
            shop_list = []

    return all_info


def hot_sell():

    sell_sql = '''SELECT * FROM goods ORDER BY is_show_sales_count DESC limit 6;'''

    hot_sale = read_sql(sell_sql)[:6]

    goods = db.goods_headerimg

    data = []
    for item in hot_sale:
        data.append({'shop_content':item[3],
                     'shop_id':item[0],
                     'shop_price':item[4],
                     'shop_img':list(goods.find({'goods_id': item[0]}))[0]['img_list'][0]
                     })

    return data


# print(len(hot_sell()))


