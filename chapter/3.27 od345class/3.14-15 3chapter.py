list1 = []
list2 = list()
stu = ['a','b','c']
print(list1,list2,stu,sep=',,')
print(stu[1])#列表可以视为数组访问下标也是从0开始
print(stu[-1])#复数索引访问倒数第一个元素
'''
变量命名要易读，遇到不会的单词可以用拼音例如 卖出->mai4chu1数字是声调
'''


list3 = [1,2,3]#这里的list可以理解为一个类里面包含的成员函数有append insert这些可以通过.调用
it = 'ok'

list3.append(it)#app到end
print(list3)

list3.insert(4,'nok')#insert（添加的位置，内容）
print(list3)

year1 = [2000,2001,2002]
year2 = [2003,2004,1999,1847]

year1.extend(year2)#将year2的内容添加到year1的尾部
print(year1)

year1.append(year2)
print(year1)

'''
year1.remove(2001)#删除元素在调用remove()方法时，只会删除从左到右第一个出现的值为"xiaohong"的元素。在连续调用了两次students.remove("xiaohong")之后，才能将列表中第二个"xiaohong"删除。
print(year1)#慎用或不用
'''
'''
year1.index(2001)#查找元素在列表中的位置
year1.pop(1)#删除指定位置的元素  .pop()删除末尾元素
del1 = year1.pop(1)#pop（）删除指定位置的元素并返回删除的元素
print(year1)
print(del1)

year1.clear()#清空列表
print(year1)

year1.reverse()#反转列表
print(year1)

year2.sort()#排序列表   error:'<' not supported between instances of 'int' and 'list本来排序的是year1但是因为year1里面合并了列表year2所以无法把int类型和list类型比较
print(year2)

num = [1,2,2]#列表乘法
num =num*4
print(num)
'''

list4 = [1,2,3,4,5]
print(list4)
list4[2] = 100#修改列表指定位置元素
print(list4)

#错误的修改方式
#很多初学者容易犯这样一个错误：将列表中的一个元素取出，赋值给一个变量，然后修改这个变量，期望列表中对应的元素也能够一起修改。
#这里修改的肯定是新变量的值啊，列表里存该变量的地址完全就不是同一个了，所以修改不了原列表的值。

son_list4 = list4[0:3:1]#列表切片 = 列表名[起始索引:终止索引:步长]步长是隔几个取一个元素默认为1
print(son_list4)#终止位置的元素不包含在切片内，左闭右开的区间
son2_list4 = list4[1:3]#步长为1可以省略
print(son2_list4)
son3_list4 = list4[::2]#步长为2 省略起始和终止的索引->从头到尾取
print(son3_list4)
son4_list4 = list4[::-1]#步长为负数->反转列表
print(son4_list4)
son5_list4 = list4[3:1:-1]#可以看到当我们使用负步长进行反向切片的时候，起始索引必须大于终止索引
print(son5_list4)
son6_list4 = list4[::]#取了一个有一模一样元素的列表，但是当然两个列表的存储地址不同
#切片索引不会越界 起始和终止取不到也不会报错

#列表的内容可以反复修改是可变数据类型类似于数组，字符串的内容不能修改
#到目前为止我们已经学习了多种和列表相关的操作。其中大部分操作属于原地修改（in-place modification）。
#所谓原地修改，指的是对原对象自身进行的修改，并没有额外创建新的对象。比如append()、extend()、pop()等方法，包括在文档Python常用内置函数、方法、技巧汇总 中提到的sort()、reverse()等方法。+=，*=等运算符，有时候也被称为原地修改运算符。
#而与之对应的非原地修改，指的将修改结果储存在一个新的对象中，而原对象不发生改变的一种修改。比如在文档Python常用内置函数、方法、技巧汇总 中提到的sorted()、reversed()等内置函数。

dif = list[1,2,'h']#列表中元素类型可以不一致

# 对lst本身进行升序排列，使用sort()方法
lst = [3, 1, 2]
# lst变为[1, 2, 3]
lst.sort()
# 得到一个新的升序列表，lst保持不变，使用sorted()*内置函数
lst = [3, 1, 2]
# lst不变，lst_sorted为[1, 2, 3]
lst_sorted = sorted(lst)
'''
无论是方法sort()或者内置函数sorted()都有两个形参，
reverse和key，前者表示是否倒序排列，后者表示排序的依据，通常会涉及到lambda匿名函数的使用（后续会详细讲解）。
'''
# 对lst本身进行降序排列，使用sort()方法
lst = [3, 1, 2]
# *lst变为[3, 2, 1]
lst.sort(reverse = True)#双参数形式

# 得到一个*新的降序列表，*lst保持不变，使用sorted()内置函数
lst = [3, 1, 2]
# lst不变，lst_sorted为[3, 2, 1]
lst_sorted2 = sorted(lst, reverse = True)
print('lst:',lst)
print('lst_sorted:',lst_sorted)


#映射map()函数，把一个列表里的所有元素批量地调用某一个函数，并映射得到一个新的列表（原列表中元素相对位置不变）
# 可以使用内置函数map(func, iter)双参数并用到迭代器
lst_str = ["1", "2", "3"]
# 得到lst_num为[1, 2, 3]
lst_num = list(map(int, lst_str))
print('lst_num:',lst_num)

lst_str = ["1", "2", "3"]
lst_num2 = [1,2]#列表的生成空列表是list(),自定义是lst=[1,2]  为了代码逻辑的清晰和避免混淆，最好将 lst_num2 的初始定义为空列表，除非有特殊需求：lst_num2 = []
#这段代码是一个简单的 for 循环，用于遍历列表 lst_str 中的每一个元素
# 每次迭代时，将列表中的一个元素赋值给变量 variable，并将该变量转换为整数类型，然后将转换后的整数类型的值添加到列表 lst_num 中
for variable in lst_str:
    #在给定的代码片段中，for 循环内部的操作是将 variable 追加到列表 lst_num2 中
    print(type(lst_num2))
    lst_num2.append(int(variable))
print('lst_num2:',lst_num2)

s = "1 2 3 4 5"
lst = s.split()#()里填想用什么分割符号，默认为，
# 等价于lst = s.split(" ")

s = "1,2,3,4,5"
lst2 = s.split(",")

# 两种分割均会得到lst = ["1", "2", "3", "4", "5"]

lst3 = ["a", "b", "c"]
s = "".join(lst)
# 会得到s = "abc"

s_space = " ".join(lst)
# 会得到s_space = "a b c"

s_star = "*".join(lst)#"加字符串进列表
# 会得到s_star = "a*b*c"

'''
注意:
1. 字符串属于一种不可变数据类型，并不能直接进行修改操作。当题目要求对一个字符串进行修改时，通常会先将原字符串使用split()方法或list()转化成列表，对列表修改后再使用join()方法得到新字符串的方式来实现。
2. 列表lst必须是一个字符串类型列表，即lst: List[str]。如果lst是一个整数类型列表，直接使用语句"".join(lst)会出现类型错误TypeError。如需进行合并操作，必须使用map()内置函数对lst中的元素进行类型转换，将lst中的所有int类型元素转换成str类型
'''

#用split提出列表元素再用map逐个输出
lst = input().split()#先从键盘输入列表然后用split分离
lst4=list(map(int,input().split()))#输入数字列表

lst5 = ['a','b','c']
ans = ','.join(lst5)#把列表元素提出来生成一个字符串
print('lst5:',ans)
