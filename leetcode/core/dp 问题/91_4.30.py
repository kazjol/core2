# 粉刷房子
# 数组 dp


# 三列 第一列代表把房子刷成红色，第二列代表把房子刷成蓝色，第三列代表把房子刷成绿色。[][0] [][1] [][2]
# 示例：
# costs = [[1,10,10],[10,1,1],[10,10,1]]
# 给了三栋房子 第一栋房子刷成红色耗费1 第二栋房子刷成红色耗费10
# 二维矩阵dp 
# 横坐标代表房子 纵坐标代表颜色
# dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + costs[i][0]



from typing import List
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0] # 第一栋房子上色 dp三元素分别代表当前元素上色为红蓝绿的最小花费 每次都要更新三种状态
        for i in range(1, len(costs)): # 给每个房子上色 从第二个房子开始
            # dp核心还是状态的转化和继承
            dp = [min(dp[j - 1], dp[j - 2]) + c for j, c in enumerate(costs[i])] # 选择当前的房子涂什么颜色  视j为当前的房子涂什么颜色 则要继承的之前房子涂什么颜色的最小花费是min(dp[j - 1], dp[j - 2])不能和当前的颜色一样
            # dp = [min(dp[j - 1], dp[j - 2]) + costs[i][j] for j in range(3)] # 选择当前的房子涂什么颜色  视j为当前的房子涂什么颜色 则要继承的之前房子涂什么颜色的最小花费是min(dp[j - 1], dp[j - 2])不能和当前的颜色一样

            # enumerate要快因为避免了costs[][]的查找
        return min(dp)
from typing import List
class Solution2:
    def minCost(self, costs: List[List[int]]) -> int:
        from functools import lru_cache

        n = len(costs)

        @lru_cache(maxsize=None)
        def dfs(i: int, color: int) -> int:
            if i == 0: # 边界条件
                return costs[0][color]
            # 只能从前一栋房子的其他两种颜色转移过来 则之前房子只能涂另外两种颜色
            return costs[i][color] + min(
                dfs(i - 1, (color + 1) % 3),
                dfs(i - 1, (color + 2) % 3)
            )

        # 最后一栋房子可以是任意颜色，取最小值
        return min(dfs(n - 1, color) for color in range(3)) # 入口是最后一个房子分别选三种颜色看结果

costs = [[17,2,17],[16,16,5],[5,3,19],[20,3,20]]
print(Solution().minCost(costs))
costs = [[17,2,17],[16,16,5],[5,3,19],[20,3,20]]
print(Solution().minCost(costs))

