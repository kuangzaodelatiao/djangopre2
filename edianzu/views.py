# from django.shortcuts import render,HttpResponse,redirect
# import datetime
# import json
# from .setMongodb import pinglun
# from bson import ObjectId

# # Create your views here.


# def index(request):
#     # print(render(request,'index.html').__dict__['_container'][0])
#     print(render(request, 'index.html').content)

#     return render(request, 'index.html')


# def product(request,id):
#     return render(request, 'product.html',{'pid':id})

# def article(request,aid):
#     return render(request, 'article.html', {'aid': aid})

# #ajax返回数据
# def jsonApi(request):
#     dictobj = {'title': '标题'}
#     a = HttpResponse(json.dumps(dictobj, ensure_ascii=False))
#     # 允许你的域名来获取我的数据
#     a['Access-Control-Allow-Origin'] = "*"

#     # 允许你携带Content-Type请求头
#     a['Access-Control-Allow-Headers'] = "Content-Type"
#     return a


# #GET/POST
# def methodApi(request):
#     # http = 'http://localhost:8000/methodApi?abc=123'
#     if request.method=='GET':
#         request.GET.get('abc')  # ===>123
#         request.POST.get('username')  # ===>admin
    
    
#     return HttpResponse('methodApi')


# #设置cookie
# def setcookie(request):
#     a = HttpResponse('12345')
#     # 设置cookies超过10秒失效，写法
#     a.set_cookie('isLogin', 'true', max_age=60)

#     # 从登录10秒后失效，写法
#     current_time = datetime.datetime.utcnow()
#     current_data = current_time + datetime.timedelta(seconds=10)
#     a.set_cookie('key', 'value', expires=current_data)
#     return a

# #获取cookie的写法
# def getcookie(request):
#     islogin = request.COOKIES.get('isLogin')
#     return HttpResponse(redirect('index'))



# #设置session
# def setsession(request):

#     request.session['username'] = '老王'
#     return HttpResponse('setsession')

# #获取seseion
# def getsession(request):
#     # request.session.get('username')
#     return HttpResponse(request.session['username'])

# # 设置文件上传


# def uploadfile(request):
#     if request.method == 'GET':
#         return render(request, 'upload.html')
#     else:
#         obj = request.FILES.get('files')
#         print(obj)
#         print(obj.__dict__)
#         # print(obj.name,obj.size)  #读取文件名称和大小，返回后台

#         f = open('./static/upload/'+obj.name, 'wb')
#         for chunk in obj.chunks():
#             f.write(chunk)
#         f.close()
#         return HttpResponse('图片上传成功')


# def pinglunList(request):
#     result =  pinglun.find()

#     resList = []
#     for item in result:
#         item['_id'] = str(item['_id'])
#         resList.append(item)
    
#     # print(resList)
#     jsonStr = json.dumps(resList,ensure_ascii=False)
#     # print(jsonStr)
    
#     a = HttpResponse(jsonStr)

#     a['Access-Control-Allow-Origin'] = "*"

#     # 允许你携带Content-Type请求头
#     a['Access-Control-Allow-Headers'] = "Content-Type"
#     return a


# def addContent(request):
#     print(request.GET.get('username'))
#     contentDict = {
#         'username': request.GET.get('username'),
#         'headerimg': request.GET.get('headerimg'),
#         'content': request.GET.get('content'),
#         'zanNum': request.GET.get('zanNum')
#     }
#     print(contentDict)

#     pinglun.insert(contentDict)




#     a = HttpResponse('ok')

#     a['Access-Control-Allow-Origin'] = "*"

#     # 允许你携带Content-Type请求头
#     a['Access-Control-Allow-Headers'] = "Content-Type"
#     return a


# def addzan(request):

#     print(request.GET.get('_id'))

#     _id = request.GET.get('_id')

#     # res1 = pinglun.find_one({'_id': _id})
#     res = pinglun.update({'_id': ObjectId(_id)}, {'$inc': {'zanNum': 1}})
    

#     print(res)

#     a = HttpResponse('ok')

#     a['Access-Control-Allow-Origin'] = "*"

#     # 允许你携带Content-Type请求头
#     a['Access-Control-Allow-Headers'] = "Content-Type"
#     return a


