from django.contrib import admin

# Register your models here.

from .models import UserProfile,UserAddress

class UserProfileAdmin(admin.ModelAdmin):
    pass


class UserAddressAdmin(admin.ModelAdmin):
    pass


#将表单模型（数据库相关），和后台模型（后台页面样式）类对象进行结合注册
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
