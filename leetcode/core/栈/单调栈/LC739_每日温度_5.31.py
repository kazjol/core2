# https://ahym1n4sq5.feishu.cn/docx/EqzUdmuKCo1pZQxjGyqctjw1n0e

'''
    经典的单调栈的问题


'''
from typing import List

# 遍历超时 35/48
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # 遇到温度低的就入栈 遇到高的时候再全部弹出
        l = []
        ans = [0]*n

        for i in range(n): # 对每个元素求后续的全部
            l.append(temperatures[i]) # 每次开始时当前元素都入栈 能保证一天就退出值为1
            for j in range(i+1,n):

                if temperatures[j] <= temperatures[i]: # 同温度也不算升温
                    l.append(temperatures[j])
                else:
                    ans[i] = len(l) # 遇到温度高的了
                    l = []
                    break
            if len(l) == n-i:
                l = []
        return ans


# 单调递增栈
class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # 构建一个栈,用来存放每日温度的下标 计算下标差值就是需要几天升高
        stack = []

        # 获取数组长度
        length = len(temperatures)

        # 构建一个数组，用来保存输出结果
        res = [0] * length

        # 从头开始遍历每天的温度
        for i in range(length):
            # 拿到当天的温度，不断的和栈顶元素进行比较
            temperature = temperatures[i]


            '''
                这个栈保存的元素是单调的
            '''
            # 栈不为空 当前温度大于栈顶温度 出栈执行pop（） stack更新然后继续判while
            '''
                什么时候用while 什么时候用for
                for 是遍历中间不会跳出除非加了break
                while 是每次循环都做操作 随时满足条件可退出 
                单调栈一定是用while的
                
                 
            '''


            # 栈从下到上长 上面是栈顶 保存的元素从栈底到栈顶单增（单调增栈）  底也就是压在最下面的也就是最早入栈的
            # 遇到比栈顶元素大的则弹出 相比较栈顶元素而言升温了
            # 连续弹出 也就能计算之前的相隔多少天才遇到今天（升温） 因为栈里保存的是索引所以相隔天数可以计算差值
            # 栈的好处就是能保存之前的状态 使得可以不从头开始计算

            while stack and temperature > temperatures[stack[-1]]: # 每次做完pop（）都会再判断 栈顶元素也就是最后一个入栈的元素也就是stack[-1]

                # 首先获取栈顶元素的值，也就是现在要比较当前温度是不是想比pre这天的温度上涨了
                preIndex = stack.pop()

                # 它们的下标差就是栈顶元素等了多少天等到的更高温度的结果，保存到输出数组 res 中

                # 当天温度是preIndex的第一个升温的天数
                res[preIndex] = i - preIndex

            # 再把当天的温度的下标值存放到栈中
            # 注意：是下标索引值
            stack.append(i)

        # 最后输出 res 数组即可
        return res
temperatures = [55,38,53,81,61,93,97,32,43,78]
print(Solution().dailyTemperatures(temperatures))
print(Solution2().dailyTemperatures(temperatures))