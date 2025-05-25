#https://www.bilibili.com/video/BV1ho4y1W7QK/?vd_source=584c3163bb422497e2633945b1038f8b
# 不限制交易次数

# 122 买卖股票最佳时机
# 贪心 数组 动态规划dp Dynamic Programming

# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
# 返回 你能获得的 最大 利润 。


# 示例 1：
# 输入：prices = [7,1,5,3,6,4]  [1 5] [1 3] [1 6] [1 4] [5 6] [3 6] [3 4]
# 输出：7
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
# 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3。
# 最大总利润为 4 + 3 = 7 。


# 重要还是在状态转移方程的建立 买入和卖出是两种状态
# 画状态机 还有就是一天的开始和一天的结束是两种情况 这个和图那里对一个点分析是一样的
# ****然后自定义函数把状态方程实现 最后递归调用 这个进入递归的入口就也非常重要了

# 利润可以为负数 假如4元买入 没有卖出 那么买入的钱就是负利润 -> 这种负值的思想也是非常常见的
# 第 0 天到第 5 天的利润 = 第 0 - 4 天的利润 + 第 5 天的利润
# 第 0 天到第 4 天的利润 = 第 0 - 3 天的利润 + 第 4 天的利润 可以一直这么递推下去建立方程
# 并且这种思想一般都是从后往前推
# 涉及递归问题了 对于递归问题 递归边界和递归入口就比较重要了


# 第四天结束 = 第五天开始 讨论边界情况的时候这种转移关系非常重要

from functools import cache
from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果 缓计算结果 可以直接比较

        # 递归函数
        def dfs(i: int, hold: bool) -> int:
            if i < 0: # 递归边界（-1，0）或（-1，1）一开始就持有股票则股票之前没卖出利润为负无穷 一开始不持有股票利润为0
                return -inf if hold else 0


            # 如果这天持有股票 看之前是持有还是不持有利润高
            if hold:
                # 状态从上一天不持有到今天的持有 说明今天开始的时候花的是今天的价格 prices[i] 买的股票利润-prices[i]
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])


            # 如果不持有股票 同样看之前是持有还是不持有利润高 逆着推的
            # 状态从上一天的持有到今天的不持有 说明今天开始时按今天的价格 prices[i] 卖出的股票利润 +prices[i ]
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])



        return dfs(n - 1, False) # 递归入口调用递归 开始从len（prices）-1也就是从最后一天开始
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))


print("简短的判断语句：",1 if "a" > "b" else 0 )



# 空间优化
print('\n\ndp解法 空间优化')
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        f0, f1 = 0, -inf
        for p in prices:
            f0, f1 = max(f0, f1 + p), max(f1, f0 - p)
        return f0
prices = [7,1,5,3,6,4]
print(Solution3().maxProfit(prices))



