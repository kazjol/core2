# 买卖股票的最佳时机 IV
# 0-1背包问题 每次买或不买


# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

from math import inf
from typing import List
from functools import cache
# 记忆化搜索
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
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
        
        return dfs(0, k, False) # 从0开始 不持有股票

# 动态规划解法 - 时间优化
class Solution2:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
            
        n = len(prices)
        
        # 特殊情况处理：当k很大时，问题退化为不限交易次数  优化时间
        if k >= n // 2:
            # 贪心算法解决不限交易次数的情况
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
            
        # dp[i][j][0]表示第i天最多进行j次交易且不持有股票的最大利润
        # dp[i][j][1]表示第i天最多进行j次交易且持有股票的最大利润
        dp = [[[0, -float('inf')] for _ in range(k+1)] for _ in range(n+1)] # 可以直接导入inf 直接赋值
        
        # 初始化：第0天不可能持有股票
        for j in range(k+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -float('inf')
        
        for i in range(1, n+1):
            price = prices[i-1]  # 当前价格
            for j in range(k+1):
                # 不持有股票：前一天不持有，或前一天持有今天卖出
                dp[i][j][0] = dp[i-1][j][0]
                if j > 0 and dp[i-1][j-1][1] != -float('inf'):
                    dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-1][1] + price)
                
                # 持有股票：前一天持有，或前一天不持有今天买入
                dp[i][j][1] = dp[i-1][j][1]
                if dp[i-1][j][0] != -float('inf'):
                    dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][0] - price)
        
        return dp[n][k][0]
    # 动态规划 单设空间来保存之前的状态用于更新 对记忆化搜索只做到了空间优化
    def maxProfit2(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        f = [[[-inf] * 2 for _ in range(k + 2)] for _ in range(n + 1)] # 初始化dp数组 三维数组保存状态 （天数 交易次数 持有状态  ） 
        for j in range(1, k + 2): # 初始化第0天 交易次数从1到k+1
            f[0][j][0] = 0
        for i, p in enumerate(prices): # 遍历每一天
            for j in range(1, k + 2): 
                f[i + 1][j][0] = max(f[i][j][0], f[i][j][1] + p) # 不持有股票 前一天不持有 或前一天持有今天卖出
                f[i + 1][j][1] = max(f[i][j][1], f[i][j - 1][0] - p)
        return f[-1][-1][0]


    # 空间优化版 - 状态压缩
    def maxProfit_optimized(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
            
        n = len(prices)
        
        # 特殊情况处理：当k很大时，问题退化为不限交易次数
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
        
        # 只保留当前状态和前一状态
        # buy[j]表示最多进行j次交易且最后一步是买入的最大利润
        # sell[j]表示最多进行j次交易且最后一步是卖出的最大利润
        buy = [-float('inf')] * (k+1)
        sell = [0] * (k+1)
        
        for price in prices:
            for j in range(1, k+1):
                # 对于每个交易次数j，更新买入和卖出的最大利润
                # 注意更新顺序：先更新buy再更新sell
                buy[j] = max(buy[j], sell[j-1] - price)
                sell[j] = max(sell[j], buy[j] + price)
        
        return sell[k]
    
    def maxProfit_optimized2(self, k: int, prices: List[int]) -> int:
        f = [[-inf] * 2 for _ in range(k + 2)] # 初始化dp数组 二维数组保存状态 （交易次数 持有状态 ） k+2项 每项2个元素（表示持有状态） 
        for j in range(1, k + 2):
            f[j][0] = 0
        for p in prices:
            for j in range(k + 1, 0, -1): # 从后往前更新  在同一天 更新不同交易次数和不同持有状态的dp状态 更新为最大的收益
                f[j][0] = max(f[j][0], f[j][1] + p)
                f[j][1] = max(f[j][1], f[j - 1][0] - p)
        return f[-1][0]

    
    def maxProfit_binary_search(self, k: int, prices: List[int]) -> int:
        res = 0 # 记录最终的最大利润
        if not prices:
            return res # 如果价格列表为空，则没有交易，利润为0
        n = len(prices) # 获取价格列表长度
        l, r = 1, max(prices) # 二分查找的左右边界，r代表最大的可能的交易成本 z在范围里猜
        while l <= r: # 闭区间解法
            c = (l + r) // 2 # 计算当前二分查找的中间交易成本
            # 初始化交易过程中的变量
            buyCount, sellCount = 0, 0 # 记录买入和卖出的次数
            buy, sell = -prices[0], 0 # 初始化买入的最大收益，卖出收益初始化为0
            for i in range(1, n):
                # 更新买入状态：如果可以获利润得更好的买入利润，就更新buy
                if sell - prices[i] >= buy:
                    buy = sell - prices[i]
                    buyCount = sellCount # 买入次数与上次卖出次数相同
                # 更新卖出状态：如果可以获得更高的卖出利润，就更新sell
                if buy + prices[i] - c >= sell:
                    sell = buy + prices[i] - c
                    sellCount = buyCount + 1 # 卖出次数+1
            # 根据交易次数 sellCount调整二分边界
            if sellCount >= k:
                res = sell + k * c # 更新最大收益
                l = c + 1 # 交易次数太多，增加交易成本c
            else:
                r = c - 1 # 交易次数太少，降低交易成本c
        # 特殊情况处理：如果res为0，则使用贪心计算最大收益
        if res == 0:
            res = sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))
        return res
prices = [3,2,6,5,0,3]
k = 2
print("记忆化搜索结果:", Solution().maxProfit(k, prices))
print("动态规划结果:", Solution2().maxProfit(k, prices))
print("空间优化结果:", Solution2().maxProfit_optimized(k, prices))   
print("二分查找结果:", Solution2().maxProfit_binary_search(k, prices))   
        