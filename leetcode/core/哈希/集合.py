
# 集合的创建
# 方法1：使用花括号
set1 = {1, 2, 3, 4, 5}
# 方法2：使用set()函数
set2 = set([1, 2, 3, 4, 5])  # 从列表创建
set3 = set((1, 2, 3, 4, 5))  # 从元组创建
set4 = set("hello")  # 从字符串创建，会得到字符集合 {'h', 'e', 'l', 'o'}


# 集合的添加和删除
# 添加元素
set1.add(element)  # 添加单个元素
set1.update([1, 2, 3])  # 添加多个元素，参数可以是列表、元组、集合等

# 删除元素
set1.remove(element)  # 删除指定元素，如果元素不存在会报错
set1.discard(element)  # 删除指定元素，如果元素不存在不会报错
set1.pop()  # 随机删除并返回一个元素
set1.clear()  # 清空集合


# 集合的查询操作
# 检查元素是否存在
if element in set1:  # 推荐使用
    print("元素存在")

# 获取集合长度
length = len(set1)

# 集合的遍历
for element in set1:
    print(element)


# 集合的运算
# 交集
set3 = set1 & set2  # 使用 & 运算符
set3 = set1.intersection(set2)  # 使用intersection方法

# 并集
set3 = set1 | set2  # 使用 | 运算符
set3 = set1.union(set2)  # 使用union方法

# 差集
set3 = set1 - set2  # 使用 - 运算符，返回在set1中但不在set2中的元素
set3 = set1.difference(set2)  # 使用difference方法

# 对称差集（异或）
set3 = set1 ^ set2  # 使用 ^ 运算符，返回在set1或set2中，但不同时在两者中的元素
set3 = set1.symmetric_difference(set2)  # 使用symmetric_difference方法


# 集合的关系判断
# 判断子集
is_subset = set1.issubset(set2)  # 判断set1是否是set2的子集
is_subset = set1 <= set2  # 使用 <= 运算符

# 判断超集
is_superset = set1.issuperset(set2)  # 判断set1是否是set2的超集
is_superset = set1 >= set2  # 使用 >= 运算符

# 判断两个集合是否不相交
is_disjoint = set1.isdisjoint(set2)  # 判断两个集合是否没有共同元素


# 集合的拷贝
# 浅拷贝
set2 = set1.copy()
set2 = set(set1)

# 深拷贝
import copy
set2 = copy.deepcopy(set1)


# 集合推导式
# 创建新集合
set2 = {x for x in set1 if condition}

# 示例：将集合中的元素翻倍
set2 = {x*2 for x in set1}


# 集合的不可变版本：frozenset
# frozenset是不可变的集合，创建后不能修改
frozen_set = frozenset([1, 2, 3, 4, 5])
# frozenset支持所有集合运算，但不支持修改操作（add, remove等）


# 集合的应用场景
'''
1. 去重：快速去除列表中的重复元素
   unique_list = list(set(duplicate_list))

2. 成员检测：快速判断元素是否存在
   if element in set1:  # O(1)时间复杂度

3. 数学运算：交集、并集、差集等集合运算

4. 数据过滤：使用集合推导式进行数据过滤
   filtered_set = {x for x in set1 if x > 0}

5. 关系判断：判断集合间的包含关系
   if set1.issubset(set2):
       print("set1是set2的子集")
''' 