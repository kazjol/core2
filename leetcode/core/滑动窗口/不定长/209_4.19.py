# 长度最小的子数组
# 数组 二分（有序表）用二分能变成O(nlogn)   前缀和 滑动窗口

# 给定一个含有 n 个  正整数 的数组和一个正整数 target 。
# 找出该数组中满足其总和 大于等于 target 的长度最小的
# 大于等于都算 不只是等于 target
# 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0


# 返回的是元素个数 原数组是无序不能排序因为子序列的顺序是不可变的
# 不用二分和贪心就不要排序 二分是在一个（min，max）取值范围内猜值
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        print('mine 超时了主要问题在sum上 滑动窗口固定用right用for遍历数组 left用while判断窗口缩到哪里 for套while ')

        left , right,tip = 0, 0,0
        n = len(nums)
        sum_n = []
        min_len = n
        # for i in range(n):
        #     if nums[i] >= target:
        #         return 1
        # 下面滑动窗口能迭代做出这个结果 这部分多余了



        while right < n and left <= right:

            if sum(sum_n) < target: # 用数组每次都要计算一次sum（）当元素多的时候 太慢了
                sum_n.append(nums[right])

            while sum(sum_n) >= target:
                tip = 1
                min_len = min(min_len,len(sum_n))
                sum_n.pop(0) # 弹出第一个元素 pop()默认弹出栈顶
                left += 1 # 左指针向右移动

            right += 1 # 右指针向右移动

        if tip == 0:
            return 0

        return min_len


class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        print('\n\nod 单while')

        # 滑动窗口的左端
        left = 0

        # 滑动窗口中所有元素的和
        sum = 0

        # 记录滑动窗口的长度，并且不断更新获取最小的那个
        # 一开始，result 可以初始化为一个超过数组长度的值
        # 这样的目的是为了最后返回结果的时候判断 result 有没有被更新
        # 如果没有被更新，并且滑动窗口的长度不可能为 result，因为超过了数组的长度
        # 那就代表不存在符合条件的子数组，需要返回 0
        # 比如 target = 11, nums = [1,1,1,1,1,1,1,1]
        # 先设置 result = 9，执行完后续代码，result 依旧为 9
        # 代表 nums 里面找不到一个子数组和大于等于 11 ，需要返回 0
        result = len(nums) + 1

        # 滑动窗口的右端从 0 开始，这样，当 nums 为空时，可以直接跳出 for 循环
        for right in range(len(nums)):

            # 滑动窗口中加入了 nums[right] 这个元素
            # 滑动窗口元素和需要发生变化
            sum += nums[right]

            # 变化之后需要判断一下，如果滑动窗口的元素和大于等于了 target
            # 那么这个时候就需要不断的向右移动 left，缩小滑动窗口的长度
            while sum >= target:
                # 在获取到一个满足要求的子数组时，更新 result 的值
                result = min(result, right - left + 1)

                # 把 nums[left] 移除滑动窗口
                # 移除不用非要用数组修改结果 减去元素值也是一个效果
                sum -= nums[left]

                # 即 left 向右移动
                left += 1

        # 返回结果
        return 0 if result == len(nums) + 1 else result





nums = [12,28,83,4,25,26,25,2,25,25,25,12]
target = 213

print(Solution().minSubArrayLen(target, nums))
print(nums)
print(Solution2().minSubArrayLen(target, nums))