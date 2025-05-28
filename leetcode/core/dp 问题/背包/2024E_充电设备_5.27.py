# https://wv8qmy18z4.feishu.cn/docx/PzqhdpH2joUo6dxpVU3cJg6GnEe

# 0-1背包问题 路径无关
'''
    容量（限制）：p_max
    物品：n个设备
    重量：设备功率
'''
from typing import List
def max_num(n:int,devices:List[int],p_max:int)->int:
    # 构建二维dp数组，长度为(n+1)*(p_max+1)，为布尔类型的二维数组
    # dp[i][j]的含义为
    # 在考虑第i个设备时，功率j是否能够取到 行是设备数列是是否能取到某功率
    dp = [[False] * (p_max + 1) for _ in range(n + 1)] # 一列p_max+1个元素，表示是当前功率能否取到 n+1行（项）表示n个设备
    # 初始化dp[0][0]为True，表示可以取到，第一个设备一定能取到0
    dp[0][0] = True

    # 遍历每一种设备的功率p
    # 注意为了和二维dp数组的索引一一对应，故i从1开始，取到n结束，二维dp数组会多一行一列，所以最后返回dp[m][n]
    for i in range(1, n + 1):
        # i是从1开始计数的，故p应为devices[i-1]
        p = devices[i - 1]
        # 遍历dp[i-1]数组，所有可以取到的功率总和，用pre_p表示
        for pre_p in range(0, p_max + 1): # 对当前设备是否能取到pre_p功率的初始化
            # 假如某个功率总和pre_p可以取到，则更新到dp[i][pre_p]
            if dp[i - 1][pre_p] == True: # 前一个设备能取到pre_p，则当前设备也能取到pre_p，继承
                dp[i][pre_p] = True
                # 因为是在if dp[i-1][pre_p] == True的情况下，所以表示该设备i之前的设备i-1能取到pre_p，所以可以继承到i再加上p的功率进行更新
                # 假如从某个功率总和pre_p出发，加上当前的设备功率p，更新

                cur_p = p + pre_p
                # 如果cur_0没有超出最大功率限制
                if cur_p <= p_max:
                    # 则cur_p功率也是一个可以取得的方案，将dp[i][cur_p]修改为True
                    dp[i][cur_p] = True

    return max((i for i in range(p_max+1) if dp[-1][i])) # 对最后一个设备的横向遍历 判断其能达到的全部功率里的最大值



def max_sum_1dp(n:int,devices:List[int],p_max:int)->int:
        # 构建一维dp数组，长度为(p_max+1)，为布尔类型的数组
        # dp[i]功率i是否能够取到
        dp = [False] * (p_max+1)
        # 初始化dp[0]为True，表示可以取到，0功率一定能取得
        dp[0] = True

        # 遍历每一种设备的功率p，继承并更新每个设备能取到的最大功率dp数组
        '''
           for 循环遍历每个设备 代替 二维dp数组的行遍历（设备遍历并保存状态）
        '''
        for p in devices:
            # 遍历当前dp数组，所有可以取到的功率总和，用pre_p表示
            # 这里必须使用拷贝，因为在本次遍历中，dp数组会发生改变
            # dp数组正在发生的改变，不能在遍历中被考虑
            #
            # 另一种可行的方法是，逆序遍历dp数组
            # 这样可以保证大功率的修改总是发生在遇到小功率之前
            temp = dp[:] # 这里必须使用拷贝初始化，否则会修改到原数组，用上一个设备的状态来更新当前设备的状态

            # 遍历全部的功率
            for pre_p in range(0, p_max+1):# range取不到末尾元素，所以要加1
                if temp[pre_p] == True: # 这里的temp保存的dp还是上个设备的dp，上个设备能取到这个功率pre_p，则当前设备也能取到这个功率然后继承并更新
                    # 更新
                    cur_p = p + pre_p
                    # 如果cur_0没有超出最大功率限制
                    if cur_p <= p_max:
                        # 则cur_p是一个可以取得的方案，将dp[cur_p]修改为True
                        dp[cur_p] = True

        # 输出dp数组中为True的最大值，即为小于等于p_max的最大功率
        return max((i for i in range(p_max + 1) if dp[i] == True))

# 哈希表直接继承
def max_sum_hash(n:int,devices:List[int],p_max:int)->int:
    dp = set() # 集合是哈希类型 可以用匹配制
    dp.add(0) # 初始化，0功率一定能取得
    for device in devices: # 遍历每个设备 对每个功率能否取到判断 所以还是要嵌套遍历全部功率
        # for i in range(1, p_max + 1):
        for p in list(dp): # 遍历继承来的dp集合 并更新 ***因为for是要用迭代器自动以步长1遍历的 set是哈希集合只满足匹配制不可索引***
            if p + device <= p_max: # 继承并更新每个设备能取到的最大功率dp集合
                dp.add(p + device) # 继承并更新每个设备能取到的最大功率dp集合 下一个设备自动继承dp的功率更新（上一个设备的更新）
    return max(dp)




# 求<=p_max 满足目标值的最大子序列和
# n = int(input()) # 待设备个数
# devices = list(map(int, input().split())) # 每个充电设备的输出功率
# p_max = int(input()) # 充电站最大输出功率
# print(max_num(n,devices,p_max))
# print(max_sum_1dp(n,devices,p_max))
# print(max_sum_hash(n,devices,p_max))



'''
    背包：限制条件
    物品：在限制条件下选择 填满背包容量
    方法：选择方法 
    目的：得到最优解

    遍历方法
    先物品 后背包 

    考虑当前物品是否被选择到 0~背包容量 的每个方法里 
    0-1背包 正序遍历容量 保证当前物品只被选择一次
    完全背包 逆序遍历容量 保证当前物品可以被选择多次

    逆序更新 例：当更新更新完dp[4]选择了当前物品且用dp[2]更新，因为是逆序所以dp[2]还是上一个物品的dp，
    所以该方法里当前物品只被选择一次，接下来更新dp[3]选择当前物品且用dp[1]更新,dp[1]还是上一个物品的dp同理 所以可以保证在每个方法里当前物品只被选择一次
    
    正序更新 例：先更新dp[2]，此时dp[2]已经包含了“本轮新加的方案数”。这里已经选了当前物品 增加了重量p
            接着更新dp[3]，它会用到刚刚更新过的dp[2]，且同样可以选择当前物品 增加重量p，这里对于当前物品就产生了两次（多次）选择这个方法里就选择了两次当前物品

                
                
'''

'''
    变式：求方法数 0-1背包

'''

# 题目：选择元素使得最符合p_max的方法数
from collections import defaultdict

devices = [1, 2, 2, 3, 5]
p_max = 6
n = len(devices)




# key = 能到到的功率，value = 方法数 
dp = defaultdict(int) 
dp[0] = 1 # 初始化到达功率为0的方法数为1 也就是不选设备

for p in devices:  # 遍历每个设备 先物品 
    for pre_p in range(p_max, -1, -1):  # 逆序遍历容量保证一个物品只选一次 关键字 后背包
        cur_p = p + pre_p
        if cur_p <= p_max:
            dp[cur_p] += dp[pre_p]

print(dp[max(i for i in dp if dp[i] != 0)]) # 输出最大功率的方法数


'''
    变式：求方法数 完全背包
'''

for p in devices:  # 遍历每个设备 先物品 


    for pre_p in range(0, p_max+1):  # 正序遍历容量能够多次选择 
        cur_p = p + pre_p
        if cur_p <= p_max:
            dp[cur_p] += dp[pre_p]

print(dp[max(i for i in dp if dp[i] != 0)])



