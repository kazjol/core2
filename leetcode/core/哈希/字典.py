# 字典的插入和更新
# 方法1：直接赋值
dict[key] = value
# 方法2：使用update方法
dict.update({key: value})  # 更新单个键值对
dict.update({key1: value1, key2: value2})  # 更新多个键值对
# 方法3：使用setdefault（如果键不存在才插入）
dict.setdefault(key, default_value)


# 字典的删除
# 方法1：del语句
del dict[key]  # 删除指定键值对
# 方法2：pop方法（返回被删除的值）
value = dict.pop(key)  # 删除并返回对应的值
value = dict.pop(key, default)  # 如果键不存在，返回default值
# 方法3：popitem方法（删除并返回最后一个键值对）
key, value = dict.popitem()
# 方法4：clear方法（清空整个字典）
dict.clear()


# 关键字对比
# 检查键是否存在 字典是哈希的可供直接查找的是键 对值的查找要先调函数
if key in dict:  # 推荐使用
# 获取所有键
keys = dict.keys()  # 返回所有键的视图
keys_list = list(dict.keys())  # 转换为列表
# 获取所有值
values = dict.values()  # 返回所有值的视图
values_list = list(dict.values())  # 转换为列表
# 获取所有键值对
items = dict.items()  # 返回所有键值对的视图
items_list = list(dict.items())  # 转换为列表


# 值的操作
# 获取值
value = dict[key]  # 如果键不存在会报错
value = dict.get(key)  # 如果键不存在返回None
value = dict.get(key, default)  # 如果键不存在返回default值
# 遍历字典
'''
    字典的遍历 字典是哈希的 以键匹配实现查找的 可供查找的是键
'''
for key in dict:  # 遍历键  
    print(key, dict[key])

for key, value in dict.items():  # 遍历键值对
    print(key, value)

for value in dict.values():  # 只遍历值
    print(value)

# 字典的合并
# 方法1：使用update
dict1.update(dict2)
# 方法2：使用 | 运算符（Python 3.9+）
dict3 = dict1 | dict2
# 方法3：使用字典推导式
dict3 = {**dict1, **dict2}

# 字典的拷贝
# 浅拷贝
dict2 = dict1.copy()
dict2 = dict(dict1)

# 深拷贝
import copy
dict2 = copy.deepcopy(dict1)


# 字典的排序
# 按键排序
sorted_dict = dict(sorted(dict.items())) # 先转字典的键值对为元组 然后用lambda匿名函数指定输入参数
# 按值排序
sorted_dict = dict(sorted(dict.items(), key=lambda x: x[1]))
# 按值降序排序
sorted_dict = dict(sorted(dict.items(), key=lambda x: x[1], reverse=True))

# 字典推导式
# 创建新字典
dict2 = {k: v for k, v in dict1.items() if condition}

# 示例：将值翻倍
dict2 = {k: v*2 for k, v in dict1.items()}


