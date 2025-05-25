# 移动0
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。顺着放就行了
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。不能有额外的辅助空间。


# 用count计数0   然后从头到尾存非0元素最后再把0放到末尾
# 优化 不需要用count 把剩下的没用的空间全存0

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        cur = 0 # 当前存放非0元素的位置
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            else:
                nums[cur] = nums[i]
                cur += 1
        # 这个部分常用 处理尾元素的时候
        # 生成当前存放位置到末尾的序列
        for i in range(cur, len(nums)):
            nums[i] = 0



nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)