# https://yxvp0lnjvna.feishu.cn/docx/SsPpdlxghoBBCexjZjUc44Ounjc
# 输入
# 3 11 6 7 8
# 1
# 每小时只能吃一课树


# 二段性二分数据为数组 猜speed
'''
    对于这种对比数据是数组的情况 要先简化数据为单个数据再做二分 这里就是数学思维了
'''


# 导入向上取整函数ceil，用于后续的计算 用于数学表达式 

from math import ceil


nums = list(map(int, input().split()))
h = int(input())


# 计算在速度k的条件下，吃一堆要花多久，计算每一堆基于k要花费的时间 然后设计二分里的判断式子
# 这里导入了ceil所以就不用转向上取整为向下取整了 因为除法是自动向下取整如果直接除的话还要转换式子
def cal_hour_used(nums, k):
    return sum(ceil(p / k) for p in nums) # 满足的最小情况一定是向上取整的不能少
    # return n+sum(p//k for p in nums )  //是向下取整


# 二分查找求解问题的函数
def minEatingSpeed(nums, h):
    # 左闭右开 因为速度不能为0 所以0不在猜测范围内
    left, right = 1, max(nums) + 1
    while left < right:
        mid = (left + right) // 2
        # 花费时间太少，速度偏大，速度还可以减小，
        # 搜索区间向左折半，right可以向左移动
        if cal_hour_used(nums, mid) <= h:
            right = mid
        else:# 因为左闭右开 左边能取到 所以对于不符合条件的mid值 直接跳过
            left = mid + 1 # left返回第一个符合目标的值
    return left 


# 如果nums的长度已经大于h，一定无法在h小时内吃完所有蟠桃
# 直接输出0
if len(nums) > h:
    print(0)
# 否则进行二分，输出答案
else:
    print(minEatingSpeed(nums, h))