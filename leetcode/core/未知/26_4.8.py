# 删除有序重复数组中的重复元素并返回最终结果的长度
# 双指针 j始终在i前面 直到元素不相等 i移动到j的位置j向前
# 结果要修改保存到nums里


# 题目要求原地操作数组 所以不能新开辟一个中间数组
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lern = len(nums)

        count = 0 # i改变了几次就录入了几个元素
        i = 0
        j = 1
        while i < lern and j < lern: # 如果已经越界就能说明当前i是最后一个不重复的元素

            if nums[i] == nums[j] :
                j += 1
            else:
                nums[count] = nums[i]
                i = j
                j = i+1
                count+=1
        nums[count] = nums[i]
        count += 1
        # return list(set(nums))才能把nums改变 参数传递

        return count

# nums后面的数不用管 其实输出在count长度外还有元素


nums = [1,1]
print(Solution().removeDuplicates(nums))
print(nums)
print(list(set(nums)))

print('************************************************************************************************')

# 更快
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int: # 不同类下用同一函数名
        # 指针 i 进行数组遍历
        n = len(nums)

        # 指针 j 指向即将被赋值的位置
        j = 0

        # 开始对数组进行遍历
        for i in range(n): # 遍历数组 range(n) 0-n-1 生成n个元素的序列

            # 进行筛选
            if i == 0 or nums[i] != nums[i - 1]:# 第一个元素或者和前一个元素不同
                # 赋值
                nums[j] = nums[i]# j就是count

                # j 移动
                j += 1

        # 获取结果
        return j
nums = [1,1]
print(Solution2().removeDuplicates(nums))