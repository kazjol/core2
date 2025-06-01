# https://yxvp0lnjvna.feishu.cn/docx/ELLhdbqqtorqftxNQR5cC1m4nHf
from cmath import inf
from collections import defaultdict
from typing import List
ans = [[inf,0],[inf,0]]

def jump(c_step:List[int],target:int) :
   dict = defaultdict(int)
   global ans
   for i in range(len(c_step)): # 步数是键 索引是值
       dict[c_step[i]] += i
   
   # print(dict)
   for step,i in dict.items():
       if (target - step) in dict and ans[0][0] + ans[1][0] > i + dict[target - step]:
           ans[0][0] = i
           ans[0][1] = step
           ans[1][0] = dict[target - step]
           ans[1][1] = target - step
#    return [ ans[i][1] for i in (0,1) ] #注意到逗号","的后面的包含空格" "的。但这是错误的输出结果，会得0分！



c = input() # s = input()[1:-1]可以直接写
c_step =list(map(int,c[1:-1].split(',')))
# print(c_step)
target = int(input())
jump(c_step,target)
print(f"[{ans[0][1]},{ans[1][1]}]") # 输出结果其实不是数组类型 而是把[]当字符打出来了 我服了



'''
    它允许我们在字符串中直接嵌入 Python 表达式。基本语法是在字符串前加上 
    花括号 {} 来包含要插入的表达式。

    x = 10
    y = 20
    print(f"{x} + {y} = {x + y}")
    # 输出：10 + 20 = 30




    pi = 3.14159
    # 保留两位小数
    print(f"π的值是{pi:.2f}") .2f保留两位float
    # 输出：π的值是3.14


    name = "Bob"
    # 左对齐，总宽度10
    print(f"{name:<10}!")
    # 输出：Bob       !

    # 右对齐，总宽度10
    print(f"{name:>10}!")
    # 输出：       Bob!

    # 居中对齐，总宽度10
    print(f"{name:^10}!")
    # 输出：   Bob    !
'''