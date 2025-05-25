# 给定整数数组nums 和目标数target  找nums里的两个整数，使得它们的和等于target返回数组下标 只返回数组下标
# 一个数组里只有一个答案
from typing import List


# 访问一个元素做一次减法并查找map 判断map里是否有该配对元素 如果没有就在map里存入当前元素和下标 然后继续访问下一个元素

class Solution:
    def twoSum(self,nums: List[int],target: int) ->  List[int]:
       # key为元素组值，value为元素下标

       map1 = dict()# 定义一个字典 直接用map命名会和内置函数map冲突

       # 遍历整个字典并得到元素和下标
       for i,num in enumerate(nums):

        # 把遍历的结果和target做差值后在map1里找

        if target - num not in map1:
            map1[num] = i

        else:
            return [map1.get(target - num),i]

'''
map2 = {'1':2,'2':3}
print(map2.get('1'))
获取字典关键字的下标
'''
nums = list(map(int,input().split(',')))
target = int(input())
print(Solution().twoSum(nums,target))
