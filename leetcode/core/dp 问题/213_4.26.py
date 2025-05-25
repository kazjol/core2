# 打家劫舍II
# dp 数组

# 数组的元素是连成环的 0和-1是算作相邻的 增加了边界判断问题
# 去掉第一个元素和最后一个元素的情况 取最大值
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=3: # 因为为3时也不能取两个元素
            return max(nums)

        # dp只存n-1个元素
        dp = [0] * (n-1)

        # 去掉第一个元素
        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])

        for i in range(3, n): # 从第三个元素开始是因为去掉了第一个元素
            # 这里出错因为实际dp存的位置和nums是错一个的
            dp[i-1] = max(dp[i-3] + nums[i], dp[i-2],dp[i-1])

        money = dp[-1]
        dp = [0] * (n-1)

        # 去掉最后一个元素
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n-1): # 从第三个元素开始是因为去掉了最后一个元素
            dp[i] = max(dp[i-2] + nums[i], dp[i-1],dp[i])
        money = max(money, dp[-1])
        return money
class Solution2:
    # 198. 打家劫舍
    def rob1(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for x in nums:
            f0, f1 = f1, max(f1, f0 + x)
        return f1

    def rob(self, nums: List[int]) -> int:
        return max(nums[0] + self.rob1(nums[2:-1]), self.rob1(nums[1:])) # 直接切片去除第一个元素和最后一个元素 而且也包含了只有一个元素的情况

nums = [1,2,3,1]
print(Solution().rob(nums))
print(Solution2().rob(nums))