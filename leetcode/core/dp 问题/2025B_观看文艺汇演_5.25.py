# https://og7kl7g6h8.feishu.cn/docx/WyahdwqCLoz0TNxY0Fmc8PUVnSg
 
# dp 贪心

# 输入：
# 2   两场演出
# 720 120 开始时间 持续时间 （看两场演出要间隔15min）
# 840 120
# 输出：
# 1


n = int(input())
lst = []
for i in range(n):
    start,during = tuple(map(int,input().split())) # 以空格为分割存储
    end = start + during + 15 # 因为开始看下一场要间隔15min 所以可以直接加15作为总时间
    lst.append((start,end))

lst.sort()  # 按照开始时间排序  tuple元素排序自动用第一个元素
ans = 0
pre_end = 0  # 记录上一场演出的结束时间

# 贪心 讨论三种情况
for start, end in lst:
    if start >= pre_end:  # 如果当前演出可以观看(开始时间晚于上一场结束时间)
        ans += 1
        pre_end = end  # 更新结束时间
    elif start < pre_end <= end: # 第二场开始时间在第一场结束时间后 且第一场结束时间更晚 选看第一场为最优
        continue # 看不了第二场
    elif pre_end > end: # 第二场开始时间在第一场结束时间后 且第二场结束时间更早 选看第二场为最优所以把pre_end更新为第二场的end 此时ans已经加过1了只不过现在这个1是第二场
        pre_end = end
print(ans)




# 动态规划
n = int(input())
lst = []
for i in range(n):
    start,during = tuple(map(int,input().split())) # 以空格为分割存储
    end = start + during + 15 # 因为开始看下一场要间隔15min 所以可以直接加15作为总时间
    lst.append((start,end))

lst.sort()  # 按照开始时间排序  tuple元素排序自动用第一个元素
ans = 0
dp = [0] * n # i处的最长无重叠演出场数
dp[0] = 1 # 第一场演出的最优解是1 
# 和马戏团的那道题目一样 遍历之前的所有状态选择最优的更新
for i in range(n):
    temp = 0
    for j in range(i): # 遍历i之前的所有状态
        if lst[j][1] <= lst[i][0]: # 如果j处的演出结束时间小于等于i处的演出开始时间 则可以看j处的演出
            temp = max(temp,dp[j]) # 选择最优的 
    dp[i] = temp + 1 # 更新dp[i]
    ans = max(ans,dp[i]) # 更新ans      也可以最后输出max(dp)输出最大状态
print(ans)