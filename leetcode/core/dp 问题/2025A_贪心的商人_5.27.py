# https://og7kl7g6h8.feishu.cn/docx/LHD9d8pkrouZBCx5SOEcLTpinLf



'''
    买卖股票的贪心算法 赚到每一种利润 只考虑有没有利润 不考虑买卖

'''
# 同LC122. 买卖股票的最佳时机II 0-1背包问题
# 读取商品数量和天数
goods = int(input())
days = int(input())

maxnum = list(map(int,input().split())) # 每件商品的持有数量 不能用[]直接转为列表

# map(int, input().split()) 返回的是一个 map 对象，这是一个迭代器
# 当我们使用 [map(int, input().split())] 时，我们实际上创建了一个只包含一个 map 对象的列表
# 这样 max[0] 会是一个 map 对象，而不是我们想要的整数列表

# # 错误的方式
# max = [map(int, input().split())]  # 假设输入是 "1 2 3"
# # max 现在是 [<map object at 0x...>] 这是一个迭代器 表示这个 map 对象在内存中的地址。
# # max[0] 是一个 map 对象，不能直接用于计算

#    # 错误的方式：直接使用map对象
#    numbers = map(int, "1 2 3".split())
#    print(numbers[0])  # 错误！map对象不支持索引访问
   
#    # 正确的方式：转换为列表
#    numbers = list(map(int, "1 2 3".split()))
#    print(numbers[0])  # 正确！输出: 1


# 存储每个商品每天的价格
price = []
# 读取每个商品的价格数据
for i in range(goods):
    # 将输入的价格数据转换为元组并添加到price列表中
    price.append(tuple(map(int, input().split())))
print(price)
# 计算最大利润
profit = 0
for i in range(goods):  # 遍历每个商品
    for j in range(1, days):  # 遍历每天
        # 如果今天的价格比昨天高,就卖出获得利润
        
        if price[i][j] > price[i][j-1]:
            profit += (price[i][j] - price[i][j-1])*maxnum[i] # 这里是一件商品的持有数
        # 否则不做操作
print(profit)  # 输出最大利润



'''
    动态规划
'''

goods = int(input())
days = int(input())
maxnum = list(map(int,input().split())) # 每件商品的持有数量 不能用[]直接转为列表
price = []
for i in range(goods):
    price.append(tuple(map(int,input().split())))

# 构建长度为n*2的dp数组
# dp[i]表示第i天的情况
# dp[i][0]表示在第i天如果持有0份股票的最大利润
# dp[i][1]表示在第i天如果持有1份股票的最大利润
profit = 0
for i in range(goods):
    # 初始化dp数组 股票的默认条件
    # 第一层for是对不同的商品 所以每次循环开始都要初始化price
    
    dp = [[0] * 2 for _ in range(days)] # days项(行) 每项保存持有状态和最大利润 这里可以优化空间 只保存利润即可
    '''
        经常出错的问题 持有和不持有的最大利润 要单独维护不能合并
    '''
    dp[0][0] = 0 # 第一天不持有股票 利润为0
    dp[0][1] = -price[i][0]*maxnum[i] # 第一天持有股票 利润为-price[0][0] 第一天买了股票

    for j in range(1,days): # 第一天的初始化已经完成了 ***而且对于状态数组一定要初始化才能往后迭代***
        dp[j][0] = max(dp[j-1][0],dp[j-1][1]+price[i][j]*maxnum[i]) # 第j天不持有股票 利润为前一天不持有股票的利润和前一天持有股票的利润+今天的价格
        dp[j][1] = max(dp[j-1][1],dp[j-1][0]-price[i][j]*maxnum[i]) # 第j天持有股票 利润为前一天持有股票的利润和前一天不持有股票的利润-今天的价格
    profit += dp[days-1][0] # 最后一天不持有股票的最大利润 因为要卖多种物品
    
print(profit) # 输出最后一天不持有股票的最大利润



'''
    函数调用更方便
'''
# 计算某个特定商品能取得的最大利润的函数
# 和LeetCode122. 买卖股票的最佳时机II完全一致

# 因为有多个商品 所以可以对多个商品调用最大利润函数
def maxProfit(prices, days):
    # 设置一个三维数组 dp
    # dp[i][k][b]
    # i 表示天数，dp[i] 表示第 i 天的最大利润
    # k 表示最多交易次数，每次交易包含买入和卖出，这里只在买入的时候将 k - 1
    # 注意：【 k 表示最多交易次数，而不是实际交易次数，比如最多交易两次可能实际只交易一次】
    # b 表示当前是否持有股票，取值为 0 和 1
    # 其中 0 表示当前持有 0 份股票，即【不持有】股票
    # 而 1 表示当前持有 1 份股票，即【持有】股票

    # 在本题中，k 的值为正无穷，因此可以不设置这个维度
    # i 的取值范围为数组 prices 的长度，从 0 开始

    # 构建长度为n*2的dp数组
    # dp[i]表示第i天的情况
    # dp[i][0]表示在第i天如果持有0份股票的最大利润
    # dp[i][1]表示在第i天如果持有1份股票的最大利润
    dp = [[0] * 2 for _ in range(days)]

    # dp[0][0][0] 表示在第 0 天结束时，即收盘后，手上持有 0 份股票，且此时最多进行了 0 次交易的情况下可以获得的最大收益
    # 此时，就是什么都没做，利润为 0

    # dp[0][k][0] 表示在第 0 天结束时，即收盘后，手上持有 0 份股票，且此时最多进行了 k 次交易的情况下可以获得的最大收益
    # 此时，就是什么都没做，利润为 0
    dp[0][0] = 0

    # dp[0][k][1] 表示在第 0 天结束时，即收盘后，手上持有 1 份股票，且此时最多进行了 k 次交易的情况下可以获得的最大收益
    # 手上持有了 1 份股票，那肯定是执行了买入操作，然后又还没有卖出，那么钱都投入了股票中，利润就是负的，即为 -prices[0]
    dp[0][1] = -prices[0]

    # 动态规划：自底向上，即从前向后遍历，实现一个萝卜一个坑
    for i in range(1, days):
        # 对于每个坑来说，都有两种状态
        # 今天也就是第 i 天

        # 1、今天【不持有】股票
        # 第 i - 1 天【持有】股票，第 i 天卖出
        # 昨天【持有】股票，今天卖出
        # vs
        # 第 i - 1 天【不持有】股票，第 i 天不操作
        # 昨天【不持有】股票，今天不操作
        dp[i][0] = max(dp[i-1][0], dp[i - 1][1] + prices[i])

        # 2、今天【持有】股票
        # 第 i - 1 天【持有】股票，第 i 天不操作
        # 昨天【持有】股票，今天不操作
        # vs
        # 第 i - 1 天【不持有】股票，第 i 天买入
        # 昨天【不持有】股票，今天买入
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

    # for 循环结束后，dp 数组填充完毕
    # dp[days-1][k][0]
    # 表示第 days - 1 天结束时，即最后一天收盘后，
    # 手上持有 0 份股票，可以获得的最大收益
    return dp[days-1][0]

# 输入商品数量
n = int(input())
# 输入天数
days = int(input())
# 输入每种商品的最大数目
numbers = list(map(int, input().split()))

# 初始化答案变量
ans = 0
# 循环n次，输入每种商品在days天中的价格变化
for i in range(n):
    prices = list(map(int, input().split()))
    # maxProfit(prices, days)返回单件第i种商品能够取得的最大利润
    # 再乘上numbers[i]即为能够获得第i种商品能够获得的总利润
    ans += maxProfit(prices, days) * numbers[i]

print(ans)



# 用核心代码方式检测函数编写问题
from typing import List, Tuple # 接收参数为tuple的声明
class Solution:
    def maxProfit(self, goods: int, days: int, maxnum: List[int], prices: List[Tuple[int, ...]]) -> int:
        # 计算最大利润
        profit = 0
        for i in range(goods):
            # 初始化dp数组
            dp = [[0] * 2 for _ in range(days)]
            
            # 初始化第一天
            dp[0][0] = 0  # 第一天不持有
            dp[0][1] = -prices[i][0] * maxnum[i]  # 第一天持有，需要买入maxnum[i]个商品
            
            # 状态转移
            for j in range(1, days):
                # 今天不持有 = max(昨天不持有, 昨天持有+今天卖出)
                dp[j][0] = max(dp[j-1][0], dp[j-1][1] + prices[i][j] * maxnum[i])
                # 今天持有 = max(昨天持有, 昨天不持有-今天买入)
                dp[j][1] = max(dp[j-1][1], dp[j-1][0] - prices[i][j] * maxnum[i])
            
            # 最后一天必须不持有
            profit += dp[days-1][0]
        
        return profit
   
goods = int(input())
days = int(input())
maxnum = list(map(int,input().split()))
prices = []
for i in range(goods):
    prices.append(tuple(map(int,input().split())))
print(Solution().maxProfit(goods,days,maxnum,prices))

