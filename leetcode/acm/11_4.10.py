# 贪心 双指针
# 不要纠结贪心算法为什么能解决问题，只要找到最优解即可
# 贪心算法的思路是，每次都选择当前最优的方案，直到无法再优化，也就是找到全局最优解。
# 盛最多水的容器

# 选择更高的就是贪心算法的思路，每次都选择当前最优的方案，直到无法再优化，也就是找到全局最优解。

# 答案是两端遍历 谁更小就移动谁然后更新max_area 直到两端相遇 面积就是两端距离的乘积

# 容积取决于更短的柱子和中间宽度 如果每次保留更短的柱子会导致宽度和高度同时减小所以后续的结果不可能更大
# 所以每次保留更高的柱子 实际上这是一种反证法的思路 能够减少一半的计算量
# 移动两根柱子之间更短的那根柱子，才有可能在宽度一定变小的情况下，找到一个更高的水面，从而使得面积有可能更大。
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                max_area = max(max_area, height[left] * (right - left))
                left += 1
            else:
                max_area = max(max_area, height[right] * (right - left))
                right -= 1
        return max_area

height = list( map(int,input().split(',')))
print(Solution().maxArea(height))