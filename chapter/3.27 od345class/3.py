# hash table & hash set
# 字典实现hash 键和值对应
# 初始化空字典


d1 = dict()
# 初始化键值对
d2 = {'a': 1, 'b': 2, 'c': 3}# 字典不能索引 通过计算得到键对应的值
print(d2['b'])# 用[]访问键对应的值
# 字典修改
d2['a'] = 4
print(d2['a'])
# 字典添加键值对
d2['d'] = 5
print(d2['d'])
print(d2)
# 字典删除键值对
del d2['d']
print(d2)
"""
都是通过键修改值，因为字典是要用键来找值的
字典的键不能重复，所以修改值的时候如果键不存在，则会自动添加键值对
"""

# 只输出键 key
print(list(d2.keys()))# 把结果生成成一个列表
# 只输出值 value
print(d2.values())
# 输出键值对 item项目
print(d2.items())

# 字典长度
print("length",len(d2))

# 字典遍历
for key in d2:# for 变量 in 字典 for循环的用法
    print("item",key, d2[key])

    print("元组形式")
for item in d2.items():# for 变量 in 字典.items() for循环的用法
    print("item2",item)

print("双变量遍历")# ***python的代码结构因为for没有{}了所以要严格观察缩进问题否则会归到for循环里
for key,value in d2.items():# for 变量1,变量2 in 字典.items() for循环的用法
    print("item3",key,value)

# 只遍历键
for key2 in d2.keys(): # 出现中文的字符时可能报错或警告
    print("key2",key2)

# 只遍历值
for value in d2.values():
    print("value",value)
# 输出不一定有序


# 字典合并
d3 = {'e': 6, 'f': 7}
d2.update(d3)# 加载d3字典的所有键值对到d2字典中
print(d2)

# 字典get（）方法
print(d2.get('k',"不存在"))# 输出键k对应的值，如果键不存在则返回不存在***给不存在的键增加了返回值

# 不知道键是否存在的情况下查删改
d2["k"] = d2.get("k",9) + 1# 给k键加1，如果k不存在则给它赋值9
print('k',d2["k"])

"""
这里调用的都是dict字典类对象的成员函数，用对象名.函数名直接调用
很多函数能直接调用是因为基本库里已经定义好了，在一开始就会链接到文件里，就像c和c++一样一开始要说明头文件，然后才能调用函数
头文件里就包括了写好的可以直接调用的函数，那么此时在代码命名中就不能出现与已经由头文件定义的函数重名的变量或函数了
"""

"""
api接口，也就是自带的能直接使用的函数
比如print()函数，它是python自带的，不需要自己写，直接调用就行
"""


# ***特别好用的api 计数器类Counter（）一种特殊的哈希表，可以统计元素出现的次数
# Counter()继承了dict（）,所以它也有的所有方法，就是dict（）的所有函数Counter（）也能用

# 要调用Counter()函数需要先说明Counter()函数所在的内置库

from collections import Counter # 导入Counter()函数所在的内置库collections
cnt = Counter("aabbcc")
print('cnt',cnt) # 输出Counter({'a': 2, 'b': 2, 'c': 2})
cnt2 = Counter([1,2,3,4,1,1,1,2,3]) # 也可以统计列表,生成结果为一个字典，键值为统计的值，值为出现次数
print("cnt2",sorted(list(cnt2.values())))# sorted()函数可以对字典的值进行排序，然后输出成列表
"""
指到Counter（）可以转到实现看Counter()源码
"""
# 在用到一些函数的时候要先链接内置库像是要用到inf()函数，那么就要先链接inf（）所在的内置库，然后才能调用inf()函数
from math import inf # import输入，从math库导入inf()函数 没被用到指定函数的时候都是显示灰色
print(inf) # 输出inf

# 字典中的键可以是任何数据类型，键一定是不可变的数据类型，因为最后要通过键来查找值，所以键不能修改，只能添加或删除 可hashable可以用作哈希查找
# 字典的键不能重复因为要保证一一对应否则会出现冲突查不到值，所以修改值的时候如果键不存在，则会自动添加键值对

# 在一定情况下可以用列表代替哈希表，在键值规律的情况下

# hash set 哈希集合 哈希表就是哈希字典 hash dict用来存键-值对用于查找 哈希集合只存数据集合是无序且元素各不相同的但是哈希集合要可哈希

# 初始化空集合
s1 = set() # 初始化都是类似的
s2 = {1,2,3} # 集合用花括号
s3 = set([1, 2, 3, 4, 5]) # 列表转集合
print("s3:",s3)

# 集合函数 add() remove() 集合是不可修改的数据类型 只能通过删除和插入或者转列表进行修改

#集合转列表 可以对列表去重 因为集合不允许有重复元素
l3 = [1,2,3,3]
s3 =  set(l3)
l3 = list(s3)
l3.sort()
print("l3:",l3)

