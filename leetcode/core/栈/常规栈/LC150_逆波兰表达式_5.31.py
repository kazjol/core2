# https://ahym1n4sq5.feishu.cn/docx/Udkkd4S8KoKHqsxNN4dcYjNDnfb
from typing import List


# 两个整数之间的除法只保留整数部分，向零截断。

# 逆波兰表达式 a,b,'+' 遇符号弹出前两个元素 左边的是第一个操作数

def rpn(tokens:List[str])->int:

    l = []
    for token in tokens:
        # if token[1:-1] in [str(i) for i in range(-200, 201)] :
        #     l.append(int(token))

        '''
            因为输入的数字是字符类型所以其实没办法判断是否是数字
            所以应该放到else
        '''
        # 四种计算方法
        if token == '+':
             tmp = l.pop() + l.pop() # 出栈并返回值 ?从左向右执行就可以连续弹出吧
             l.append(tmp)

        elif token == '-':
            tmp = -l.pop() + l.pop() # 前右后左
            l.append(tmp)

        elif token == '*':
            tmp = l.pop() * l.pop()
            l.append(tmp)

        elif token == '/':
            # tmp = 1//l.pop() * l.pop() # 因为除完向下取整所以这里可能出错
            right = l.pop()
            left = l.pop()
            tmp = int(left / right) # 用int首先先把除法处理好否则后面还是会影响
            l.append(tmp)

        else:
            l.append(int(token))
    return int(l[0])
tokens = ["4","13","5","/","+"]
print(rpn(tokens))

# l = [1,2,3,4]
# print(l.pop(),'+',l.pop(),l.pop(),l.pop())
#

# print(-2+3)

print(1/3 * 6)










