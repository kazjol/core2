# 在排序数组中查找元素的第一个和最后一个位置
# 因为数组是有序的所以target一定是连续的，所以可以用二分法查找target的第一个和最后一个位置


from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
            
        left, right = 0, len(nums) - 1  # 使用闭区间
        res = [-1, -1]
        
        # 二分查找找到第一个目标值
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:  # 找到目标值
                # 继续向左查找，确保找到第一个目标值 
                # 直接二分会导致找到的target不一定是第一个匹配值 尤其是当target很多时
                # 而我用的这个思路必须保证先找到第一个target 
                mid -= 1
                res[0] = mid
                # 向右遍历找到最后一个目标值
                while mid < len(nums) and nums[mid] == target:
                    mid += 1
                res[1] = mid - 1
                return res
class Solution2:
    # lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    # 如果数组为空，或者所有数都 < target，则返回 len(nums)
    # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 闭区间 [left, right]
        while left <= right:  # 区间不为空 闭区间的判断方式
            # 循环不变量：
            # nums[left-1] < target
            # nums[right+1] >= target
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1  # 范围缩小到 [left, mid-1]
            else:
                left = mid + 1  # 范围缩小到 [mid+1, right]
        # 循环结束后 left = right+1
        # 此时 nums[left-1] < target 而 nums[left] = nums[right+1] >= target
        # 所以 left 就是第一个 >= target 的元素下标
        return left
        '''
        # lower_bound 是二分的下界写法 返回的是第一个大于等于target的值 会一直缩到最左边且满足条件的位置
        # 当 nums 中存在多个 target 时，lower_bound 会一直向左收缩区间，直到找到第一个等于 target 的位置。
        # 这是因为只要 nums[mid] >= target，就会把 right 往左移，直到不能再移为止。
        # 最终 left 停在第一个 nums[left] >= target 的地方。
        # 如果 nums[left] == target，那么 left 就是第一个等于 target 的下标。
        '''



    def searchRange(nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target: # 没有找到比target大或等于的数 或者找到的是第一个大于target的数
            return [-1, -1]  # nums 中没有 target
            # 如果 start 存在，那么 end 必定存在
        end = lower_bound(nums, target + 1) - 1 # 换成目标值是target的后一个数（因为是整数类型所以比target后比target大的数最少也要大1） 返回其位置-1也就是target的最后一个位置
        return [start, end]

   

nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums, target))


# 问：怎么判断我写的是哪一种二分？

# 答：看 while 循环的条件，如果是 left <= right，就是闭区间；
# 如果是 left < right，就是半闭半开区间；
# 如果是 left + 1 < right，就是开区间
