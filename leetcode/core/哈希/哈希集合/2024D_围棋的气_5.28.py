# https://og7kl7g6h8.feishu.cn/docx/YRlBdstoFoxaQCxxfRUcz5ymnab
from typing import Tuple, List

# 把遍历过的位置加入集合，遍历全部的棋子当出现重复位置则跳过

# 这个和图那里有点类似 遍历上下左右四个位置
def air_num(blackt:List[Tuple[int,int]], whitet:List[Tuple[int,int]])->str:
    '''
       偏移数组的设置 非常重要
    '''
    D = [(0,1),(0,-1),(1,0),(-1,0)] # 偏移数组 元素是元组类型 分别为上下左右
    black_set = set() # 黑棋的气
    white_set = set() # 白棋的气

    # 计算黑棋的气
    for b in blackt:
        for d in D: # 遍历四个方向
            nb = (b[0]+d[0],b[1]+d[1]) # 元组类型
            # 位置在棋盘范围内，且不是任何棋子的位置
            if (0 <= nb[0] <= 18 and 0 <= nb[1] <= 18 and 
                nb not in blackt and nb not in whitet):
                black_set.add(nb)
    
    # 计算白棋的气
    for w in whitet:
        for d in D:
            nw = (w[0]+d[0],w[1]+d[1])
            # 位置在棋盘范围内，且不是任何棋子的位置
            if (0 <= nw[0] <= 18 and 0 <= nw[1] <= 18 and 
                nw not in blackt and nw not in whitet):
                white_set.add(nw)

    return f'{len(black_set)} {len(white_set)}'


# 输入数据
black = list(map(int,input().split())) # 前是横坐标 后是纵坐标
blackt = list((black[i],black[i+1]) for i in range(0,len(black),2)) # (a,b)就说明这是元组类型了 不用写tuple(a,b)
white = list(map(int,input().split()))
whitet = list((white[i],white[i+1]) for i in range(0,len(white),2)) # 步长为2间隔取
print(air_num(blackt,whitet))



# 简单解法


# 上下左右四个方向的偏移量数组
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# set_color为某种颜色（黑或白）对应的棋子位置构成的哈希集合
# set_other_color对应另一种颜色的棋子位置构成的哈希集合
# 本函数用于计算该种颜色的气的个数
def cal_qi_num(set_color, set_other_color):
    # 构建气的哈希集合，之所以用哈希集合是为了共有气的去重
    set_qi = set()
    # 考虑所有同色棋子
    for i, j in set_color:
        # 遍历上下左右四个方位
        for di, dj in D:
            # 考虑近邻点(i, j)
            ni, nj = i+di, j+dj
            # 近邻点不越界，且为空位（既不是黑棋，也不是白棋）
            if (0 <= ni <= 18 and 0 <= nj <= 18 and
                (ni, nj) not in set_color and (ni, nj) not in set_other_color):
                # 此时近邻点为一个气，加入哈希集合set_qi中
                set_qi.add((ni, nj))
    # 返回哈希集合的长度，即为该种颜色的气的个数
    return len(set_qi)


# 输入数据
lst_black = list(map(int, input().split()))
lst_white = list(map(int, input().split()))

# 每两个数字为一组坐标，构建所有黑棋/白棋对应的哈希集合
set_black = set((lst_black[i], lst_black[i+1]) for i in range(0, len(lst_black), 2)) # 用的set存元组 防止重复？但是也不可能出现重复位置的棋子（出现提子？）好像set比list合适
set_white = set((lst_white[i], lst_white[i+1]) for i in range(0, len(lst_white), 2))
# 分别调用cal_qi_num，计算黑棋和白棋的气的个数
ans_black = cal_qi_num(set_black, set_white)
ans_white = cal_qi_num(set_white, set_black)
# 输出答案
print(ans_black,ans_white) # 输出的时候 两个输出元素自动用空格分隔