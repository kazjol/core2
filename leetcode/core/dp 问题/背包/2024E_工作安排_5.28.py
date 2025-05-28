# https://wv8qmy18z4.feishu.cn/docx/CoymdHJTAop3ehxez1wcHj9Anmb
# 0-1背包 容量：总工作时间 价值：报酬  物品：任务
from collections import defaultdict
from typing import List

def bestreword(T:int,n:int,times:List[int],rewards:List[int])->int:
    dp = [0] * (T+1) # 对于背包 dp大小是背包容量 保存当前的最大收入
    dp[0] = 0
    data = list(zip(times,rewards)) # 元素为元组的列表
    print(data)
    
    # 二维数组是有物品数行和时间数列 dp = [[0]*(T+1) for _ in range(n+1)] 二维数组会多一行一列0 [[]*n]才是二维数组 [0*n]是一维 
    for t,r in data: # 遍历物品 先物品
        # 0-1背包逆序遍历背包 后背包
        for cur_t in range(T,-1,-1):
            pre_r = dp[cur_t] # 保存当前时间量的最大收入（上一轮数值） 用作更新
            if t+cur_t<=T: # 更新
                dp[t+cur_t] = max(dp[t+cur_t],pre_r+r) # 继承原来当前时间的dp 或选当前工作作为新dp更新
    return max(dp)


# 一维哈希这个对比二维数组好理解 关键字是当前时间：值是当前时间对应的最大收入
def bestreward_hash(T:int,n:int,times:List[int],rewards:List[int])->int:
    data = list(zip(times,rewards))
    dp = defaultdict(int)
    for t,r in data:
        for pre_t in range(T,-1,-1):
            if pre_t+t<=T: # 选择当前工作可以更新 满足容量
                dp[pre_t+t] = max(dp[pre_t+t],dp[pre_t]+r)
    return max(dp.values()) # 返回字典值的最大值



# 二维数组 dp[i][j] 表示前i个任务在j时间内可以获得的最大报酬 每个工作一行 每个时间一列
def bestreward_2dp(T:int,n:int,times:List[int],rewards:List[int])->int:
    data = list(zip(times,rewards))
    dp = [[0]*(T+1) for _ in range(n+1)] # 多一行一列0 T+1 n+1
    for i in range(1,len(data)+1):
        t,r = data[i-1]
        for pre_t in range(T,-1,-1): # 给每个工作创造空间保存了就不用遍历物品了
            if t+pre_t<=T: # 选择当前工作可以更新 满足容量
                dp[i][t+pre_t] = max(dp[i][t+pre_t],dp[i-1][pre_t]+r)
            else:# 时间容量不足继承之前的
                dp[i][pre_t] = dp[i-1][pre_t]
    # 输出dp数组最后一行中的最大值，即考虑所有工作后在时间范围内可获得的最大报酬
    return max(dp[n])






T,n=map(int,input().split())
times = []
reward = []
for i in range(n):
    t,r=input().split()
    times.append(int(t))
    reward.append(int(r))
# print(bestreword(T,n,times,reward))
# print(bestreward_hash(T,n,times,reward))
print(bestreward_2dp(T,n,times,reward))
