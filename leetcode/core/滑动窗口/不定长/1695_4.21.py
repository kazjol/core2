# 删除子数组的最大得分
# 数组 哈希表 滑动窗口
# 给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素和 。
#
# 返回 只删除一个 子数组可获得的 最大得分 。
#
# 如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

# 返回包含 无重复元素的和最大的子数组
# 无重复元素就是包含了数组中出现的全部的元素，并且没有重复的元素。
# 只要不是重复直接往里面放就行了

# 示例：
# 输入：nums = [5,2,1,2,5,2,1,2,5]
# 输出：8
# 解释：最优子数组是 [5,2,1] 或 [1,2,5]
import collections
from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        ch = set(nums)

        score = 0
        c_sum = 0
        dict = collections.defaultdict(int)
        left,right = 0,0 # 初始化滑动窗口

        for right,val in enumerate(nums):

            dict[val] += 1 # 记录遍历的元素
            c_sum += val # 记录当前窗口和
            # right += 1  right+1一般都放在全部执行结束后 放在前面会导致越界

            # 如果元素没凑齐就不动窗口直接往里面加


            while dict[val] > 1: # 先调函数再放参数

                dict[nums[left]] -= 1
                c_sum -= nums[left]
                left += 1


            score = max(score,c_sum) # 没重复就直接往里面加



        return score

nums = [4,2,4,5,6]
print(Solution().maximumUniqueSubarray(nums)) # Solution（）后面有个括号别忘了 是个形参 空值是self也就是初始化了一个Solution对象 Solution（）调用默认的构造函数



print("\n\n")
a = {1, 2, 3, 1, 1} # 集合{}自动去重
print(a)
if a == a:
    print(a)
