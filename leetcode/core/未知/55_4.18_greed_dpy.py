# 跳跃游戏
# 贪心 数组 动态规划

# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

# 示例 1：
# 输入：nums = [3,2,1,0,4]
# 输出：false

print('灵神 dp greedy')
# 这个体现了动态规划
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0 # 每次都保存跳最远可以到达的位置 如果遍历的时候跳最远的位置到不了最后一个位置，则返回false
        for i, jump in enumerate(nums): # 从头到尾遍历位置 可以省略写nums[i]简化代码
            if i > mx:  # 无法到达 i
                return False
            mx = max(mx, i + jump)  # 从 i 最右可以跳到 i+jump 少写一个if判断 简化代码
        return True



nums = [5,9,3,2,1,0,2,3,3,1,0,0]
print(Solution().canJump(nums))


print('\n\nmine')
from typing import List
class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        # 每次保存能跳到的最远距离
        # 遍历整个数组 如果最远距离到不了下标则false

        maxjump = 0

        for index in range(len(nums)):

            if maxjump >= index and maxjump < len(nums) - 1:
                if maxjump < nums[index] + index:


                    maxjump = nums[index] + index
                    # print(maxjump)

            if maxjump >= len(nums) - 1:
                return True

            elif maxjump < index:
                return False
nums = [3,0,8,2,0,0,1]
print(Solution3().canJump(nums))


print('\n\nod 解法')

class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        # 设置数组，保存每个位置如果在当前位置出发，一次性可以到达的最远位置
        # 比如 nums 为 [ 2 , 4 , 5 , 3 , 1 , 0 , 6]
        # 那么对于 2 来说，可以跳到最远的位置是 5 那个位置，即索引为 2 的那个位置
        # 对于 4 来说，可以跳到最远的位置是 0 那个位置，即索引为 5 的那个位置
        # 对于 5 来说，可以跳到最远的位置超过了数组的范围

        jump = list(range(len(nums)))

        # 初始化 jump
        for i in range(len(nums)):
            # jump[i] 就是当前的索引值 i 加上该位置可以跳跃的最大长度 nums[i]
            # 初始化了一个边界数组 每个位置最远能跳到哪里
            jump[i] = i + nums[i]

        # 从数组下标为 0 的位置开始起跳，索引为 0
        index = 0

        # 设置变量 maxJump，用来记录可以到达的最远位置
        # 从数组下标为 0 的位置开始起跳，此时记录的最远距离为 jump[0]
        # 逐个求最远距离
        maxJump = jump[0]

        # 开始起跳
        # 直到 index 到达数组尾部，index >= nums.length

        # 遍历整个数组一步一步的跳然后比较

        # 当maxJump 小于下一个位置的索引时说明连下一个位置都无法到达则一定是跳不动了
        while index < len(nums) and index <= maxJump:

            # 如果发现可以跳到的最远距离 maxJump 小于 jump[index]
            # 也就是边界值可以满足可以跳到 说明可以向后继续

            # 因为是逐个遍历的所以maxjump要和每个位置的最远距离比较
            if maxJump < jump[index]:
                # 那么需要更新 maxJump
                maxJump = jump[index]

            # index 向前移动
            index += 1

        # 循环结束后，如果 index 已经访问了 nums 中所有的元素
        if index > len(nums) - 1:
            # 说明可以到达最后一个下标
            print(len(nums))
            return True

        # 否则说明无法到达最后一个下标
        return False
nums = [5,9,3,2,1,0,2,3,3,1,0,0]
print(Solution2().canJump(nums))




# dp 解法
print('\n\ndp')
from functools import cache
class Solution4:
    def canJump(self, nums: List[int]) -> bool:

        """
        如果第 i - 2 个节点能够到达 i -1 那么判断是否能够到达 i -2 ,
        否则对 i - 3 进行判断
        """

        n = len(nums)
        @cache
        def dfs(i,target):
            # print(i,target)
            if target == 0:
                return True
            if i < 0:
                # print(i,target)
                return False

            if i + nums[i] >= target:
                return dfs(i-1,i)
            else:
                return dfs(i-1,target)

        return dfs(n-2,n-1)

