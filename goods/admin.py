from django.contrib import admin

# Register your models here.


# from .models import Goods,Category


class GoodsAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


# #将表单模型（数据库相关），和后台模型（后台页面样式）类对象进行结合注册
# admin.site.register(Goods, GoodsAdmin)
# admin.site.register(Category, CategoryAdmin)
