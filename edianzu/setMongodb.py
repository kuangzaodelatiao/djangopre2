from pymongo import MongoClient



#连接
conn = MongoClient('192.168.8.112', 27017)

#进入数据库
db = conn.edianzu  #连接mydb数据库，没有则自动创建

#进入集合
# pinglun = db.pinglun  # 使用test_set集合，没有则自动创建
# goods_img = db.goods_img
# goods_img.insert({'img_list':['https://edzimg.edianzu.com/product/2018/09/b05410dbe885cf45fb56dea5102bb6ac.jpg?x-oss-process=image/resize,m_fill,h_380,w_380']})
















# img_list

# pinglun.insert({'name':'hah'})


#插入数据（insert插入一个列表多条数据不用遍历，效率高， save需要遍历列表，一个个插入）

#1/insert方式
# pinglunDict = {
#     'username':'小红',
#     'headerimg': 'https://tvax3.sinaimg.cn/crop.0.0.750.750.180/006758Pyly8fg6x9s2jhtj30ku0ku74m.jpg',
#     'content': '王思聪吃热狗又出周边了！这次是捣蒜神器，想要[doge] ​​​​',
#     'contentimg': ['https://wx4.sinaimg.cn/mw690/006758Pyly1fx0etbf8f0j30yi1hwwwl.jpg', 'https://wx3.sinaimg.cn/mw690/006758Pyly1fx0etbpdnbj30k00qote5.jpg', 'https://wx1.sinaimg.cn/mw690/006758Pyly1fx0etbwqp2j30k00qo796.jpg'],
#     'zanNum':0

# }

# # pinglun.insert(pinglunDict)

# #2/save方式
# # pinglun.save(pinglunDict)

# #添加多条数据到集合中
# pinglunList = [
#     {
#         'username': '小李',
#         'headerimg': 'https://tvax3.sinaimg.cn/crop.0.0.750.750.180/006758Pyly8fg6x9s2jhtj30ku0ku74m.jpg',
#         'content': '王思聪吃热狗又出周边了！这次是捣蒜神器，想要[doge] ​​​​',
#         'contentimg': ['https://wx4.sinaimg.cn/mw690/006758Pyly1fx0etbf8f0j30yi1hwwwl.jpg', 'https://wx3.sinaimg.cn/mw690/006758Pyly1fx0etbpdnbj30k00qote5.jpg', 'https://wx1.sinaimg.cn/mw690/006758Pyly1fx0etbwqp2j30k00qo796.jpg'],
#         'zanNum':0

#     },
#     {
#         'username': '小黑',
#         'headerimg': 'https://tvax3.sinaimg.cn/crop.0.0.750.750.180/006758Pyly8fg6x9s2jhtj30ku0ku74m.jpg',
#         'content': '王思聪吃热狗又出周边了！这次是捣蒜神器，想要[doge] ​​​​',
#         'contentimg': ['https://wx4.sinaimg.cn/mw690/006758Pyly1fx0etbf8f0j30yi1hwwwl.jpg', 'https://wx3.sinaimg.cn/mw690/006758Pyly1fx0etbpdnbj30k00qote5.jpg', 'https://wx1.sinaimg.cn/mw690/006758Pyly1fx0etbwqp2j30k00qo796.jpg'],
#         'zanNum':0

#     },
#     {
#         'username': '小花',
#         'headerimg': 'https://tvax3.sinaimg.cn/crop.0.0.750.750.180/006758Pyly8fg6x9s2jhtj30ku0ku74m.jpg',
#         'content': '王思聪吃热狗又出周边了！这次是捣蒜神器，想要[doge] ​​​​',
#         'contentimg': ['https://wx4.sinaimg.cn/mw690/006758Pyly1fx0etbf8f0j30yi1hwwwl.jpg', 'https://wx3.sinaimg.cn/mw690/006758Pyly1fx0etbpdnbj30k00qote5.jpg', 'https://wx1.sinaimg.cn/mw690/006758Pyly1fx0etbwqp2j30k00qo796.jpg'],
#         'zanNum':0

#     }
# ]
# # pinglun.insert(pinglunList)
#或
# for item in pinglunList:
#     pinglun.save(item)


#更新数据
# pinglun.update({'username':'小花'},{'$set':{'zanNum':1}},multi=True,upsert=True)

# my_set.update(
#     < query > ,  # 查询条件
#     < update > ,  # update的对象和一些更新的操作符
#     {
#         upsert: < boolean >,  # 如果不存在update的记录，是否插入
#         multi: < boolean > ,  # 可选，mongodb 默认是false,只更新找到的第一条记录
#     }
# )
# 把上面插入的数据内的age改为20




# #删除某个文档
# pinglun.remove({查找语句})
# pinglun.remove({'username': '小李'})



# #删除整条记录
# id = my_set.find_one({"name": "zhangsan"})["_id"]

#删除name=lisi的某个id的记录
# pinglunimg = pinglun.find_one({'username':'小黑'})['_id']
# print(pinglun.remove(pinglunimg))

# #删除集合里的所有记录
# pinglun.remove()


#查找具体某条信息
#语法：find_one({条件key:条件value})

# result = pinglun.find_one({'username':'小黑'})
# result = pinglun.find({'username':'小黑','zanNum':0})
# result = pinglun.find().count()
# print(result)






# #查询,大于$gt，大于等于$gte,小于$lt，小于等于$lte,不等于$ne
# result = pinglun.find_one({
#     'zanNum':{'$ne':0}
# })
# print(result)


# pinglun.update({'username':'小花'},{'$set':{'zanNum':1}})
#在原基础上进行增加
# pinglun.update({'username': '小花'}, {'$inc': {'zanNum': 1}})

# #and条件，》db.col.find({key1:value1, key2:value2}).
# result = pinglun.find_one({
#     'zanNum': {'$lt': 50},
#     'username':'小花'
# })
# print(result)

# #OR 条件

# result = pinglun.find_one({
#     '$or':[
#         {'zanNum':0},
#         {'zanNum':2}
#     ]
# })
# print(result)


# # >db.col.find(
# #     {$or: [
# #         {key1: value1}, {key2: value2}
# #     ]
# #     }
# # )

# #limit()方法接受一个数字参数，该参数指定从MongoDB中读取的记录条数。
# #skip()方法来跳过指定数量的数据，skip方法同样接受一个数字参数作为跳过的记录条数。


# # count统计数目


# #sort排序
# #pymongo.ASCENDING      1
# #pymongo.DESCENDING    -1
# # find().sort((("age", pymongo.ASCENDING), ("high", pymongo.ASCENDING)))

# #正则表达式查询
# # find({'name': {'$regex': r'.*wei.*'}})


