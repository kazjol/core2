# 最长递增子序列的个数
# 树状数组 数组 线段树 dp
from bisect import bisect_left # binary select


from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # LIS: 最长递增子序列
        # 创建一个数组dp，用于存储以每个元素结尾的最长递增序列的长度
        dp = [1] * n

        # count[i]: 以nums[i]为结尾的LIS的个数
        count = [1] * n

        # 初始化
        maxLength = 1

        # 从0开始，填充dp数组
        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue

                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[i] == dp[j] + 1:
                    count[i] += count[j]

            maxLength = max(maxLength, dp[i])

        result = 0
        for i in range(n):
            if dp[i] == maxLength:
                result += count[i]

        return result






