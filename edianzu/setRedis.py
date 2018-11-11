import redis    # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
import time

# host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# pipe = r.pipeline()

#字符串增删改查

# #设置
# r.set('gender', 'male')     # key是"gender" value是"male" 将键值对存入redis缓存
# r.set('fruit','banana')

# #获取
# print(r.get('gender'))      # gender 取出键male对应的值


# set(name, value, ex=None, px=None, nx=False, xx=False)

# 在Redis中设置值，默认，不存在则创建，存在则修改
# 参数：
# ex，过期时间（秒）
# px，过期时间（毫秒）
# nx，如果设置为True，则只有name不存在时，当前set操作才执行（新建）
# xx，如果设置为True，则只有name存在时，当前set操作才执行（更新）



# r.set('gender', 'female', ex=3)    # key是"food" value是"mutton" 将键值对存入redis缓存
# print(r.get('gender'))
# time.sleep(4)
# print(r.get('gender'))

# # print(r.get('food'))  # mutton 取出键food对应的值



# 哈希类型设置

# r.hset('字典名','key','value')
# r.hset('abc','username','admin')
# r.hset('abc', 'list', ['pingguo','香蕉'])

# r.hget('字典名', 'key')
# print(r.hget('abc', 'username'))


# #缓存用户信息
# r.hset('users','userid','json格式数据保存用户相关信息')
# #缓存页面内容
# r.hset('htmls','articleid','<html><h1>HELLOWORLD</h1></html>')
# r.hget('htmls','articleid')
# 获取字典的所有key值
# print(r.hkeys('abc'))
# print('-------->')
# r.hmset('abc',{'img':'tt','content':'666'})
# print(r.hmget('abc','username','list'))
# print(type(r.hgetall('abc')['list']))
# r.hgetall('字典名')
# print(r.hgetall('abc'))

# 当字典里的key值不存在时，则新建一个，存在则不执行
# r.hsetnx('abc','username','cpeng')

# print(r.hgetall('abc'))

# r.hlen("字典名") 获取哈希类型的数据长度
# print(r.hlen("abc"))


# 获取name对应的hash中所有的key的值
# print(r.hkeys("abc"))
# 获取name对应的hash中所有的value的值
# print(r.hvals("abc"))

# hexists(name, key)检查name对应的hash是否存在当前传入的key
# print(r.hexists("abc", "list"))  # True 存在
# print(r.hexists("abc", "k1"))  # False 不存在


# 删除键值对
# hdel(name, *keys) 
# 将name对应的hash中指定key的键值对删除

# print(r.hgetall("abc"))
# r.hset("abc", "k2", "v222")   # 修改已有的key k2
# # r.hset("abc", "k11", "v1")   # 新增键值对 k11
# r.hdel("abc", "k2")    # 删除一个键值对
# print(r.hgetall("abc"))

# 自增自减整数(将key对应的value--整数 自增1或者2，或者别的整数 负数就是自减)
# hincrby(name, key, amount=1)
# 自增name对应的hash中的指定key的值，不存在则创建key = amount
# 参数：
# name，redis中的name
# key， hash对应的key
# amount，自增数（整数）

# r.hset("abc", "readnum", 0)
# r.hincrby("abc", "readnum", amount=1)
# print(r.get('abc'))

# print(r.hgetall("abc"))

# r.hincrby("bck", "k4", amount=1)  # 不存在的话，就创建出来 value默认就是1     


# print(r.hgetall("abc"))


# 在Redis中设置值，默认，不存在则创建，存在则修改
# 参数：
# ex，过期时间（秒）
# px，过期时间（毫秒）
# nx，如果设置为True，则只有name不存在时，当前set操作才执行（新建）
# xx，如果设置为True，则只有name存在时，当前set操作才执行（更新）



# 双向操作列表


#从右往左依次插入
# r.lpush("list1", 1, 2, 3)  #[33,22,11]
# 
# r.rpush("list2", 11, 22, 33)  #[11,22,33]


# print(r.lrange('list1',0,-1))
# print(r.lrange('list2',0,-1))

# print(r.llen('list1'))          #获取列表长度
# print(r.lrange('list1', 0, -1)) #获取全部数据
# print(r.lrange('list1',0,3))    #获取从 0到3 共4个值
# r.lpushx("list10", 10)          # 往已经有的name的列表的左边添加元素，没有的话无法创建 有个x
# r.linsert("list1", "before", "22", "15")   # 往列表中左边第一个出现的元素"22"前插入元素"15"


# r.rpush("list2", 11, 22, 33)  # 方向向右，从左往右依次插入
# print(r.lrange("list2", 0, -1))  # 切片取出值，范围是索引号0-3

# print(r.llen("list2"))  # 列表长度


# 往已经有的name的列表的左边添加元素，没有的话无法创建
# lpushx(name, value)

# 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边
# 更多：

# r.lpushx("list10", 10)   # 这里list10不存在
# print(r.llen("list10"))  # 0
# print(r.lrange("list10", 0, -1))  # []
# r.lpushx("list2", 77)   # 这里"list2"之前已经存在，往列表最左边添加一个元素，一次只能添加一个
# print(r.llen("list2"))  # 列表长度
# print(r.lrange("list2", 0, -1))  # 切片取出值，范围是索引号0到-1(最后一个元素
# # 往已经有的name的列表的右边添加元素，没有的话无法创建

# r.rpushx("list2", 99)   # 这里"foo_list1"之前已经存在，往列表最右边添加一个元素，一次只能添加一个
# print(r.llen("list2"))  # 列表长度
# print(r.lrange("list2", 0, -1))  # 切片取出值，范围是索引号0到-1(最后一个元素)
# 新增（固定索引号位置插入元素）
# r.linsert(name, where, refvalue, value))
#     在name对应的列表的某一个值前或后插入一个新值
#     参数：
#     name，redis的name
#     where，before或after
#     refvalue，标杆值，即：在它前后插入数据
#     value，要插入的数据

# r.linsert("list1", "before", "22", "15")   # 往列表中左边第一个出现的元素"22"前插入元素"15"
# print(r.lrange("list2", 0, -1))   # 切片取出值，范围是索引号0-最后一个元素
# 修改（指定索引号进行修改）
#     r.lset(name, index, value)
#     对name对应的list中的某一个索引位置重新赋值
#     参数：
#     name，redis的name
#     index，list的索引位置
#     value，要设置的值
# r.lset("list2", 0, -11)    # 把索引号是0的元素修改成-11
# print(r.lrange("list2", 0, -1))
# 删除（指定值进行删除）
# r.lrem(name, value, num)
# 在name对应的list中删除指定的值
#     参数：
#     name，redis的name
#     value，要删除的值
#     num， num=0，删除列表中所有的指定值；
#     num=2, 从前到后，删除2个； num=1, 从前到后，删除左边第1个
#     num=-2, 从后向前，删除2个

# r.lrem('list2',-11,num=1)

# r.lrem("list2", "11", 1)    # 将列表中左边第一次出现的"11"删除
# print(r.lrange("list2", 0, -1))
# r.lrem("list2", "99", -1)    # 将列表中右边第一次出现的"99"删除
# print(r.lrange("list2", 0, -1))
# r.lrem("list2", "22", 0)    # 将列表中所有的"22"删除
# print(r.lrange("list2", 0, -1))
# 删除并返回
#     lpop(name)
#     在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
#     更多：
#     rpop(name) 表示从右向左操作

# print(r.lpop("list2"))    # 删除列表最左边的元素，并且返回删除的元素
# print(r.lrange("list2", 0, -1))
# r.rpop("list2")    # 删除列表最右边的元素，并且返回删除的元素
# print(r.lrange("list2", 0, -1))
# 删除索引之外的值
#     ltrim(name, start, end)
#     在name对应的列表中移除没有在start-end索引之间的值
#     参数：
#     name，redis的name
#     start，索引的起始位置
#     end，索引结束位置
# r.ltrim("list1", 0, 2)    # 删除索引号是0-2之外的元素，值保留索引号是0-2的元素
# print(r.lrange("list2", 0, -1))

# 取值（根据索引号取值）
#     lindex(name, index)
#     在name对应的列表中根据索引获取列表元素
# print(r.lindex("list1", 1))  # 取出索引号是1的值



# # 移动 元素从一个列表移动到另外一个列表
# #     rpoplpush(src, dst)
# #     从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
# #     参数：
# #     src，要取数据的列表的name
# #     dst，要添加数据的列表的name

# r.rpoplpush("list1", "list2")
# print(r.lrange("list2", 0, -1))

# 移动 元素从一个列表移动到另外一个列表 可以设置超时
#     brpoplpush(src, dst, timeout = 0)
#     从一个列表的右侧移除一个元素并将其添加到另一个列表的左侧
#     参数：
#     src，取出并要移除元素的列表对应的name
#     dst，要插入元素的列表对应的name
#     timeout，当src对应的列表中没有数据时，阻塞等待其有数据的超时时间（秒），0 表示永远阻塞

# r.brpoplpush("list1", "list2", timeout = 2)
# print(r.lrange("list2", 0, -1))

# # 一次移除多个列表
# #     blpop(keys, timeout)
# #     将多个列表排列，按照从左到右去pop对应列表的元素
# #     参数：
# #     keys，redis的name的集合
# #     timeout，超时时间，当元素所有列表的元素获取完之后，阻塞等待列表内有数据的时间（秒）, 0 表示永远阻塞
# #     更多：
# #     r.brpop(keys, timeout) 同blpop，将多个列表排列, 按照从右像左去移除各个列表内的元素

# r.lpush("list10", 3, 4, 5)
# r.lpush("list11", 3, 4, 5)

# r.blpop(["list10", "list11"], timeout = 2)
# print(r.lrange("list10", 0, -1), r.lrange("list11", 0, -1))

# # 自定义增量迭代
# #     由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要：

# #     获取name对应的所有列表
# #     循环列表
# #     但是，如果列表非常大，那么就有可能在第一步时就将程序的内容撑爆，所有有必要自定义一个增量迭代的功能：

# def list_iter(name):
#     """
#     自定义redis列表增量迭代
#     :param name: redis中的name，即：迭代name对应的列表
#     :return: yield 返回 列表元素
#     """
#     list_count=r.llen(name)
#     for index in range(list_count):
#         yield r.lindex(name, index)

#     # 使用
# for item in list_iter('list2'):  # 遍历这个列表
#     print(item)


# redis基本命令 set

# 1.新增
# sadd(name, values)
# name对应的集合中添加元素

# r.sadd("set1", 33, 44, 55, 66)  # 往集合中添加元素
# print(r.scard("set1"))  # 集合的长度是4
# print(r.smembers("set1"))   # 获取集合中所有的成员
# 2.获取元素个数 类似于len
# scard(name)
# 获取name对应的集合中元素个数
# r.zadd('set2',12)
# print(r.scard("set1"))  # 集合的长度是4
# 3.获取集合中所有的成员
# smembers(name)
# 获取name对应的集合的所有成员

# print(r.smembers("set1"))   # 获取集合中所有的成员
# 获取集合中所有的成员--元组形式
# sscan(name, cursor=0, match=None, count=None)

# print(r.sscan("set1"))
# 获取集合中所有的成员--迭代器的方式
# sscan_iter(name, match=None, count=None)
# 同字符串的操作，用于增量迭代分批获取元素，避免内存消耗太大

# for i in r.sscan_iter("set1"):
#     print(i)
# 4.差集
# sdiff(keys, *args)
# 在第一个name对应的集合中且不在其他name对应的集合的元素集合

# r.sadd("set2", 11, 22, 33)
# print(r.smembers("set1"))   # 获取集合中所有的成员
# print(r.smembers("set2"))
# print(r.sdiff("set1", "set2"))   # 在集合set1但是不在集合set2中
# print(r.sdiff("set2", "set1"))   # 在集合set2但是不在集合set1中
# 5.差集--差集存在一个新的集合中
# sdiffstore(dest, keys, *args)
# 获取第一个name对应的集合中且不在其他name对应的集合，再将其新加入到dest对应的集合中

# r.sdiffstore("set3", "set1", "set2")    # 在集合set1但是不在集合set2中
# print(r.smembers("set3"))   # 获取集合3中所有的成员
# 6.交集
# sinter(keys, *args)
# 获取多一个name对应集合的交集

# print(r.sinter("set1", "set2"))  # 取2个集合的交集
# 7.交集--交集存在一个新的集合中
# sinterstore(dest, keys, *args)
# 获取多一个name对应集合的并集，再将其加入到dest对应的集合中

# print(r.sinterstore("set3", "set1", "set2"))  # 取2个集合的交集
# print(r.smembers("set3"))
# 并集
# sunion(keys, *args)
# 获取多个name对应的集合的并集

# print(r.sunion("set1", "set2"))  # 取2个集合的并集
# 并集--并集存在一个新的集合
# sunionstore(dest, keys, *args)
# 获取多一个name对应的集合的并集，并将结果保存到dest对应的集合中

# print(r.sunionstore("set3", "set1", "set2"))  # 取2个集合的并集
# print(r.smembers("set3"))
# 8.判断是否是集合的成员 类似in
# sismember(name, value)
# 检查value是否是name对应的集合的成员，结果为True和False

# print(r.sismember("set1", 33))  # 33是集合的成员
# print(r.sismember("set1", 23))  # 23不是集合的成员
# 9.移动
# smove(src, dst, value)
# 将某个成员从一个集合中移动到另外一个集合

# r.smove("set1", "set2", 44)
# print(r.smembers("set1"))
# print(r.smembers("set2"))
# 10.删除--随机删除并且返回被删除值
# spop(name)
# 从集合移除一个成员，并将其返回, 说明一下，集合是无序的，所有是随机删除的

# print(r.spop("set2"))   # 这个删除的值是随机删除的，集合是无序的
# print(r.smembers("set2"))
# 11.删除--指定值删除
# srem(name, values)
# 在name对应的集合中删除某些值

# print(r.srem("set2", 11))   # 从集合中删除指定值 11
# print(r.smembers("set2"))






# redis基本命令 有序set

# Set操作，Set集合就是不允许重复的列表，本身是无序的
# 有序集合，在集合的基础上，为每元素排序；元素的排序需要根据另外一个值来进行比较，
# 所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。

# 1.新增
# zadd(name, *args, **kwargs)
# 在name对应的有序集合中添加元素
# 如：

# import redis
# import time

# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
# r = redis.Redis(connection_pool=pool)

# r.zadd("zset1", n1=11, n2=22)
# r.zadd("zset2", 'm1', 22, 'm2', 44,'m1',22)
# print(r.zcard("zset1"))  # 集合长度
# print(r.zcard("zset2"))  # 集合长度
# print(r.zrange("zset1", 0, -1))   # 获取有序集合中所有元素
# print(r.zrange("zset2", 0, -1, withscores=True))   # 获取有序集合中所有元素和分数
# 2.获取有序集合元素个数 类似于len
# zcard(name)
# 获取name对应的有序集合元素的数量

# print(r.zcard("zset1"))  # 集合长度
# 3.获取有序集合的所有元素
# r.zrange(name, start, end, desc=False, withscores=False, score_cast_func=float)
# 按照索引范围获取name对应的有序集合的元素
# 参数：
# name，redis的name
# start，有序集合索引起始位置（非分数）
# end，有序集合索引结束位置（非分数）
# desc，排序规则，默认按照分数从小到大排序
# withscores，是否获取元素的分数，默认只获取元素的值
# score_cast_func，对分数进行数据转换的函数

# 3-1 从大到小排序(同zrange，集合是从大到小排序的)
# zrevrange(name, start, end, withscores=False, score_cast_func=float)

# print(r.zrevrange("zset1", 0, -1))    # 只获取元素，不显示分数
# print(r.zrevrange("zset1", 0, -1, withscores=True))  # 获取有序集合中所有元素和分数,分数倒序
# 3-2 按照分数范围获取name对应的有序集合的元素
# zrangebyscore(name, min, max, start=None, num=None,
#               withscores=False, score_cast_func=float)

# for i in range(1, 30):
#    element = 'n' + str(i)
#    r.zadd("zset3", element, i)
# print(r.zrangebyscore("zset3", 15, 25))  # 在分数是15-25之间，取出符合条件的元素
# # 在分数是12-22之间，取出符合条件的元素（带分数）
# print(r.zrangebyscore("zset3", 12, 22, withscores=True))
# 3-3 按照分数范围获取有序集合的元素并排序（默认从大到小排序）
# zrevrangebyscore(name, max, min, start=None, num=None,
#                  withscores=False, score_cast_func=float)

# # 在分数是22-11之间，取出符合条件的元素 按照分数倒序
# print(r.zrevrangebyscore("zset3", 22, 11, withscores=True))
# 3-4 获取所有元素--默认按照分数顺序排序
# zscan(name, cursor=0, match=None, count=None, score_cast_func=float)

# print(r.zscan("zset3"))
# 3-5 获取所有元素--迭代器
# zscan_iter(name, match=None, count=None, score_cast_func=float)

# for i in r.zscan_iter("zset2"):  # 遍历迭代器
#     print(i)
# 4.zcount(name, min, max)
# 获取name对应的有序集合中分数 在[min, max] 之间的个数

# print(r.zrange("zset3", 0, -1, withscores=True))
# print(r.zcount("zset3", 11, 22))
# 5.自增
# zincrby(name, value, amount)
# 自增name对应的有序集合的 name 对应的分数

# r.zincrby("zset3", "n2", amount=2)    # 每次将n2的分数自增2
# print(r.zrange("zset3", 0, -1, withscores=True))
# 6.获取值的索引号
# zrank(name, value)
# 获取某个值在 name对应的有序集合中的索引（从 0 开始）
# 更多：
# zrevrank(name, value)，从大到小排序

# print(r.zrank("zset3", "n1"))   # n1的索引号是0 这里按照分数顺序（从小到大）
# print(r.zrank("zset3", "n6"))   # n6的索引号是1

# print(r.zrevrank("zset3", "n1"))    # n1的索引号是29 这里安照分数倒序（从大到小）
# 7.删除--指定值删除
# zrem(name, values)
# 删除name对应的有序集合中值是values的成员

# r.zrem("zset3", "n3")   # 删除有序集合中的元素n3 删除单个
# print(r.zrange("zset3", 0, -1))
# 8.删除--根据排行范围删除，按照索引号来删除
# zremrangebyrank(name, min, max)
# 根据排行范围删除

# r.zremrangebyrank("zset3", 0, 1)  # 删除有序集合中的索引号是0, 1的元素
# print(r.zrange("zset3", 0, -1))
# 9.删除--根据分数范围删除
# zremrangebyscore(name, min, max)
# 根据分数范围删除

# r.zremrangebyscore("zset3", 11, 22)   # 删除有序集合中的分数是11-22的元素
# print(r.zrange("zset3", 0, -1))
# 10.获取值对应的分数
# zscore(name, value)
# 获取name对应有序集合中 value 对应的分数

# print(r.zscore("zset3", "n27"))   # 获取元素n27对应的分数27




# 8、其他常用操作

# 1.删除
# delete(*names)
# 根据删除redis中的任意数据类型（string、hash、list、set、有序set）

# r.delete("gender")  # 删除key为gender的键值对

# 2.检查名字是否存在
# print(r.exists('username'))
# 检测redis的name是否存在，存在就是True，False 不存在

# print(r.exists("zset1"))
# 3.模糊匹配
# keys(pattern='')
# 根据模型获取redis的name
# 更多：
# KEYS * 匹配数据库中所有 key 。
# KEYS h?llo 匹配 hello ， hallo 和 hxllo 等。
# KEYS hllo 匹配 hllo 和 heeeeello 等。
# KEYS h[ae]llo 匹配 hello 和 hallo ，但不匹配 hillo

# print(r.keys("user*"))
# 4.设置超时时间
# expire(name, time)
# 为某个redis的某个name设置超时时间
# r.expire('abc',time=3)
# r.lpush("list5", 11, 22)
# r.expire("list5", time=3)
# print(r.lrange("list5", 0, -1))
# time.sleep(3)
# print(r.lrange("list5", 0, -1))
# 5.重命名
# rename(src, dst)
# 对redis的name重命名

# r.lpush("list5", 11, 22)
# r.rename("list5", "list5-1")
# 6.随机获取name
# randomkey()
# 随机获取一个redis的name（不删除）

# print(r.randomkey())
# 7.获取类型
# type(name)
# 获取name对应值的类型

# print(r.type("list1"))
# print(r.type("hash2"))
# 8.查看所有元素
# scan(cursor=0, match=None, count=None)

# print(r.hscan("hash2"))
# print(r.sscan("set3"))
# print(r.zscan("zset2"))
# print(r.getrange("foo1", 0, -1))
# print(r.lrange("list2", 0, -1))
# print(r.smembers("set3"))
# print(r.zrange("zset3", 0, -1))
# print(r.hgetall("hash1"))


# 9.查看所有元素--迭代器
# scan_iter(match=None, count=None)

# for i in r.hscan_iter("hash1"):
#     print(i)

# for i in r.sscan_iter("set3"):
#     print(i)

# for i in r.zscan_iter("zset3"):
#     print(i)
# other 方法

# print(r.get('name'))    # 查询key为name的值
# r.delete("gender")  # 删除key为gender的键值对
# print(r.keys())  # 查询所有的Key
# print(r.dbsize())   # 当前redis包含多少条数据
# r.save()    # 执行"检查点"操作，将数据写回磁盘。保存时阻塞
# r.flushdb()        # 清空r中的所有数据




# 管道（pipeline）
# 原子性/提升效率/速度
# redis默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
# 如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。

# 管道（pipeline）是redis在提供单个请求中缓冲多条服务器命令的基类的子类。它通过减少服务器-客户端之间反复的TCP数据库包，从而大大提高了执行批量命令的功能。

# import redis
# import time

# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
# r = redis.Redis(connection_pool=pool)


# pipe = r.pipeline()  # 创建一个管道

# pipe.set('name', 'jack')
# pipe.set('role', 'sb')
# pipe.sadd('faz', 'baz')
# pipe.incr('num')    # 如果num不存在则vaule为1，如果存在，则value自增1
# pipe.execute()

# pipe.set('hello', 'redis').sadd('faz', 'baz').incr('num').execute()


# print(r.get("name"))
# print(r.get("role"))
# print(r.get("num"))
# # 管道的命令可以写在一起，如：


# print(r.get("name"))
# print(r.get("role"))
# print(r.get("num"))




