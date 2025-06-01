# 删除有序数组的重复项 II
# 给你一个有序数组 nums ，请你原地删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。  不能用中间数组
# 还是原地操作问题现在就要多加一个count变量来记录重复元素的个数，如果count大于等于2，大于2的最多保留2个
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lth = len(nums)
        i = 0
        j = 1
        count = 1
        cur = 0
        while j <lth:
            if nums[i]==nums[j]:
                j += 1
                count += 1

            else:
                if count >= 2: # 只存两个所以 存的位置也是有规律的
                    nums[cur] = nums[i]
                    cur += 1
                    nums[cur] = nums[i]
                    cur += 1
                    count = 1
                    i = j
                    j = i + 1
                else:
                    nums[cur] = nums[i]
                    cur += 1
                    i = j
                    j = i + 1
        if i<lth-1: # 对待保存的最后一个元素做判断是否>=2次 因为此时j已经大于lth了 进while会访问越界
            nums[cur] = nums[i]
            cur += 1
            nums[cur] = nums[i+1]
            cur += 1
        else:
            nums[cur] = nums[i]
            cur += 1
        length = cur
        del nums[cur:lth] # 删除超出长度的元素

        return length


# 这里需要保证把结尾删除
nums = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(nums))
print(nums)




# 更快解法
class Solution2(object):
    def removeDuplicates(self, nums):

        # 指针 slow 指向即将被赋值的位置
        slow = 0

        # 开始对数组进行遍历
        for fast in range(len(nums)):# 快慢指针 初始都是0

            # 进行筛选
            if slow < 2 or nums[fast] != nums[slow - 2]:
                # 赋值
                nums[slow] = nums[fast]
                # slow 移动
                slow += 1 # 边比较边存

        # 获取结果
        return slow




print('*******************************************************************************')
# 列表删除元素
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # 删除索引为2的元素，即3

my_list = [1, 2, 3, 4, 5]
my_list.remove(3)  # 删除值为3的元素

my_list = [1, 2, 3, 4, 5]
removed_element = my_list.pop(2)  # 删除索引为2的元素，并返回该元素  pop()方法默认删除最后一个元素

my_list = [1, 2, 3, 4, 5]
del my_list[2:5]  # 删除索引2到索引4（不包括5）的元素 包括起始不包括结束
print(my_list)  # 输出: [1, 2, 4, 5]

my_list = [1, 2, 3, 4, 5]
my_list = [x for x in my_list if x != 3]  # 删除值为3的所有元素 去除了所有值为3的元素
print(my_list)  # 输出: [1, 2, 4, 5]





