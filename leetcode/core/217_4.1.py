# 存在重复元素
# 先存在set里再比较


class Solution: # Solution类里面有多变量和函数

    def containsDuplicate(self, nums: list[int]) -> bool : #返回类型bool 参数nums为list[int]
        # 用set来存全部元素

        pre = set()

        # 遍历全部元素是否在set里，如果在，则返回True说明至少有两个
        for num in nums:# 遍历已给的数组
            if num in pre:
                print('存在重复元素')
                return True
            else:
                pre.add(num)
        if len(pre) == len(nums):
            print('不存在重复元素')
            return False








