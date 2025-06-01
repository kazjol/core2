# https://wv8qmy18z4.feishu.cn/docx/Vag2deDbNoxpUWxreJGc3Fo2nSe

# 0-1背包 背包容量：汽车容量 物品：代表团个数 填充：各代表团人数
# 返回方案数
from typing import List
from collections import defaultdict
# 一维哈希 关键字是坐车的人 值是方案数
def save_hsh(visit: List[int], car: int)-> int:
    dp = defaultdict(int)
    dp[0] = 1 # 初始状态 ***非常关键 因为没做人的方案数为1 要是不初始化则循环结束后结果为0 ***
    for v in visit: # 先物品
        for pre_c in range(car, -1, -1): # 后背包
            if pre_c+v <= car:
                dp[pre_c+v] += dp[pre_c] # 填充方案数 满足则继承前面的方案数也就是1*dp[pre_c]

    return dp[car]

def save_dp(visit: List[int], car: int)-> int:
    dp = [0]*(car+1)
    dp[0] = 1
    for v in visit:
        # 答案的遍历范围是range(car-v,-1,-1) 因为可能出现越界情况
        # 且对于选不选当前物品v而言如果当前背包容量pre_c+v>car 则必然不可能选v 故可以直接跳过
        for pre_c in range(car, -1, -1):
            if pre_c+v <= car:
                dp[pre_c+v] += dp[pre_c]
    return dp[car]

visit = list(map(int,input().split(',')))
car = int(input())
# print(save_hsh(visit, car))
print(save_dp(visit, car))
