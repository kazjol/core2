# 爬楼梯
# 记忆化搜索  动态规划

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#



# 还是斐波那契数列  台阶数增多继承之前的走法
# 但是这里需要做时间优化 因为给的数字更大2^N超时
from functools import cache
@cache
class Solution:
    def climbStairs(self, n: int) -> int:

        return n if n <= 2 else self.climbStairs(n-1) + self.climbStairs(n-2)
n = 4
print(Solution().climbStairs(n))





# 状态只记录i-1 i-2 两个状态 然后做状态转移得到i的状态
# 当前的状态只和前两阶有关 保存前两阶的状态 然后做状态转移
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n < 2: # 只有1阶和没有阶梯
            return n

        a = 1 # 第一阶走法 后续用来记录i-2的状态

        b = 2 # 第二阶走法 后续用来记录i-1的状态

        for i in range(2, n): # 从第三阶开始
            t = b # 保存i-2的状态
            b =a + b
            a = t



        return b
n = 4
print(Solution2().climbStairs(n))