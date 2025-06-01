#数组 双指针 *二分查找*->分左右半表查 能这样是因为数组是有序的


#两数之和 II - 输入有序数组
# 给你一个 下标从 1  开始的整数数组 numbers ，该数组已按 非递减顺序排列=> ，请你从数组中找出满足相加之和等于目标数 target 的两个数。
# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
# 你可以假设每个输入 只对应唯一的答案一定有解 ，而且你 不可以 重复使用相同的元素。
# 你所设计的解决方案必须只使用 常量级 的额外空间。



# 数组是有序的 如果无序则先用sort（）排序 再用二分查找
# 双指针法
print("双指针法:背向双指针")


from typing import List
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # 定义左侧指针left，指向数组中第一个元素
        # 默认从数组的索引为 0 的位置开始
        left = 0

        # 定义右侧指针 right，指向数组中最后一个元素
        right = len(numbers) - 1

        # 两个索引向内移动
        # left 向右移动
        # right 向左移动
        while left < right: # 可以写成while 1 因为一定会有答案 不会死循环
            # 1、如果左侧指针与右侧指针所指向的元素和等于目标值，则返回结果
            if numbers[left] + numbers[right] == target:
                # 题目说明下标从 1 开始，就操作一下
                return [left + 1, right + 1]


            # 2、如果左侧指针与右侧指针所指向的元素和小于目标值
            elif numbers[left] + numbers[right] < target:
                # 一点一点调整
                # 因为数组是升序排列的，为了让两数之和变大一些
                # 因此应将左侧指针向右移动一位
                left += 1

            # 3、如果左侧指针与右侧指针所指向的元素和大于目标值
            elif numbers[left] + numbers[right] > target:

                # 因为数组是升序排列的，为了让两数之和变小一些
                # 因此应将右侧指针向左移动一位
                right -= 1


numbers = [2,3,4]
target = 6
print(Solution1().twoSum(numbers, target)) # [1,2]

print('\n\n\n')


# 二分查找法
print("二分查找法")
from bisect import bisect_left# binary search 二分查找模块 调用这个函数能用二分查找的算法查到目标值 实现了二分 (bisection) 算法 的模块
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            x = target - numbers[i]
            j = bisect_left(numbers, x, lo=i + 1) # lo：location

            # 具体来说，bisect_left(a, x, lo=0, hi=len(a)) 会在有序列表 a 中查找 x 应该插入的位置，
            # 使得插入后列表仍然有序。如果 x 已经存在列表中，
            # 它将返回 x 可以插入的位置，以保持列表顺序不变（即插入在已存在元素的左侧）。


            # bisect_left 函数:
            # 参数:
            # a: 一个有序列表。
            # x: 要查找的值。
            # lo: 查找范围的起始索引（包含），默认为 0。
            # hi: 查找范围的结束索引（不包含），默认为列表的长度。
            # 返回值:
            # 如果 x 存在于列表 a 中，返回其下标；否则返回插入位置。



            if j < n and numbers[j] == x:
                return [i + 1, j + 1]
numbers = [2,3,4]
target = 6
print(Solution1().twoSum(numbers, target)) # [1,2]




