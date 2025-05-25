# 两个数组的交集 要返回交集部分且结果唯一
from typing import List# 要用List需要接入typing模块
# 给数组nums1和nums2，返回两个数组的交集返回元素结果唯一


# 先合并再转set，然后转list
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]: # 双列表参数  返回类型也为列表
        # 先遍历取相同元素放入集合
        set1 = set()
        for i in nums1:
            if i in nums2:
                    set1.add(i)# add函数是没有返回值的set = set.add(i)是错误的
        nums = list(set1)
        return nums
        # nums = list(set(nums1 + nums2))# 列表可以直接合并相加

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print("solve1:",Solution().intersection(nums1, nums2))# [2]


#这个是双层嵌套循环，时间复杂度O(n^2)


# 两个数组的交集 要返回交集部分且结果唯一
from typing import List# 要用List需要接入typing模块
# 给数组nums1和nums2，返回两个数组的交集返回元素结果唯一

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]: # 双列表参数  返回类型也为列表
        # 先遍历取相同元素放入集合
        return list(set(nums1) & set(nums2))# 集合是不能像列表一样直接用+号合并的，只能用&符号 取交集 因为用+会出现重复元素

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print("solve2：",Solution().intersection(nums1, nums2))# [2]


