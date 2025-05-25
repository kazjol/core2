# 山洞里有 M 株不同的草药，采每一株都需要一些时间 t_i，每一株也有它自身的价值 v_i。给你一段时间 T，在这段时间里，你可以采到一些草药。让采到的草药的总价值最大。
'''
    经典0-1背包问题
'''
from math import inf as INF
tcost = [0] * 103
moneyget = [0] * 103
# 增加一个数组 mem 来记录每个 dfs(pos,tleft) 的返回值。刚开始把 mem 中每个值都设成 -1（代表没求解过）。每次需要访问一个状态时
# 如果相应状态的值在 mem 中为 -1，则递归访问该状态。否则我们直接使用 mem 中已经存储过的值即可。
# 对于python来说直接加装饰器cache就行
mem = [[-1 for i in range(1003)] for j in range(103)] # 记忆化搜索的暂存结果的数组


def dfs(pos, tleft):
    if mem[pos][tleft] != -1: # 已经求解过 直接退栈返回保存的结果
        return mem[pos][tleft] # tleft 剩余时间 pos 当前草药编号
    if pos == n + 1: # 没有草药可采
        mem[pos][tleft] = 0
        return mem[pos][tleft]
    '''
        对于每种草药，有两种选择：采或不采
        不采：直接考虑下一种草药 dfs1 = dfs(pos + 1, tleft)
        采：时间减少，价值增加 dfs2 = dfs(pos + 1, tleft - tcost[pos]) + moneyget[pos]
        取两种选择的最大值 max(dfs1, dfs2)
    '''
    dfs1 = dfs2 = -INF # 每次dfs都要初始化 清除原有数据
    dfs1 = dfs(pos + 1, tleft) # 不采
    if tleft >= tcost[pos]: # 采  如果选择采则要有条件判断 不采的话不用考虑
        dfs2 = dfs(pos + 1, tleft - tcost[pos]) + moneyget[pos]
    '''
      和买彩票一样 都是操作二元化 两种操作分别做递归 最后选最值这个时候就是最优解 
      因为每次决定的操作只有两次
    '''
    mem[pos][tleft] = max(dfs1, dfs2) 
    return mem[pos][tleft]

print('输入总时间t和草药数量n')
t, n = map(lambda x: int(x), input().split()) # 输入时间t和草药数量n 依次赋给t，n
print('每行输入草药的时间和价值')
for i in range(1, n + 1): # for循环会每次读取 输入每株草药的时间和价值 依次赋给tcost[i], moneyget[i]
    tcost[i], moneyget[i] = map(lambda x: int(x), input().split())
print('最大价值为:',dfs(1, t))

# 输入
# 输入总时间t和草药数量n
# 10 3
# 每行输入草药的时间和价值
# 3 7
# 8 12
# 2 3

# 输出
# 最大价值为: 15 
'''

Lambda函数是Python中的一种匿名函数，它允许你快速定义小型的一次性函数，而不需要使用def语句创建完整的函数定义。
主要特点：
语法简洁：使用lambda 参数: 表达式的形式
匿名：不需要函数名
单行表达式：只能包含一个表达式，不支持多条语句
自动返回：表达式的值自动作为返回值

这里的lambda x: int(x)定义了一个接收参数x并返回int(x)的匿名函数。它等价于：

但由于int函数本身就接受一个参数并返回转换后的整数，所以可以直接使用：

Lambda函数在需要简单函数作为参数时特别有用，比如在排序、过滤或映射操作中。但当只是简单调用一个已有函数时（如int），直接传递函数名更为简洁。
'''