# 打家劫舍
# 数组 dp

# 取不连续的数的最大和

# 示例：
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。

from typing import List
class Solution:
    # 当前的状态和前两个元素的状态有关 对于当前元素取或不取比较大小 然后取max值更新当前元素的状态
    # dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    def rob(self, nums: List[int]) -> int:
        if len(nums) <3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1] # 最后一个元素的状态 -1越界会折返





nums = [2,7,9,3,1]
print(Solution().rob(nums))