# 不同路径
# dp 数学 组合数

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？
#



# 记录上一次的状态 同时记录mn的剩余值
# 递归 记录某点的状态
# 到一个点的方式有两种（i-1，j）和（i，j-1）从两个点到（i，j）
# dfs(i,j)=dfs(i-1,j)+dfs(i,j-1) 用两个栈分开算然后求和
# python 可以用装饰器 否则要用memo哈希表记录点的状态避免重复计算
# 递归边界 进入：（m-1,n-1） 单层跳出：i==0 或 j==0

# 递归栈超时
from functools import cache
import math
from my_python_lib import timing_decorator
from my_python_lib import memory


@cache
@timing_decorator
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        def dfs(i:int,j:int)->int:
            if i == 0 or j == 0:# 边界为0了 这个栈开始出栈 因为单边界为0剩下走法只有一种了
                return 1
            if i<0 or j <0:# 走不到
                return 0

            return dfs(i-1,j) + dfs(i,j-1) # 跳到m或n为0的时候开始退栈起始值为1

        return dfs(m-1,n-1) # 递归入口 给dfs传入参数m-1和n-1对应的ij接收

# 用组合数学
# 因为一次只能走一步所以走的总步数是不变的 对横m纵n的位置来说 要走m+n-2步 在总步数里要挑m个机会选择往右走那剩下一定是往下走
@timing_decorator
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:

        return math.comb(m+n-2,m-1) # 因为对三个格只需走两步就到最后一个格 计算Cmn的函数



# 二维数组分行列遍历 然后记录 再用递推式
@timing_decorator
class Solution3:

    def uniquePaths(self, m: int, n: int) -> int:
        # 设置二维数组 dp 用来储存到达每个位置时不同路径的数量
        # dp[0][0] 表示从第 0 行第 0 列到达第 0 行第 0 列时不同路径的数量
        # dp[0][i] 表示从第 0 行第 0 列到达第 0 行第 i 列时不同路径的数量
        # dp[j][0] 表示从第 0 行第 0 列到达第 j 行第 0 列时不同路径的数量
        # dp[i][j] 表示从第 0 行第 0 列到达第 i 行第 j 列时不同路径的数量
        dp = [[0] * n for _ in range(m)]

        # 初始化 dp[0][0]，
        # dp[0][0] 表示从第 0 行第 0 列到达第 0 行第 0 列时不同路径的数量
        # 仅此一条，别无分路
        dp[0][0] = 1

        # i 从 1 遍历到 m - 1
        # 获取从第 0 行第 0 列到达第 j 行第 0 列时不同路径的数量
        # 由于每次只能向下或者向右移动一步，此时只能向下移动一步
        # 所以，只能一直向下走，只有这一条路径
        for i in range(1, m):
            # 仅此一条，别无分路
            dp[i][0] = 1

        # j 从 1 遍历到 n - 1
        # 获取从第 0 行第 0 列到达第 0 行第 i 列时不同路径的数量
        # 由于每次只能向下或者向右移动一步，此时只能向右移动一步
        # 所以，只能一直向右走，只有这一条路径
        for j in range(1, n):
            # 仅此一条，别无分路
            dp[0][j] = 1

        # 初始化了第一行第一列


        # 接下来从第 1 行到第 m - 1 行
        # 从第 1 列到 n - 1 列
        # 填充二维数组 dp 里面的值
        # dp[i][j] 表示从第 0 行第 0 列到达第 i 行第 j 列时不同路径的数量
        for i in range(1, m):

            for j in range(1, n):
                # 由于每次只能向下或者向右移动一步
                # 位置 (i,j) 的不同路径的数量是由
                # 1、上边位置 dp[ i - 1 ][j] 的不同路径的数量
                # 2、左边位置 dp[i][ j - 1 ] 的不同路径的数量
                # 两者之和获取到的
                # 左边和上边的元素和
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # dp[ m - 1][ n - 1 ] 表示从第 0 行第 0 列到达第 m - 1 行第 n - 1 列时不同路径的数量
        # 即到达终点的数量
        # 返回这个结果即可
        return dp[m - 1][n - 1]

@timing_decorator
class Solution4:
    def uniquePaths(self, m: int, n: int) -> int:
        # 使用一维数组优化空间复杂度
        dp = [1] * n  # 初始化第一行，每个位置都是1

        # 从第二行开始计算
        for i in range(1, m):
            for j in range(1, n):
                # dp[j] 表示当前行的第j列
                # dp[j-1] 表示当前行的第j-1列
                # 更新dp[j]为左边和上边的路径数之和
                dp[j] += dp[j - 1]

        return dp[-1]  # 返回最后一列的值



m = 7
n = 3
print('递归栈 双栈',Solution().uniquePaths(m,n),'\n\n') # Solution().函数() Solution带（）是先初始化了一个实例再调用
print('组合数学',Solution2().uniquePaths(m,n),'\n\n')
print('二维数组',Solution3().uniquePaths(m,n),'\n\n')
print('一维数组 二维数组优化',Solution4().uniquePaths(m,n))