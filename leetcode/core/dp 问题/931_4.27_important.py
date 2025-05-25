# 下降路径最小和
# 数组 dp 矩阵

# 和120很像最主要的特点是无法从上层确定最优解要通过与下层的对比来实现
# 但是区别在第一行不是一个元素
# 最好理解的就是从 最后一层 开始 计算所有到达点的最优解 最后取最小值

# 状态转移方程 递推方程 dp(i,j) = dp(i-1,j-1) + min(matrix(i+1,j),matrix(i+1,j+1),matrix(i+1,j-1))
# 这里用递归的话还是从下到上 跟着状态方程列递归方程
# 递归入口：dfs(n−1,c)，遍历所有 c，取最小值，即为答案。
# 递归边界：dfs(0,c)=matrix[0][c] 到第一行 以及 dfs(r,−1)=dfs(r,n)=∞，出界是不合法的，设置成无穷大，这样取 min 的时候就会自动忽略不合法的情况。
#


# 还是初始化最后一行然后记录每个到达点的最小路径 最后取最小
# 这种解法好像就是二维数组的空间优化成一维
from functools import cache
from typing import List
class Solution:
    # @cache # 存在不可哈希的list不能用cache
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = matrix[-1].copy() # 初始成最后一行 要用copy（）函数否则在改dp的时候matrix会变
        for row in range(m-2, -1, -1): # 从倒数第二行开始
            temp = [0] * len(dp)  # 临时变量 存储当前层到达点的最小路径

            for col in range(n): # 遍历每一列 存储当前层到下一层的最小路径 现在是方形要考虑边界越界问题

                if col == 0: # 左边界
                    temp[col] = matrix[row][col] + min(dp[col], dp[col+1])
                elif col == n-1: # 右边界
                    temp[col] = matrix[row][col] + min(dp[col], dp[col-1])
                else: # 其他位置
                    temp[col] = matrix[row][col] + min(dp[col], dp[col+1],dp[col-1]) # 计算当前点到达点的最小路径
            dp = temp.copy()

        return min(dp)

# 代码简化 记忆化搜索 从上到下 这里是正着存每个位置的最短路径从起点开始 上面的是倒着存从终点开始
class Solution_optimize:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        f = [inf] + matrix[0] + [inf] # +可以直接拼表 首尾加inf完美解决了边界问题 min永远取不到inf
        print(f)
        for row in matrix[1:]:# 从第二行开始
            pre = f[0]  # 充当 f[c]
            for c, x in enumerate(row): # 在需要索引和索引值的时候都用枚举
                pre, f[c + 1] = f[c + 1], min(pre, f[c + 1], f[c + 2]) + x
        return min(f)

# 递归
from math import inf
class Solution2:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # dfs(r, c) 表示从 matrix[r][c] 出发，向上走到第一行的最小路径和
        def dfs(r: int, c: int) -> int:
            if c < 0 or c >= n:  # 出界
                return inf # 我一直就在想这个出界的问题怎么解决 因为既要一直往后走剩下的又不能返回具体值 设置inf很好的避免了会选到的问题 min用inf max用-inf
            if r == 0:  # 到达第一行
                return matrix[0][c]
            return min(dfs(r - 1, c - 1), dfs(r - 1, c), dfs(r - 1, c + 1)) + matrix[r][c]
        return min(dfs(n - 1, i) for i in range(n))  # 枚举起点，取最小值 对每个终点都求最小路径最后取最小的 和第一种方法思想一样


matrix = [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]
print(Solution().minFallingPathSum(matrix))
print(Solution_optimize().minFallingPathSum(matrix))
print(Solution2().minFallingPathSum(matrix))