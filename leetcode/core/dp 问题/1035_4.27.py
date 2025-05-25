# 不相交的线
# 数组 dp
from math import inf
# 只给两个数组  连线不能相交一个数只能用一次  求最大连线数

# 出现相交的情况 i>i' 且 j<j' 判断条件

# 求最长公共子序列  动态规划
from functools import cache
from typing import List
class Solution:
    def maxNonOverlapping(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]     # 定义dp数组二维 因为跳过第一行第一列所以是+1行列
        for i ,num1 in enumerate(nums1):# 跳过第一行第一列
            for j, num2 in enumerate(nums2):
                if num1 == num2:# 匹配斜向继承加1
                    dp[i+1][j+1] = dp[i][j] + 1 # 从列表的第0个字符开始 但是存dp从dp[1][1]开始
                else:# 不匹配继承更新最大状态
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])



        return dp[len(nums1)][len(nums2)]
class Solution2:
    def maxUncrossedLines(self, s: List[int], t: List[int]) -> int:
        n, m = len(s), len(t)
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if s[i] == t[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        return dfs(n - 1, m - 1)



nums1 = [2,1]
nums2 = [1,2,1,3,3,2]
print(Solution().maxNonOverlapping(nums1, nums2))