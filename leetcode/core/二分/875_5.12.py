# 爱吃香蕉的珂珂
# 数组 二分
# 输入数组piles 和时间 h 选择一小时吃多少能速度最慢的在 h 的时间内完成所有香蕉。

# 用二分 数组一定是要有序的 所以先排序
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        '''
            待猜测的是吃的速度 对速度用二分查找
            速度最小是0 最大是max(piles)
        '''
        left = 0  # 恒为 False
        right = max(piles)  # 恒为 True

        # 二分查找的模板 反复的从左右缩小范围直到最后 left+1 == right 锁定一个元素是最合适的结果
        while left + 1 < right:  # 开区间不为空的判断 因为区间内要有数 而开区间如果相等或是只用left<right 那么会取不到任何一个数
            mid = (left + right) // 2
            # 计算吃完每堆香蕉需要的时间 然后做累加计算结果和h比较 然后猜出最小的速度
            # 这个计算式的巧妙之处在于：
            # 使用(p-1) // mid来实现向上取整
            # 通过把n个+1移到右边，简化了计算
            # 使用生成器表达式和sum函数，使代码更简洁
            '''
                对于数据分割情况做二分
                这种情况而分里的if是要做sum的 最主要的是列数学式进行判断的设计
            '''
            # 因为整除会向下取整 所以要减1 后面实际还是会加1的然后做了sum会变成整体加n 这里把n移到了等式右边
            if sum((p - 1) // mid for p in piles) <= h - n: # 如果剩余的香蕉在h小时内能吃完 那么就持续向左缩小范围 因为要找最小值
                right = mid  # 循环不变量：恒为 True
            else:
                left = mid  # 循环不变量：恒为 False
        return right  # 最小的 True 这里相当于是bisect_right 返回右侧值向上取整
       
        # 返回right是因为我们要找的是第一个满足条件的值
        # 这相当于bisect_right，返回第一个True的位置
        # 如果返回left，就会得到最后一个False，这不是我们想要的
        # 这种"找第一个满足条件的值"的模式在二分查找中很常见，通常都是返回right。


        # bisect_left：
        # 返回第一个大于等于目标值的位置
        # 如果目标值存在，返回第一个等于目标值的位置
        # 如果目标值不存在，返回第一个大于目标值的位置
        # bisect_right：
        # 返回第一个大于目标值的位置
        # 如果目标值存在，返回最后一个等于目标值的位置的下一个位置
        # 如果目标值不存在，返回第一个大于目标值的位置


# 闭区间写法
class Solution2:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # left的初始化为1 因为速度不可能为0 这样就不会出现除0错误   
        left,right = 1,max(piles)
        
        while left<= right:# 闭区间写法
            mid = (left + right) // 2
            # 剩的时间多 可以减小速度
            '''
                对于数据分割情况做二分
            '''
            if sum((p-1)//mid for p in piles) <= h-len(piles):  
                right = mid - 1
            # 剩余时间不足
            else:
                left = mid+1

        return left

        

piles = [3,6,7,11]
h = 8 # 八小时吃完全部香蕉 选择一堆吃 当堆里的香蕉个数小于速度也不再进食
print(Solution().minEatingSpeed(piles, h))
print(Solution2().minEatingSpeed(piles, h))


# 二分其实就是缩小范围 然后猜测最小值 然后再缩小范围 直到范围内只有一个值 然后返回这个值
# ***整除向下取整 转成先减1再取整是很重要的思想 这样算完再加1就相当于是向上取整也是非常重要的转化思想
# 在代码中，我们使用了一个技巧来计算向上取整：
# (p - 1) // mid + 1 等价于 ⌈p/mid⌉



# 向上取整：(n-1)//k + 1
# 向下取整：n//k
# 四舍五入：(n+k//2)//k



# 开区间：
# 不包含left和right
# 区间内至少有一个数
# 移动时直接赋值mid 因为取不到端点值 mid赋值完实际是略过的

# 闭区间：
# 包含left和right
# 移动时需要+1或-1
# 可以检查到边界值

# 半闭区间：
# 包含left不包含right
# left移动时+1 因为left可以取到
# right移动时直接赋值mid 因为会取左边一个 

# 是循环体内的赋值操作 使得while循环的判断条件不同 二者结合形成了三种写法
