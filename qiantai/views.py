from django.shortcuts import render,HttpResponse
# from user.user_model.rw_sql import read_sql,write_sql
# from edianzu.setMongodb import db
from qiantai.qiantai_models.structure_data import structure_data,hot_sell
# Create your views here.

def index(request):

    # username = request.COOKIES.get('username')
    username = request.session.get('username')
    print(username)
    if username == None:
        data = {
            'username': '您好,欢迎来到易点租',
            'login': '登录',
            'register': '注册',
        }
        return render(request, 'qiantai_index.html', data)
    else:
        # name = request.get_signed_cookie('name', salt='wuzaipei')
        data = {
            'username': '您好! %s 欢迎来到易点租' % username,
            'login': '',
            'register': '',
            'all_info':structure_data(), # 类型数据
            'hot_sale':hot_sell()
        }

        # 数据格式渲染
        shop = {
            'genre_name':'',
            'genre_img':'',
            'genre_id':'',
            'shop_list':[
                {
                    'shop_id':'',
                    'shop_img':'',
                    'shop_content':'',
                    'shop_price':''
                 }
            ]
        }



    # /gooods/search/笔记本
        # all_info = structure_data()

        # print(all_info.__len__())

        print(data['all_info'].__len__())

        return render(request, 'qiantai_index.html', data)


