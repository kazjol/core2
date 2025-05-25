# 列表是动态数组，它们可变且可以重设长度，而元组不可变，且其内部数据一旦创建便无法改变。
# 元组比列表的访问和处理速度快。
# 元组也支持切片，但是它只支持通过切片访问元组中的元素，不支持修改。
# ***因为列表可以修改，元组不可以修改，因此元组比列表具有更高的安全性。
# 列表不能作为字典的键，而元组可以。
stu_tuple = ('a','b','c')# 用下划线命名的是元组 元组是小括号
print(stu_tuple)
#初始化只含一个元素的元组,要用，结尾否则会视作运算符（）
stu_tuple2 = (3,)
#空元组初始化
tuple1 = ()
tuple2 = tuple()
print(tuple1, tuple2)
value1 = stu_tuple[0]#元组也能用索引
tup = (1, 3, 5, 7, 9, 11)
sub_tup = tup[1:4]#切片从1到4的元素
print(sub_tup)
'''
虽然我们不能直接对元组本身进行修改，但既然元组和列表的结构和形式如此相似，
那么很容易想到，我们可以将元组转换为列表，对转化后的列表进行修改，
再将修改后的列表转换回元组。
'''
stu_list = list(stu_tuple)#转换为列表
stu_tuple = tuple(stu_list)#转换回元组
#想修改元组就先转为列表再修改


#定义函数
'''
def 函数名(若干参数):这里同c是形参类型
    ’’‘
    函数体
    ‘’‘
    return 返回值  
'''
#python里不用指明返回值类型，函数会自动识别
def my_add(a, b):
    ans = a + b
    return ans
print(my_add(2, 3))

#表示代码间的包含关系用tab键，表示代码块的开始和结束用四个空格

# 返回一个值
def add1(a, b):
    ans = a + b
    return ans


# 返回一个表达式
def add2(a, b):
    return a + b


# return语句后没有表达式，默认返回None
def add3(a, b):
    print(a + b)
    return


# 没有return语句，默认返回None
def add4(a, b):
    print(a + b)

#通过赋值得到函数调用结果（return的结果）

#按形参位置传实参
def greet(name, message):
    return f"{message}, {name}!"#f-string格式化字符串，可以让变量直接加入print输出
print(greet("Alice", "Hello"))  # 输出：Hello, Alice!


#关键字传参，实参通过参数名传给形参  在这个例子中，实际参数通过关键字方式传递，明确指定了实际参数对应的形式参数。
# 此时位置顺序则不作为传参的优先级，本身是按参数顺序来调用函数
def greet(name, message):
    return f"{message}, {name}!"

print(greet(message="Good morning", name="Bob"))  # 输出：Good morning, Bob!
print(greet(name="Bob", message="Good morning"))  # 输出：Good morning, Bob!

#有默认形参
def greet(message, name = "Alice"):
    return f"{message}, {name}!"

print(greet("Hello"))               # 输出：Hello, Alice!
print(greet("Hello", "Bob"))        # 输出：Hello, Bob!

#*args 允许你传入**任意数量的位置参数，这些参数在函数内部会以元组（tuple）的形式出现。
# **kwargs 允许你传入**任意数量的关键字参数，这些参数在函数内部会以字典（dictionary）的形式出现。
def summarize(*args, **kwargs):#keyword arguments   *和**的用法
    print("args:", args)
    print("kwargs:", kwargs)

summarize(1, 2, 3, name="Alice", age=30)#**在函数调用时，不使用参数名直接传递的值都是位置参数。  在这里用到了关键字赋值传参的就是关键字参数
#传入的位置参数是 1, 2, 3，它们会被打包成一个元组 (1, 2, 3)。
# 传入的关键字参数是 name="Alice" 和 age=30，它们会被打包成一个字典 {'name': 'Alice', 'age': 30}。字典有建和值，键唯一值可以重复
# 输出：
# args: (1, 2, 3)
# kwargs: {'name': 'Alice', 'age': 30}

'''
常见的不可变数据类型 创建后不可修改有：
- 整数、浮点数、字符串、元组、布尔值

可变数据类型在创建后，其值可以被改变。
常见的可变数据类型有：
- 列表、字典、集合（后两者在后面会学到）
'''


#**a 和 b 都引用同一个列表对象 [1, 2, 3]所以修改b，a也跟着修改
a = [1, 2, 3]    # 对a进行赋值，将值为[1, 2, 3]的列表对象赋值给a
b = a            # 对b进行赋值，将值为[1, 2, 3]的列表对象赋值给b
b.append(4)      # 修改b，对该值为[1, 2, 3]的列表对象进行修改，a也跟着修改，因为引用了同一个对象
print(a)         # 输出: [1, 2, 3, 4]
print(b)         # 输出: [1, 2, 3, 4]

#如果我们希望将a的值[1, 2, 3]赋值给b的时候，b仅仅获得相同的值，
# 而不是和a引用同一个对象，我们可以使用列表的copy()方法或者切片来进行。
a = [1, 2, 3]    # 对a进行赋值，将值为[1, 2, 3]的列表对象赋值给a
b = a.copy()     # 对b进行赋值，将值为[1, 2, 3]的列表对象的一个拷贝赋值给b，创建了一个拷贝
c = a[0:1]         # 对c进行赋值，将值为[1, 2, 3]的列表对象的一个拷贝赋值给c，创建了一个拷贝，切片
b.append(4)      # 修改b，因为此时a和b并不引用同一个对象，因此a不会跟着修改
c.append(5)      # 修改c，因为此时a和c并不引用同一个对象，因此a不会跟着修改
print(a)         # 输出: [1, 2, 3]
print(b)         # 输出: [1, 2, 3, 4]
print('c',c)         # 输出: [1, 2, 3, 5]

a = [[1, 2], [3, 4]]
b = a.copy()

b.append([6])
print(a)  # 输出: [[1, 2], [3, 4]]
print(b)  # 输出: [[1, 2], [3, 4], 6]
# 注意到，对b自身而言的修改，譬如b.append(6)并不会影响a，因为a和b是两个不同列表对象的引用。
# b本身是浅拷贝
b[1].append(5)
print(a)  # 输出: [[1, 2], [3, 4, 5]]
print(b)  # 输出: [[1, 2], [3, 4, 5], 6]
# 这是因为，copy()方法（以及切片）均属于浅拷贝（shallow copy）。
# 浅拷贝仅仅是拷贝了原对象的引用，创建了一个原对象的副本，但不会拷贝对象本身的深层副本。
# 当我们对浅拷贝（上述例子中的b）中的子对象进行修改的时候，原对象（上述例子中的a）中对应的子对象也会发生修改。
# 对深层对象没实现浅拷贝


# 深拷贝会创建一个新的对象，并递归地复制所有子对象。
# 深拷贝后，原对象和新对象之间完全独立，任何一个对象（以及子对象）的修改都不会影响另一个对象。
# 因此，深拷贝会创建一份原对象及其所有子对象的完全副本。
from copy import deepcopy

a = [[1, 2], [3, 4]]
b = deepcopy(a)

b.append([6])# 因为列表b对象的元素类型为列表所以插入的也应该为列表，但是插入int类型也不影响
# 插int类型会警告  应为类型 'list[int]' (匹配的泛型类型 '_T')，但实际为 'int'
print(a)  # 输出: [[1, 2], [3, 4]]
print(b)  # 输出: [[1, 2], [3, 4], 6]

b[1].append(5)
print(a)  # 输出: [[1, 2], [3, 4]]
print(b)  # 输出: [[1, 2], [3, 4, 5], 6]

# 对于不可变数据类型，
# 函数内部的修改不会影响外部对象，因为任何修改都会创建一个新的对象。
def modify_string(s):
    print(f"Original string: {s}")
    s = s + " world"
    print(f"Modified string: {s}")

my_str = "Hello"
modify_string(my_str)
print(f"String after function call: {my_str}")#函数内部操作不会影响外部对象

# 使得对不可变数据类型变量的内部修改对外部可见
# 1. 将修改结果作为返回值return出函数外，并且在调用函数的时候对a进行赋值，譬如
def modify_immutable(x):
    print(f"Original value: {x}")
    x = x + 1
    print(f"Modified value: {x}")
    return x

a = 10
a = modify_immutable(a)# 用返回值对外部对象赋值就行了
print(f"Value after function call: {a}")

# 2. 使用global关键字，在函数内将变量a声明为全局变量，且不再需要进行传参，譬如
def modify_immutable():
    global a#声明a为全局变量
    print(f"Original value: {a}")
    a = a + 1
    print(f"Modified value: {a}")

a = 10
modify_immutable()
print(f"Value after function call: {a}")

#如果函数内部修改的原版（用的引用）自然会修改源对象

#lambda匿名函数，不需要定义函数名
# 使用lambda匿名函数进行函数定义
# 注意这里的get_one_lambda看似是一个变量名
# 但实际上是一个函数名
get_one_lambda = lambda: 1

print(get_one_lambda)
# 输出形如 <function <lambda> at 0x00000249F7AD7B00> 的结果
# 这一长串复杂的十六进制数是函数get_one_lambda的内存地址

print(get_one_lambda())
# 在函数名get_one_lambda后面加上括号，才能正确地输出1

# 这里的(lambda: 1)等价于上面的函数名get_one_lambda
# (lambda: 1)()等价于get_one_lambda()
# 显然get_one_lambda这个函数名是不必要的，故称之为"lambda匿名函数"
print(lambda: 1)
# 输出形如 <function <lambda> at 0x00000249F7AD7B00> 的结果
# 这一长串复杂的十六进制数是该匿名函数的内存地址
print((lambda: 1)())
# 在匿名函数后面加上括号，才能正确地输出1





# 含参数的lambda函数
# 使用lambda匿名函数进行函数定义
# 注意这里的get_one_lambda看似是一个变量名
# 但实际上是一个函数名
add_lambda = lambda x,y: x+y# 用到lambda关键字定义匿名函数，参数x,y
print(add_lambda)
# 输出形如 <function <lambda> at 0x00000249F7AD7B00> 的结果
# 这一长串复杂的十六进制数是函数add_lambda的内存地址
print(add_lambda(10, 20))
# 在函数名add_lambda后面加上括号并传入参数，才能正确地输出结果

# 这里的(lambda x,y: x+y)等价于上面的函数名add_lambda
# (lambda x,y: x+y)(10, 20)等价于add_lambda(10, 20)
# 显然add_lambda这个函数名是不必要的，故称之为"lambda匿名函数"
print(lambda x,y: x+y)
# 输出形如 <function <lambda> at 0x00000249F7AD7B00> 的结果
# 这一长串复杂的十六进制数是该匿名函数的内存地址
print((lambda x,y: x+y)(10, 20))
# 在匿名函数后面加上括号并传入参数，才能正确地输出结果


'''
1. lambda匿名函数本质上是一个函数，而不是一个变量，使用lambda匿名函数可以得到一个函数。
2. 定义lambda匿名函数的语法为：lambda [形参]: 返回值，形参的数量可以为0，即支持定义无参数匿名函数。
3. 使用lambda匿名函数的语法为：(lambda [形参]: 返回值) ([实参])，一般情况下，实参的数量应该和定义的形参数量一致。
'''
