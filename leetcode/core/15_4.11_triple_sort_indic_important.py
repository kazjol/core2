# 三数之和
# 排序 双指针 数组
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。


# 三元组 triple = (nums[i], nums[j], nums[k])
# 初始化三元组 tuple()函数
# 初始化多个三元组 triples = [(1, 'apple', 3.14),(2, 'banana', 2.71),(3, 'cherry', 1.61)]
# 遍历三元组 for triple in triples:
#     if triple[0] + triple[1] + triple[2] == 0:
#         print(triple)
# 也可以以list[list[]]的形式存在[[1,2,3],[2,3,4],[3,4,5]]列表元素是列表形式

# 先排序再双指针遍历
# 转三数和为两数和



print('od 解法')
from typing import List
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 题目存在多组解，每一组解都是一个数组，所以使用二维数组存储所有的解
        ans = []

        # 边界情况判断
        if nums == None or len(nums) < 3:
            return ans

        # 先将数组进行排序操作，从小到大
        nums.sort()

        # 开始遍历整个数组
        # 在遍历的过程中，观察设置的三个位置的元素之后的大小
        # num[i] 为从左到右观察过去的元素
        # left 为从 i 到 len - 1 的元素  left是中间元素
        # right 为从 len - 1 向左移动到 i 的元素
        for i in range(len(nums)):

            # 如果发现 nums[i] > 0 ，由于 nums 是递增序列，left 在 nums[i] 的右侧，right 也在 nums[i] 的右侧
            # 那么 num[i]、nums[left]、nums[right] 都大于 0
            # 说明这三数之和一定大于 0 ，结束循环

            if nums[i] > 0:
                break

            # 答案中不可以包含重复的三元组，所以需要执行一个去重的操作
            # 比如这个输入 [-4,-1,-1,0,1,2]
            # i 指向的为第一个 -1 时，left 指向的元素值为 0 ，right 指向的元素值为 1
            # i 指向的为第二个 -1 时，left 指向的元素值为 0 ，right 指向的元素值为 1
            # 这两组解都是 [ -1 , 0 , 1]，所以需要去重
            # 也就是访问到同样的数的时候跳过 因为是排好序的 所以相同的数一定是
            if i > 0 and nums[i] == nums[i - 1]:
                continue # continue跳过该循环后续代码 进入下一个循环
            #后面接的都是else
            # left 为从 i 到 len - 1 的元素，向右移动
            # 开始遍历
            # left 的起始位置就是i后面一个位置
            left = i + 1

            # right 为从 len - 1 向左移动到 i 的元素，向左移动
            right = len(nums) - 1

            # left 和 right 不断的向内移动
            # 在i固定的条件下开始遍历
            while left < right:

                # 计算这三者之和
                sum = nums[i] + nums[left] + nums[right]

                # 发现三者之和为 0
                if sum == 0:

                    # 把这个结果记录一下
                    ans.append([nums[i], nums[left], nums[right]])

                    # 答案中不可以包含重复的三元组，所以需要执行一个去重的操作
                    # 比如这个输入 [-2,0,0,2,2]
                    # i 指向的元素值为 -2 ，left 指向的元素值为第一个 0 ，right 指向的元素值为倒数第一个 2 时
                    # 它们的 sum.txt 为 0 ，如果让 ，left 向右移动一下，，right 向左移动一下，它们的 sum.txt 也为 0
                    # 但是这两组解都是 [ -2 , 0 , 2]，所以需要去重
                    # 左边遍历到同一元素



                    # *在找到第一个该三元组时 把后续的相同结果都跳过 所以在if sum.txt == 0 后面加上 while
                    while left < right and nums[left] == nums[left + 1]:
                        # 每个while是独立的 判断条件都要单独设立 所以要重复加上 left < right
                        # left 向右移动
                        left += 1

                    # 右边遍历到同一元素
                    while left < right and nums[right] == nums[right - 1]:
                        # right 向左移动
                        right -= 1

                    # 如果不存在重复的left 和 right 也要移动 并且两个同时移动而不是只移一个因为不会存在相同的解
                    # left 向右移动
                    left += 1

                    # right 向左移动
                    right -= 1

                # 如果三者之和小于 0 ，那么说明需要找更大的数
                elif sum < 0:
                    # left 向右移动
                    left += 1

                # 如果三者之和大于 0 ，那么说明需要找更小的数
                elif sum > 0:
                    # right 向左移动
                    right -= 1

        # 返回结果
        return ans
nums = [-1,0,1,2,-1,-4]
print(Solution2().threeSum(nums))

# if elif else 语句的使用只执行一个分支，后面的分支不会执行。
# if if if 是多个判断 相当于 if else if else if else 是三个分块





# .sort()和sorted（）的区别
# sort()是列表的方法，sorted()是内置函数，返回一个新的排序后的列表。
# 区别：
# 1.sort()方法是直接在原列表上进行排序，而sorted()函数是返回一个新的排序后的列表。
# 2.sort()方法没有返回值而是直接对列表进行排序 无参数，而sorted()函数返回排序后的列表。
# 3.sort()方法只能对列表进行排序，而sorted()函数可以对任意可迭代对象进行排序。

print("\n\nsort 使用\n////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
a = [-1,0,1,2,-1,-4]
a=list(sorted(a))
print(a)
b = [-1,0,1,2]
b.sort()
print(b)