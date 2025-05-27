# 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# nums 为 无重复元素 的 升序 排列数组
# 请必须使用时间复杂度为 O(log n) 的算法 log n二叉树
# 二分 只能用于有序数组 ps:二分查找在python里可以直接用 bisect_left() bisect_right()返回左右边界

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left



# 因为是返回待插入的位置所以 所以当没有target的时候就返回大于target的值的最小值
# lower_bound 返回最小的满足 nums[i] >= target 的 i
# 如果数组为空，或者所有数都 < target，则返回 len(nums)
# 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]

# 闭区间写法 lower_bound是通用的二分查找的方法 且可读性更好
def lower_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left

# 左闭右开区间写法
def lower_bound2(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)  # 左闭右开区间 [left, right)
    while left < right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right)
        else:
            right = mid  # 范围缩小到 [left, mid)
    return left  # 或者 right

# 开区间写法
def lower_bound3(nums: list[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空 取不到left右边界也取不到左边right右边界
        mid = (left + right) // 2
        # 循环不变量：
        # nums[left] < target
        # nums[right] >= target
        if nums[mid] < target:
            left = mid  # 范围缩小到 (mid, right)
        else:
            right = mid  # 范围缩小到 (left, mid)
    return right # 返回left因为最后的返回条件是left+1==right 要返回第一个大于等于的数


class Solution2:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return lower_bound(nums, target)



nums = [1,3,5,6]
target = 7
print(Solution().searchInsert(nums, target))


# list 是 Python 的内置类型，用于实际创建和操作列表
# List 是类型提示工具，用于代码文档和类型检查
# 在现代 Python 开发中，推荐使用类型提示（List）来提高代码的可读性和可维护性
# 类型提示对 IDE 的代码补全和错误检查也很有帮助
# 这就是为什么在代码中我们需要导入 List 而可以直接使用 list 的原因。


# 是的，你说得对！在 Python 中，类型注解（type hints）是完全可选的，Python 是动态类型语言，不需要显式声明类型
# 但是注明类型会使代码可读性更大