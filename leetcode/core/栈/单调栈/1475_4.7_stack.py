# 给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。
# 商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。
# 请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格

# 后面比当前price[i]价格低的最近的一个 最终price[i]的价格为prices[i]-prices[j]
# 比栈顶大的压栈比栈顶小的弹栈 压入新的元素到栈顶

# 从后往前遍历数组 存储更小的元素到栈底弹出栈顶元素 就能保证离的更近且元素值更小
from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices) # 从后往前遍历
        stack = [] # 初始化栈
        res = [0]*n # 初始化结果数组 用来存最后的价格

        for i in range(n-1, -1, -1): # （起始，终止，步长）满足从后往前遍历


            while stack and prices[i] < stack[-1]: # 栈不为空且当前价格小于栈顶元素价格
                stack.pop() # 弹出栈顶元素
            if stack and prices[i] > stack[-1]:  # 栈不为空且当前价格大于栈顶元素价格

                res[i] = prices[i] - stack[-1]  # 记录折扣后的价格
                stack.append(prices[i])  # 压入当前元素到栈顶 压入的是prices[i]而不是索引

            if not stack: # 栈为空
                stack.append(prices[i]) # 压入当前元素到栈顶
                res[i] = prices[i] # 记录当前元素的价格 没有折扣

        return res
# 等于时也能打折
prices = [10,1,1,6]
print(Solution().finalPrices(prices)) # [9,0,1,6]

# 用while一定要逻辑清晰while就是用来遍历迭代的 要想明白while结束后想得到什么结果后面接什么条件判断



# stack[-1]是栈顶元素
# stack.pop()弹出栈顶元素
# stack.append(prices[i])压入当前元素到栈顶

# 调试的时候打断点然后调试 一步一步执行观察变量的变化 线程变量窗口里会都给出来









prices = [8,4,6,2,3]