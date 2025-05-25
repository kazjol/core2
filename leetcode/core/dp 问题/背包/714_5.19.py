# 买卖股票的最佳时机含手续费

# 给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。

# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

# 返回获得利润的最大值。

# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。


'''
    0-1背包问题
    保存两个状态的数据做动态规划 对状态的更新需要考虑全部的可能
'''
# 和普通股票的区别只是多了手续费
# 卖出的时候说明买过了是一次完整的交易 有手续费
# 递推 动态规划
from functools import lru_cache
from math import inf
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # 保存每持有或不持有股票的最大利润
        dp = [[0] * 2 for _ in range(n)] # 0表示不持有股票 1表示持有股票
        dp[0][0] = 0 # 第一天不持有股票的利润
        dp[0][1] = -prices[0] # 第一天持有股票的利润
        for i in range(1, n): # 从第二天开始
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee) # 只有卖出时才需要手续费
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]) 
        return dp[n-1][0] # 最后一天不持有股票的利润 最后一天不持有股票是最大利润


# 递归 
class Solution2:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache(None)
        def dfs(i: int, hold: bool) -> int:
            if i < 0:
                return 0 if not hold else -inf
            if hold:  # 持有股票
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            else:  # 不持有股票
                return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i] - fee) # 嵌套式递归 直接调主函数的参数根本没必要传的
        return dfs(len(prices) - 1, False)

prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(Solution2().maxProfit(tuple(prices), fee))  # 传入 tuple

# 如果只在函数内部转tuple 在递归调用的时候传入的参数还是list类型还是无法用chache保存
'''
    状态是动态的 所以要先定状态再计算
'''