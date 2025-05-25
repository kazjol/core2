# 移除元素
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
# 假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：
# 更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。   nums 的其余元素和 nums 的大小并不重要。*不用处理尾元素
# 返回 k。

# 不能有辅助空间

# 元素顺序不可变的话 就要平移套for循环
# 元素顺序可变 python里有remove方法可以直接删除元素 remove只会删除第一个匹配项 所以要用while循环删除所有匹配项

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

            for i in range(len(nums)):
                # 数组里有才能删
                if val in nums:

                    nums.remove(val)
            return len(nums)

nums = [3,2,2,3]
val= 3

print(Solution().removeElement(nums,val))
print(nums)



#remove只会删除第一个匹配项 所以要用while循环删除所有匹配项
print('**************************************************************************************************************')

nums = [0,1,2,2,3,0,4,2]
res = nums.remove(2)
print(nums)
print(res)
