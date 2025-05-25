# 最长重复数组
# 数组 二分 哈希 滚动哈希 dp 滑动窗口

# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度


# 状态数组dp是二维的 dp[i][j]分别保存nums1[0:i]和nums2[0:j]的最长公共子数组的长度。
# 初始化设为dp[i+1][j+1]是直接跳过了了[0][0]的状态
# 状态转移方程：
# dp[i][j] = dp[i-1][j-1] + 1
from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if x == y:
                    f[i + 1][j + 1] = f[i][j] + 1
        return max(map(max, f))  # 所有 f[i][j] 的最大值
    # map(max,f) 把f的每个子列表取最大值并逐个返回 map函数返回迭代器
