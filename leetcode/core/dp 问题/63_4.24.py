# 不同路径II
# 数组 动态规划 矩阵
import time
from my_python_lib import timing_decorator
from my_python_lib import memory_monitor
from line_profiler_pycharm import profile
from typing import List
from functools import cache
class Solution:

    # @profile()
    @memory_monitor
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # 如果起点或终点有障碍物，直接返回0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
            
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1  # 起点初始化为1
        
        # 初始化第一行
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
                
        # 初始化第一列
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
                
        # 填充剩余位置
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        return dp[m-1][n-1]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        @profile()
        @memory_monitor
        def dfs(i: int, j: int) -> int:
            # 如果当前位置有障碍则当前位置dp存0以0结果退栈
            # 如果是在dfs(i-1,j)的情况退的栈 则意味着不能顺着竖着一列往下继续递归了
            # 竖着往下不能再走了 则意味着竖着往下往左也不能走了 后续dp[i-1][]延续下去的两个dfs的值都是0 dp存0
            if i < 0 or j < 0 or obstacleGrid[i][j]:

                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dfs(m - 1, n - 1)

class Solution3:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][1] = 1 # 因为起点视作1

        for i, row in enumerate(obstacleGrid): # 遍历行定第几行 里面的列表项是行
            # 对某行的列的初始化是在内部的 只根据左边的元素来更新 当起始位置为障碍的时候 会更新初始化的dp[0][1]的值为0
            # 然后紧跟的一行都是0
            # 接下来j+1的下一行 的第一个元素会因为列首个无左边元素 所以只根据上面更新依然会为0

            # 其实根据由左上状态更新当前状态的方式 在某行或列全是障碍的时候 dp更新后在0行列后会全部更新结果会为0
            for j, x in enumerate(row): # 遍历列
                if x == 0:
                    f[i + 1][j + 1] = f[i][j + 1] + f[i + 1][j]
        return f[m][n]

# ****因为只能向右和下走 所以一步只有两种可能 状态也只由左边和上面更新**** 这种状态建立可以用到其他的题目 关键就是看现在是怎样得来的有哪些可能
# 一维数组优化二维
# 把同一列的状态都更新到第一行 实际上在遍历每一行但是最终的结果只放在第一行
# 而且因为只需要得到最后一行一列的结果所以只需保存更新的结果即可
# ***每行的状态 都可以由更新的左边和更新的上面所得 所以只需要维护左边和上面的最新结果即可***这样的话一维的dp[i-1]+dp[i-2]即可得到dp[i]


class Solution4:
        @memory_monitor
        def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
            n = len(obstacleGrid[0])
            f = [0] * (n + 1)
            f[1] = 1
            for row in obstacleGrid:
                for j, x in enumerate(row):
                    if x == 0:
                        f[j + 1] += f[j] # 上 和 上左
                    else:
                        f[j + 1] = 0
            return f[n]

class Solution5:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = obstacleGrid[0]
        f[0] ^= 1  # 0 变成 1，1 变成 0  取反在c里是~
        for j in range(1, n):
            f[j] = 0 if f[j] else f[j - 1]
        for i in range(1, m):
            if obstacleGrid[i][0]:
                f[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    f[j] += f[j - 1]
                else:
                    f[j] = 0
        return f[-1]


# 测试用例
obstacleGrid = [[0,0,0],[0,0,0],[0,0,0]]
print('二维数组递推式',Solution().uniquePathsWithObstacles(obstacleGrid))
# print('递归',Solution2().uniquePathsWithObstacles(obstacleGrid))
# print('二维数组递推式 优化 ',Solution3().uniquePathsWithObstacles(obstacleGrid))
print('一维数组优化 ',Solution4().uniquePathsWithObstacles(obstacleGrid))
print('基于一维数组的空间优化 原地操作 ',Solution5().uniquePathsWithObstacles(obstacleGrid))

# Solution1
# 为什么不用检查一行或一列全为障碍的情况
# 在动态规划的过程中，如果某一行或某一列全是障碍物，那么这一行或列的所有位置都会被初始化为0
# 当计算后续位置时，由于这些位置都是0，所以通过它们的路径数也会是0
# 最终到达终点的路径数自然会是0

# 行在dp初始化的时候是用左边和上面的元素初始化的 所以当出现包围的情况则后续dp存的值都会是0
# 当出现全行全列是障碍物的情况 则dp在初始化的时候就会是0了
# 因为初始化行的时候是用左边的元素来更新dp的元素 初始化列的时候是用上面的元素来更新dp的元素
# 如果出现全行全列的情况 说明第一行或第一列的初始化会全为0 后续的dp更新也会是0 
# 同时这样初始化也会做出如果只有一行一列出现障碍则无法到达的情况


# cache
# 不可哈希类型：
# Python中的列表（List）是不可哈希的类型
# @cache 装饰器需要将函数的参数作为字典的键来缓存结果
# 由于 obstacleGrid 是列表，不能作为字典的键，所以会报错
# 动态规划的特点：
# 这个问题的动态规划解法是自底向上的
# 我们使用二维数组 dp 来存储中间结果
# 不需要递归调用，所以不需要缓存
# 性能考虑：
# 即使我们能够使用缓存（比如将列表转换为元组），在这个问题中也不会有性能提升
# 因为每个位置只会被计算一次
# 使用缓存反而会增加内存开销