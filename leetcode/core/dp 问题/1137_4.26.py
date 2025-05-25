# 1137. 第 N 个泰波那契数
# 记忆化搜索 dp 数学

# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
#
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
from functools import cache
class Solution:
    @cache
    def tribonacci(self, n: int) -> int:

        t1, t2, t3 = 0, 1, 1
        if n < 3: # 因为n=3时求t3，给的是从t0开始的所以t3实际是第四个元素
            return 0 if n == 0 else 1

        for i in range(3, n+1): # n=4时是求t4，所以遍历到n+1
            a = t3
            b = t2
            t3 = t1 + t2 + t3
            t2 = a
            t1 = b




        return t3



n = 4
print(Solution().tribonacci(n)) # Output: 4