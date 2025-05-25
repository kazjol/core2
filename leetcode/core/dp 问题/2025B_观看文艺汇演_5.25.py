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

lst.sort # 按照开始时间排序  tuple元素排序自动用第一个元素 


# 三种情况 
# 1、第一场结束能看第二场
# 2、第一场结束不能看第二场 但是第一场结束时间更早 选第一场结束为最优
# 3、第一场结束不能看第二场 但是第二场结束时间更早 也就是选择看第二场为最优解


for i,tup in enumerate(lst): # lst已经按照start排序了
    if tup[1] <= lst[i+1][1]: # 如果第一场结束能看第二场
        count += 1
     






