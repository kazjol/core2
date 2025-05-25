# 买卖股票的最佳时机 只允许交易一次
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。


# 找差值最大就好了
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # 记录到当前为止的最低价格
        min_price = float('inf')
        # 记录最大利润
        max_profit = 0
        
        for price in prices:
            # 更新最低价格
            min_price = min(min_price, price)
            # 尝试用当前价格卖出，更新最大利润
            max_profit = max(max_profit, price - min_price)
            
        return max_profit

# 记录遍历过程中遇到的最低价格 cur
# 对于每个新价格 num，如果比当前记录的最低价格 cur 还低，就更新最低价格
# 否则计算当前价格与最低价格的差值，并与当前最大利润 res 比较，取较大值
# 这是一个典型的贪心策略：始终保持记录历史最低点，然后尝试在每个价格点卖出，更新可能的最大利润。算法复杂度是 O(n)，只需要遍历价格数组一次。
class Solution2: # 贪心
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        res = -prices[0]
        cur = prices[0]
        for num in prices:
            if num < cur:
                cur = num
                
                continue
            
            res = max(res,num-cur)
        if res < 0:
            return 0
        return res
 
prices = [2,4,1]
print(Solution2().maxProfit(prices))


