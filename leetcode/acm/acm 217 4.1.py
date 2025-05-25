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

nums = list(int(i) for i in input().split()) #可以通过遍历输入然后组成列表这里把迭代的i强制转换成int了 也可以用map
nums2 = list[2]# 列表对象要可迭代 ()是set  []是list  {}是dict
print(nums2)
print(type(nums)) # 输出结果nums为type.GenericAlias 用map转input为list时
Solution().containsDuplicate(nums) # 调用Solution().containsDuplicate(nums)时参数需要一个int列表但是nums不是
