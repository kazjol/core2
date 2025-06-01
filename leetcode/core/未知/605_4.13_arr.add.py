# 种花问题
# 贪心 数组

# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
# 给你一个整数数组 flowerbed 表示花坛，
# 由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。
# 另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false 。

# 插空问题
# 保证数组是10101
# 遍历花坛插入花 如果可插入的数大于等于待插入的则true 否则false
# 1 0 1 0 0 1 0 0 0 0 0 0 1 1
# 0 1 0 0 0
# 0 0 1 0 0

# 默认增加边界两个值为0 flowerbed[-1] = 0  flowerbed(len) = 0

print('mine')
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zero = 0

        # 特殊情况 只有一个坑
        if flowerbed[0] == 0 and len(flowerbed) == 1:
            if n <= 1:
                return True
            return False
        elif flowerbed[0] == 1 and len(flowerbed) == 1:
            if n == 0:
                return True
            return False

        # 第一个元素一定不能为0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1



        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:
                    zero += 1
            elif flowerbed[i] == 1:
                    zero = 0
            if zero == 3:
                    n -= 1
                    flowerbed[i-1] = 1
                    zero = 1
        if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2] == 0:
            n -= 1

        if n <= 0:
            return True
        return False
flowerbed = [0,0,0,0]
n = 3
print(Solution().canPlaceFlowers(flowerbed,n))


print('\n\n边界设为0')
class  Solution2():
    def canPlaceFlowers(self,flowerbed:List[int],n:int) -> bool:
        lenth = len(flowerbed)
        zero = 0
        if lenth == 1:
            if flowerbed[0] == 0 and n <= 1:
                return True
            elif flowerbed[0] == 1 and n == 0:
                return True
            else:
                return False

        flower = (lenth+1)*[0]

        flower[1:lenth] = flowerbed

        for i in range(len(flower)):

            if flower[i] == 0:
                    zero += 1
            elif flower[i] == 1:
                    zero = 0
            if zero == 3:
                    n -= 1
                    flower[i-1] = 1
                    zero = 1
        if n <= 0:
            return True
        return False
flowerbed = [1,0,0,0,1,0,0]
n = 2
print(Solution2().canPlaceFlowers(flowerbed,n))

print('\n\n灵神')
class Solution3:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 同样是设置边界为0
        # 这里提供了数组添加元素的方法，可以直接在数组中添加元素，而不用重新定义数组
        flowerbed = [0] + flowerbed + [0]
        # 非常巧妙的包括了边界的0
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1  # 种花！
                n -= 1
        return n <= 0
    # 思路完全一样但是是我的代码的优化

flowerbed = [0,0,0,0]
n = 3
print(Solution3().canPlaceFlowers(flowerbed,n))

