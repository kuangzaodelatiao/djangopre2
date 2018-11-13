from django.shortcuts import render,HttpResponse
from user.user_model.password_md5 import md5
from user.user_model.rw_sql import read_sql,write_sql
import random


# Create your views here.
def index(request):

    return render(request,'user_login.html')


def register(request):

    return render(request,'user_register.html')


def manage_register(request):

    user_name = request.POST.get('username')
    user_password = md5(str(request.POST.get('passwd')))
    print(user_name,user_password)
    # 下面这两行设置夸域请求。
    # info['Access-Control-Allow-Origin'] = '*'
    # info['Access-Control-Allow-Headers'] = "Content-Type"

    # 查看用户是否存在
    sql_seach =  '''select * from userinfo where username="%s";'''%user_name
    is_cz = read_sql(sql_seach)
    print(is_cz)
    if len(is_cz):
        return HttpResponse('该用户已存在，请重新注册')
    else:
        # 保存用户信息
        sql_insert = '''insert into userinfo(username,password,userheader) values("%s","%s","%s")'''%(
            user_name,user_password,'/static/user_img/header.png'
        )

        isgood = write_sql(sql_insert)

        if isgood:
            return HttpResponse('1')
        else:
            return HttpResponse('信息有误注册失败！')

def md():
    st = ''
    for i in range(20):
        st += chr(random.randint(65, 91))
    return st

def manage_login(request):

    verify_name = request.POST.get('username')
    verify_passwd = md5(request.POST.get('passwd'))
    auto_login = request.POST.get('autoLogin')  # true 字符串类型
    print(verify_name,verify_passwd,auto_login)

    # 查看数据库是否有该用户、密码是否正确
    verify_sql = '''select * from userinfo where username="%s";'''%(verify_name)

    verify_info = read_sql(verify_sql)
    print(verify_info)
    print(len(verify_info))
    if len(verify_info) !=0:

        verify_info = verify_info[0]
        if verify_passwd==verify_info[2] and auto_login=='true':



            st = md()
            # 设置cookie
            rep = HttpResponse('1') # 代表成功登录的意思
            rep.set_cookie('username','%swzp'%st,max_age=2*60)
            # rep.set_signed_cookie('name',verify_name,salt='wuzaipei',max_age=2*60)

            # 设置session
            request.session['username'] = verify_name

            return rep


        elif verify_passwd==verify_info[2] and auto_login == 'false':

            rep = HttpResponse('1')  # 代表成功登录的意思
            # st = md()
            # rep.set_cookie('username','%swzp'%st+verify_name)
            # rep.set_signed_cookie('name', verify_name, salt='wuzaipei')
            request.session['username'] = verify_name
            return rep

        else:
            return HttpResponse('密码输入错误')
    else:
        return HttpResponse('没有该用户请注册')


def setSession(request):
    request.session['key'] = 'value'
    return HttpResponse('ok')
