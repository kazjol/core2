# 最小路径和
# 数组 dp 矩阵

# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 只能向右和下移动一步。
from math import inf
from typing import List
# 记忆化搜索
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 创建dp数组，dp[i][j]表示从(0,0)到(i,j)的最小路径和
        dp = [[0] * n for _ in range(m)] # 一行n个[0] m 行
        
        # 初始化第一行和第一列
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            
        # 填充dp数组
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                
        return dp[m-1][n-1]
    
    # 递归
    # 递归边界：
    # 基本都是 一个判断出界的情况

    # dfs(−1,j)=dfs(i,−1)=∞。用 ∞ 表示不合法（出界）的状态，****从而保证 min 不会取到不合法的状态。
    # dfs(0,0)=grid[0][0]。
    # 递归入口：dfs(m−1,n−1)，这是原问题，也是答案。

    # 写递归函数都是自底向上 倒着想 从第一个出栈出递归的开始想怎么写


    def minPathSum_recursive(self, grid: List[List[int]]) -> int:
            m, n = len(grid), len(grid[0])
            from functools import cache # 只在当前函数中引入cache
            @cache
            def dfs(i: int, j: int) -> int:
                # 到达起点
                if i == 0 and j == 0:
                    return grid[0][0]
                # 如果在第一行，只能从左边来
                if i == 0:
                    return dfs(0, j-1) + grid[0][j]
                # 如果在第一列，只能从上方来
                if j == 0:
                    return dfs(i-1, 0) + grid[i][0]
                # 其他情况，可以从上方或左边来
                return min(dfs(i-1, j), dfs(i, j-1)) + grid[i][j]
                
            return dfs(m-1, n-1)
    
class Solution2:

    def minPathSum_cache(self, grid: List[List[int]]) -> int:
            from functools import cache
            from math import inf

            @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化） cache在函数名前就是装饰这个函数
            def dfs(i: int, j: int) -> int:
                if i < 0 or j < 0:
                    return inf # 出界返回无穷大
                if i == 0 and j == 0:
                    return grid[i][j]
            
                return min(dfs(i, j - 1), dfs(i - 1, j)) + grid[i][j]
        
            return dfs(len(grid) - 1, len(grid[0]) - 1)



class Solution3:
        # 递归思想 但只有归没有递 也就是倒推 但是不列递归方程
        def minPathSum_recursivenot(self, grid: List[List[int]]) -> int:
            
            m, n = len(grid), len(grid[0])
            f = [[inf] * (n + 1) for _ in range(m + 1)]
            for i, row in enumerate(grid):
                for j, x in enumerate(row):
                    if i == j == 0:
                        f[1][1] = x
                    else:
                        f[i + 1][j + 1] = min(f[i + 1][j], f[i][j + 1]) + x
            return f[m][n]
        # 空间优化 一样的方法 二维缩成一维 只需列数的空间大小
        # 依然是把左边的状态更新到第一行 只保存更新的元素 dp[i] = dp[i-1]+dp[i-2]
        def minPathSum_recursive_memooptimize(self, grid: List[List[int]]) -> int:
             
             n =  len(grid[0])
             f = [inf] * (len(grid[0]) + 1) # 初始化全为无穷大  min选不到更大的路径
             f[1] = 0 # 初始化起点为0
             for row in grid:
                for j, x in enumerate(row):
                     f[j + 1] = min(f[j], f[j + 1]) + x 
             return f[n]







grid = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minPathSum(grid)) # 7
print(Solution().minPathSum_recursive(grid)) # 7
print(Solution2().minPathSum_cache(grid)) # 7
print(Solution3().minPathSum_recursivenot(grid)) # 7

# 贪心和动态规划的区别就是 当前的更新是否是根据之前的数据



# 这个记忆化搜索的解法实际上和动态规划是等价的，只是实现方式不同：
# 动态规划是自底向上的
# 记忆化搜索是自顶向下的
# 但通常来说，动态规划的迭代解法更容易理解和实现，而且空间复杂度通常可以优化得更好。


# 第一行和第一列的特殊性：
# 对于第一行，每个位置只能从左边到达（因为不能从上方来）
# 对于第一列，每个位置只能从上方到达（因为不能从左边来）
# 这意味着这些位置只有一条可能的路径
# 如果不初始化会怎样：
# 如果直接开始计算 dp[1][1]，我们需要 dp[0][1] 和 dp[1][0] 的值
# 但这些值还没有被正确计算，会导致错误的结果

# 没有考虑第一行和第一列的路径
# 忽略了只能向右或向下移动的限制
# 没有正确计算到达每个位置的最小路径和
# 正确的初始化确保了：
# 第一行的每个位置只能从左边到达，所以路径和是累加的
# 第一列的每个位置只能从上方到达，所以路径和也是累加的
# 这样在计算其他位置时，才能正确比较上方和左方的路径和
# 这就是为什么初始化第一行和第一列是动态规划解决这个问题的关键步骤。