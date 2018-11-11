# from django.db import models

# # Create your models here.


# class UserProfile(models.Model):
#     username = models.CharField(max_length=100,null=False,verbose_name='用户名')
#     password = models.CharField(max_length=100, null=False, verbose_name='密码')
#     head_img = models.ImageField(
#         upload_to='static/user/%Y/%m', verbose_name='头像', blank=True, default='', max_length=500)
#     # mobile = models.CharField(verbose_name='联系方式', max_length=11, blank=True)
#     # wechat = models.CharField(verbose_name='微信', max_length=100, blank=True)
#     # integral = models.IntegerField(default=0, verbose_name='积分')
#     # balance = models.DecimalField(
#         # decimal_places=2, max_digits=8, default=0.0, verbose_name='余额')
#     # open_id = models.CharField(max_length=100, verbose_name='OpenId',blank=True)
    
#     remark = models.TextField(verbose_name='备注',blank=True)

#     def __str__(self):
#         return self.username

#     class Meta:
#         verbose_name = '用户管理'
#         verbose_name_plural = verbose_name


# class UserAddress(models.Model):
#     username = models.ForeignKey(UserProfile, null=True,  
#                              blank=True, verbose_name='用户',on_delete=models.CASCADE)
#     address = models.CharField(max_length=500, verbose_name='收件地址')
#     name = models.CharField(max_length=20, verbose_name='收件人')
#     mobile = models.CharField(max_length=30, verbose_name='手机号')

#     def __str__(self):
#         return self.address

#     class Meta:
#         verbose_name = '用户地址'
#         verbose_name_plural = verbose_name
