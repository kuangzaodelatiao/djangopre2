from django.contrib import admin

# Register your models here.
from .models import Order,OrderDetail,PayRecord


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderDetailAdmin(admin.ModelAdmin):
    pass


class PayRecordAdmin(admin.ModelAdmin):
    pass


#将表单模型（数据库相关），和后台模型（后台页面样式）类对象进行结合注册
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(PayRecord, PayRecordAdmin)
