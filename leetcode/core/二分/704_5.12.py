# 二分查找
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target
# 写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
from typing import List
import bisect

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = -1, len(nums)  # 开区间 (left, right) 用开区间写法 外扩一单位
        while left + 1 < right:  # 区间不为空
            mid = (left + right) // 2
            # 循环不变量：
            # nums[left] < target
            # nums[right] >= target
            if nums[mid] < target:
                left = mid  # 范围缩小到 (mid, right)
            else:
                right = mid  # 范围缩小到 (left, mid)
        return right if right < len(nums) and nums[right] == target else -1 



# 开区间写法
def lower_bound3(nums: list[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        # 循环不变量：
        # nums[left] < target
        # nums[right] >= target
        if nums[mid] < target:
            left = mid  # 范围缩小到 (mid, right)
        else:
            right = mid  # 范围缩小到 (left, mid)
    return right
# lower_bound3(nums, target) 等价于 bisect_right(nums, target)是二分查找的通用写法
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        i = lower_bound3(nums, target)  # 选择其中一种写法即可
        return i if i < len(nums) and nums[i] == target else -1


nums = [1,3,5,6,6,8]
target = 6
print(Solution().searchInsert(nums, target)) # Output: 2
print(Solution2().search(nums, target)) # Output: 2

