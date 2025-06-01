# https://og7kl7g6h8.feishu.cn/docx/HrFRdlddJoZ3z5xGct4c5vmdnjg
# 二段性二分



'''
    这种题要求一个值但是几乎没有任何的可推导思路 
    所以就是猜值 而且是猜满足条件的最大/最小->二分
'''

#
# 考虑出餐速度speed与能否完成供餐之间的关系
# - 出餐速度speed越大的时候，越可能完成供餐。当取到最值speed = max(nums)时，一定能完成供餐。
# - 对于在区间[1, min(nums)]之间取值的出餐速度speed而言，一定存在一个值ans，使得
#   - 当speed ∈ [0, ans)时，无法完成供餐。
#   - 当speed ∈ [ans, max(nums)]时，可以完成供餐。
#   - 这体现了这个问题的二段性，ans是我们需要的答案，而ans的寻找就可以用二分查找来完成


# 子问题分析
# 对于二分查找过程中得到的每一个出餐速度speed = mid，我们都要去判断在出餐速度的条件下能否完成供餐。
# 初始化剩余餐数 rest = M，遍历nums数组中每一分钟前来就餐的人数num。若
# - rest < num，则无法完成供餐，直接返回False。
# - rest ≥ num，该分钟可以完成供餐，rest要减去当前分钟就餐人数num，同时加上本分钟多提供的餐数speed，用于后续人员的就餐。

'''
    二分法就是把待取值框在一个范围里 (0,max) 然后在范围里用二分高效猜出最匹配的值
    
'''

'''
    用二分法猜ans 怎么用二分法更新ans
    每次取mid如果mid满足条件则 继续用二分缩小ans直到找到下一个不满足条件的ans   
'''

   

# 判断当前的ans是否满足条件
from typing import List


def check(ans:int,food:int):
    rest = food
    for p in people:
        if rest < p:
            return False
        rest -= p # 当前时间被吃掉的餐
        rest += ans # 当前时间生产的餐
    return True  
def lowb(people:List[int],food:int)->int:
    left ,right = 0,max(people)+1 # 左闭右开
    while left < right:
        mid = (left + right) // 2
        if check(mid,food): # 当前满足条件 要找更小的所以缩到右半表 
            right = mid
        else: # 当前不满足条件 要找更大的所以缩到左半表
            left = mid + 1 # 左边界能取到且当前mid不满足 所以跳过 left返回的是第一个满足条件的值

    return left # 左边指向的是第一个满足条件的值



time = int(input())
food = int(input()) # 已有餐食
people = list(map(int,input().split())) # 每个时间来的人数
print(lowb(people,food))

