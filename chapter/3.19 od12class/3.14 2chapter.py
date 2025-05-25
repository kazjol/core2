'''
a=input("write a number")
mas='hh'
mass=str(1.5)#强制类型转换
maas= (mass + '\t') * 3
mes=float(mass)*2#mass是小数float
print(mas)
print(mass)
print(maas)
print(mes)
print(type(mes))#type内置函数
print(a)
'''

'''
name = input("plz input a name: ")#在控制台里输入想输出的东西
print(name)
num = input("write a number")#input（）得到的结果一定是字符串类型所以要强制类型转换
num2 = int(num)
print(num*2)
print(num2*2)
'''

print(123, "abc", type(10086))
print(123, "abc", type(10086), sep = ",")#sep设置输出的分隔符 separator

#f-string格式化字符串字面值
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")#在字符串前面加f在想要直接输出的变量加{}_因为这里用print输出一个字符串用的是“”要在直接输出的字符串里加上要输出的变量