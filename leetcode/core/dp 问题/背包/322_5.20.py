# 零钱兑换
# bfs dp 数组
# 给你一个整数数组 coins ，表示不同面额的硬币数量不限；以及一个整数 amount ，表示总金额。

# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

# 你可以认为每种硬币的数量是无限的。

# 还是0-1背包问题 每种硬币选或不选

from cmath import inf
from functools import cache
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, c: int) -> int:
            if i < 0:
                return 0 if c == 0 else inf
            if c < coins[i]:
                return dfs(i - 1, c)
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1) # 是否选择选这枚硬币
        ans = dfs(len(coins) - 1, amount)# 从大到小找硬币
        return ans if ans < inf else -1

coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins, amount))
