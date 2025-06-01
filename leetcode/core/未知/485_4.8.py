# 最大连续的1的个数
# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
# 遍历数组 用count记录当前连续1的个数，如果遇到0则将count置0，记录最大值。
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0 # 存更大的count
        for i in range(len(nums)): # 遍历数组
            # 遇到1则count+1计数
            if nums[i] == 1:
                count += 1
                # 记录最大值 max和min函数的使用
                max_count = max(max_count, count)
            # 遇到0则count置0
            else:
                count = 0
        return max(max_count, count)
nums = [1,1,0,1,1,1,0,1,1,1,1,1]
print(Solution().findMaxConsecutiveOnes(nums)) # 3