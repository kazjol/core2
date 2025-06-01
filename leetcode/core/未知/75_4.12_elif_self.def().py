# 颜色分类
# 数组 双指针 排序
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，
# 使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 必须在不使用库内置的 sort 函数的情况下解决这个问题。


# 只包含三个颜色也就是0，1，2的数组
# 双指针法

# right遇到0 就把arr[right]和arr[left]交换 然后left右移
# 直到 left>=right 结束 开始查下一个元素1


# 特殊情况可能是 全部都是0 全部都是1 全部都是2 可能没0 可能没2 可能没1
print('mine')
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        left = 0
        right = len(nums)-1

        if 0 in nums:
            # 遍历选0
            while left < right:
                # 左边遇到0 位置正确直接右移
                if nums[left] ==  0:
                    left += 1
                # 右边遇到0 与左边交换然后左指针右移 右指针左移继续遍历
                elif nums[right] == 0:
                # 要非常注意if-elif//if-if 两者的区别
                # if-elif只执行一个
                # if-if 可能执行0，1，2的情况 两个判断之间无关

                    t = nums [left]
                    nums[left] = nums[right]
                    nums[right] = t
                    left += 1
                    right -= 1
                # 左右都没遇到0 右指针左移继续遍历
                elif nums[left] != 0 and nums[right] != 0:
                    right -= 1


        # 这个非常关键 是在加与不加的情况下报错然后分析错误点 想到的漏洞
        # 如果遍历结束left停在0的位置 右指针停在0的位置 就要右移
        if nums[left] == 0:
            left += 1


        if 1 in nums:
            # 遍历选1

            right = len(nums)-1
            while left < right:
                if nums[left] ==  1:
                    left += 1
                elif nums[right] == 1:
                    t = nums [left]
                    nums[left] = nums[right]
                    nums[right] = t
                    left += 1
                    right -= 1
                elif nums[left] != 1 and nums[right] != 1:
                    right -= 1

            # 选完0，1剩下的都是2了
nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)

print('\n\nod解法')


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        # left  指向数组的开始的位置，它指向的位置左侧都是 0
        left = 0

        # right  指向数组的结束的位置，它指向的位置右侧都是 2
        right = len(nums) - 1

        # index 指向数组的开始位置
        index = 0

        # index 向后移动，当它越过 right 时跳出循环，不需要再判断了
        # 因为此时说明 index 右侧的都已经是 2
        while index <= right:

            # 获取当前的元素值
            cur = nums[index]

            # 如果 index 位置上的元素值为 0
            if cur == 0:
                # 说明是红色，要放在最前面去
                # 最前面的那个元素被 left 指着，所以让 index 指向的元素和 left 指向位置上的元素进行交换

                self.swap(nums, left, index)

                # index 可以向后移动
                index += 1

                # left 可以向后移动，它的左侧区域都是 0
                left += 1

                # 如果 index 位置上的元素值为 1
            elif cur == 1:
                # 说明是白色，就应该放在中间，不用管它，继续移动 index
                index += 1

                # 如果 index 位置上的元素值为 2
            elif cur == 2:

                # 说明是蓝色，要放在最后面
                # 所以让 index 指向的元素和 right 指向位置上的元素进行交换
                self.swap(nums, right, index)

                # 由于原先 right 指向的元素可能为 0、1、2 这三种的任何一种
                # 交换到了 index 后，还需要继续观察一轮，所以 index 先不移动
                right -= 1

    # 通过中间变量，交换两个元素的值
    # nums[i] 的值变为了 nums[j] 的值
    # nums[j] 的值变为了 nums[i] 的值


    # 用到了类里面成员函数及元素的自由调用 self类定义的对象 self.函数名 self.变量名对类内定义的调用
    def swap(self, nums: List[int], i: int, j: int):
        # 使用临时变量 temp，保存 nums[i] 的值
        temp = nums[i]

        # nums[i] 的值修改为 nums[j] 的值
        nums[i] = nums[j]

        # nums[i] 的值修改为 temp 的值
        nums[j] = temp
nums = [2,0,2,1,1,0]
Solution2().sortColors(nums)
print(nums)