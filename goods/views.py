from django.shortcuts import render,HttpResponse
from edianzu.setMysql import cursor
from bson import ObjectId
# # Create your views here.
# from .models import Goods,Category
def index(request,type):
    print(type)
    sql = ''
    key_goods = Goods.objects.filter(keywords__contains=type)

    # cate_goods = Category.objects.filter(name__contains = type)
    # 根据数据库来查询图片
    # for i in key_goods:
    #     print(i.image_id)
    # ObjectId("5be7efcd5caf8e28206a8093")
    # for mid in key_goods:
        # _id = mid.image_id
        # list1 = goods_img.find(_id = ObjectId(_id))
        # if list1 !=None:
            # img_list = list1.img_list[0]
    # content = {
    #     goods:key_goods
    # }
    return render(request,'goods_index.html')

