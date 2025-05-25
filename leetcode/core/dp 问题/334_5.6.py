# 递增的三元子序列
# 数组 贪心
from bisect import bisect_left
# 数组中出现递增的连续三个元素

# 求最长递增子序列的长度 大于等于3

from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        g = []# 保存递增序列
        for i, num in enumerate(nums):
            if not g or num > g[-1]:# 大于最后一个元素
                g.append(num)
            else:
                g[bisect_left(g, num)] = num# 用二分查找函数插入元素 bisect_left(g, num) 返回插入位置

        if len(g) < 3:
            return False



        return True
nums = [1,2,3,4,5]
print(Solution().increasingTriplet(nums))