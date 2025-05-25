# 给定nums和k，判断nums中是否存在两个不同索引 满足 abs（i-j）<=k，且nums[i] == nums[j] 存在返回True，否则返回False。
# 遍历nums存入map包括关键字和下标然后继续往后比较是否和map中元素相同
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map1 = dict() # map = {}也可以初始化
        # i是元素值num是下标
        for idx,num in enumerate(nums):
            # print(num,idx)
            if num not in map1:
                map1[num] = idx # 字典是关键字对组成的不是索引和数值 改变字典的键值对 map[关键字] = 值
                # print(map1)
            else:
                # print(idx,num,map1.get(num),map1)
                if abs(idx - map1.get(num))<=k: # 可以用map[num]取字典中目标关键字的下标 也可以用字典自带的get函数取 idx是当前num在nums里的下标用enumerate返回的
                     # print(map1[num],idx)
                    return True

                    #更新下标
                map1[num] = idx

        return False
# map2 = {'a':1,'b':2}
# map2['b'] = 3
# print(map2)
nums = [1,0,1,1]
k = 1
print(Solution().containsNearbyDuplicate(nums,k)) # False
