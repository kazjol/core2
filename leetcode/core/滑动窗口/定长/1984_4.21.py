# 1984. 学生分数的最小差值
# 数组 排序 滑动窗口

# 给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。
#
# 从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。
#
# 返回可能的 最小差值 。

# 输入：nums = [9,4,1,7], k = 2
# 输出：2
# 解释：选出 2 名学生的分数，有 6 种方法：
# - [9,4,1,7] 最高分和最低分之间的差值是 9 - 4 = 5
# - [9,4,1,7] 最高分和最低分之间的差值是 9 - 1 = 8
# - [9,4,1,7] 最高分和最低分之间的差值是 9 - 7 = 2
# - [9,4,1,7] 最高分和最低分之间的差值是 4 - 1 = 3
# - [9,4,1,7] 最高分和最低分之间的差值是 7 - 4 = 3
# - [9,4,1,7] 最高分和最低分之间的差值是 7 - 1 = 6
# 可能的最小差值是 2
# 最大和最小的差值

# 遍历更新 贪心 先排序
# 定长的滑动窗口大小为k
# 维护一个窗口，窗口内的元素从左到右递增

from typing import List
class Solution:
        def minDifference(self, nums: List[int],k: int) -> int:
            min_sub = max(nums)
            nums.sort() # 最小差值一定是在相邻的几个数之间
            left, right = 0, k-1
            for right in range(k-1, len(nums)):
                cur_sub = max(nums[left:right + 1]) - min(nums[left:right + 1])
                left += 1

                min_sub = min(min_sub, cur_sub)

            return min_sub


nums = [9,4,1,7]
k = 2
print(Solution().minDifference(nums,k)) # 2















a = [1,2,3,4,5]
print(sorted(a))
