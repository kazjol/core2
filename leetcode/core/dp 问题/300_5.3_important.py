# 最长递增子序列
# 数组 二分 dp
from bisect import bisect_left
from functools import cache
from math import inf
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。


# 先做O（n^2)的解，遍历一遍得最长
# 遍历到下一个数字的时候新建数组空间插入 记录新长度最后取最大
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # dp[i] 表示以 nums[i] 结尾的最长递增子序列的长度 保存状态的数组
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            # 对于每个位置 i，检查之前的所有位置 j
            for j in range(i):
                if nums[i] > nums[j]:
                    # 如果 nums[i] > nums[j]，说明可以形成更长的子序列
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # 返回 dp 数组中的最大值
        return max(dp)

# 记忆化搜索 递归+缓存结果
# 把问题分解成子问题：求以每个位置结尾的最长递增子序列
# 使用递归函数 dfs(i) 表示"以 nums[i] 结尾的最长递增子序列的长度"
# res 初始为0，用来记录前面所有可能子序列的最大长度
# 遍历 i 之前的所有位置 j
# 如果 nums[j] < nums[i]，说明可以把 nums[i] 接到以 nums[j] 结尾的子序列后面
# dfs(j) 递归调用，获取以 nums[j] 结尾的最长子序列长度
# 最后 res + 1 是因为要加上当前元素 nums[i]
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        # 递归函数是对每个位置 i 计算以 i 结尾的最长递增子序列的长度
        # 和双层循环一个效果
        def dfs(i: int) -> int:
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:# 说明该元素可以接到nums[j]的后面构成递增子序列 对每个元素从头开始遍历 去构成递增子序列并更新长度的最大值
                    res = max(res, dfs(j))# 每次都只保存前面遍历元素的递增子序列长度的最大值 但是没有包含当前元素
            return res + 1  # 加一提到循环外面 
        return max(dfs(i) for i in range(len(nums)))



# 递推
class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[:i]):
                if x > y:
                    f[i] = max(f[i], f[j])
            f[i] += 1
        return max(f)

'''
很重要的思想

为什么二分插入能得到最优解：
每次替换都选择合适的位置，保证：
不会破坏递增性
让每个长度的子序列的结尾元素尽可能小
后面更容易接上更大的数
长度增加的条件很严格：只有当新数比所有现有数都大时
替换操作不会影响长度，但会让后面的数更容易接上
关键点：
长度增加的条件很严格，保证了长度的正确性
替换操作优化了后续的可能性
二分查找保证了替换位置的正确性
最终 g 的长度就是最长递增子序列的长度

长度增加的条件很严格，保证了不会多算
替换操作优化了后续的可能性，保证了不会少算
二分查找保证了替换位置的正确性
最终我们只关心长度，不关心具体序列
'''
# 贪心 + 二分
# 我的原有思路 只比最后一个数小就替换掉最后一个数
# 但是这样会破坏原有递增子序列的结构 导致结果不正确
# 比如 [0,1,0,3,2,3] 这个例子 按照我的思路会返回2 但是正确答案是3
# 因为 0 1 2 3 是一个递增子序列 但是按照我的思路 0 1 0 3 2 3 会返回2
# 因为 0 1 0 3 2 3 中 0 1 0 是一个递增子序列 但是 3 2 3 是一个递减子序列 所以结果是2
# 所以需要使用贪心 + 二分来解决这个问题 

# 关键区别：
# 你的方法：只考虑替换最后一个数
# Solution4：使用二分查找找到合适的位置，可能替换中间的数
# 这样可以保证：
# 不会破坏递增性
# 让每个长度的子序列的结尾元素尽可能小
# 不会形成非递增序列
class Solution4:
    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []# 保存的不是最长递增子序列 而是len（g）的结果是当前最长递增子序列的长度
        # 当 x 比 g 中所有数都大时，可以形成更长的子序列（长度加1）
        # 当 x 可以替换某个位置的数时，我们选择替换，因为：
        # 替换不会影响当前长度
        # 替换后的数更小，后面更容易接上更大的数
        for x in nums:
            j = bisect_left(g, x) 
            # bisect_left 是 Python 标准库 bisect 模块中的一个函数，用于二分查找。让我详细解释一下：
            # 基本功能：
            # bisect_left(g, x) 在已排序的列表 g 中查找 x 应该插入的位置
            # 返回的位置满足：所有在它左边的元素都小于 x
            # 如果 x 已经在列表中，返回最左边的位置
            if j == len(g):  # >=x 的 g[j] 不存在
                g.append(x)
            else:
                g[j] = x
        return len(g)


# 测试用例
nums = [10,9,2,5,3,7,101,18,0]
print(Solution().lengthOfLIS(nums))  # 输出: 4
# print(Solution2().lengthOfLIS(nums))  # 输出: 4
# print(Solution3().lengthOfLIS(nums))  # 输出: 4
print(Solution4().lengthOfLIS(nums))  # 输出: 4
