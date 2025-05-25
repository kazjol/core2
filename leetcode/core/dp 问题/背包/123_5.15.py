# 买卖股票的最佳时机 III 限制买卖股票IV的k为2

# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

from math import inf
from typing import List
from functools import cache
# 记忆化搜索
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prices = tuple(prices)  # 将列表转换为元组，使其可哈希 元组可哈希也可索引
        
        @cache # 用cache装饰器 要保证返回结果可哈希 cache在哪个函数前就是缓存哪个函数
        # hold这里就是0-1的体现
        def dfs(i, k, hold)->int:
            if i == n or k == 0:
                return 0
            if hold: # 持有股票 hold = True 能卖出说明之前买入了一次买入卖出才算一次操作k-1 变为不持有该股票hold = False 收益增加prices[i]
                return max(dfs(i+1, k, True), dfs(i+1, k-1, False) + prices[i]) # 不卖 卖
            else: # 不持有股票 hold = False 则第二天无法卖出只能买入 买入而没有卖出不算一次操作
                return max(dfs(i+1, k, False), dfs(i+1, k, True) - prices[i]) # 不买 买
        
        return dfs(0, 2, False) # 从0开始 不持有股票
    
    # 动态规划 
    # 简化了dp数组 因为只有两次操作 f11 f12 f01 f02 四个状态 
    def maxProfit2(self, prices: List[int]) -> int:
        f11 = f12 = -inf
        f01 = f02 = 0
        # 每次都更新四个状态 01是持有状态 12是操作次数 f12是当天持有该股票做2次交易的最大收益
        for p in prices: # 每天都更新
            f11 = max(f11, - p)     # 第一次买入
            f01 = max(f01, f11 + p) # 第一次卖出
            f12 = max(f12, f01 - p) # 第二次买入  一次操作后不持有股票的情况才能进行第二次的买入
            f02 = max(f02, f12 + p) # 第二次卖出    
        return f02 # 返回两次操作后的结果
prices = [3,3,5,0,0,3,1,4]
print(Solution().maxProfit(prices))
