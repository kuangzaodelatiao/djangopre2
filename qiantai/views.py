from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from edianzu.setMongodb import goods_img
from goods.models import Category,Goods 
# Create your views here.
def index(request):
    return HttpResponse('qiantaiok')



@csrf_exempt
def index(request):
    # type = Category.objects.filter(is_root=1)
    # for t in type:
    #     print(t)
    #     print(t.children)



    # result =  HttpResponse('ok')
    # result['Access-Control-Allow-Origin'] = '*'
    # result['Access-Control-Allow-Headers'] = '*'
    return render(request,'qiantai_index.html')

