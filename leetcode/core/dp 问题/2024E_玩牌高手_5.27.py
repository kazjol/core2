# https://og7kl7g6h8.feishu.cn/docx/AqJldxhJ8o4j7Cxk6PUcJLhAnEg

from typing import List
def max_score(core: List[int])->int:
    # 动态规划 dp保存个时间的最大得分 dp[i] = max(dp[i-1]+core[i], dp[i-3] )
    dp = [0 for _ in range(len(core))] # 初始化dp数组 列表推导式保证不是用同一内存地址
    dp[0] = 0 # 题目要求初始分数为0
    for i in range(len(core)):
        if i>=3:# 第1，2，3轮是0，1，2
            dp[i] = max(dp[i-1]+core[i], dp[i-3])
        else:
            dp[i] = max(0,dp[i-1]+core[i])
    return dp[-1]




core = list(map(int,input().split(',')))
print(max_score(core))