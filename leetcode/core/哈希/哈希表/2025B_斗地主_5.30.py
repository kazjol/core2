# https://og7kl7g6h8.feishu.cn/docx/Vmu8dqCQYoOzmExswVpc97gknRh
from cmath import inf
from collections import defaultdict, Counter

# 输入处理
# inhand = list(input().split('-'))  # 我手上的牌
# out = list(input().split('-'))     # 已经出的牌

# 将特殊牌转换为数字 直接遍历然后调用函数就好了
def convert_card(card):
    if card == 'J': return '11'
    if card == 'Q': return '12'
    if card == 'K': return '13'
    if card == 'A': return '14'
    return card

# 转换所有牌为数字
inhand = [convert_card(card) for card in inhand]
out = [convert_card(card) for card in out]

# 统计已经出现的牌
used_cards = Counter(inhand + out)

# 初始化所有牌的数量（3-14，不包括2和大小王） 推导式初始化字典
total_cards = {str(i): 4 for i in range(3, 15)}

# 计算对手手上的牌
opponent_cards = defaultdict(int)
for card, count in total_cards.items():
    opponent_cards[card] = count - used_cards[card]
# 0值也是会记录的
# print(opponent_cards)

# 取键
lst = [int(card) for card in opponent_cards if opponent_cards[card] > 0]  # 每次传的card转int
lst.sort()
ans = ''
tmp = str(lst[0])

for i in range(1,len(lst)):
   
    if lst[i] == lst[i-1]+1:
        tmp +=  '-'+str(lst[i])

        
    elif len(tmp) > len(ans) or (len(tmp) == len(ans) and tmp[-1] > ans[-1]): # 顺子更长或者最后一个值更大
        ans = tmp
        tmp = str(lst[i]) 
    else:
        tmp = str(lst[i])

print(ans)



''' 
    答案

'''

from collections import Counter, defaultdict


# 将手上的牌、已经打出的牌储存为lst1和lst2
# 注意这里没有转换成数字，元素仍为字符串
lst1 = input().split("-")
lst2 = input().split("-")


# 使用计数器Counter，储存所有已经使用过的牌的个数
# 注意这里的key是str类型
cnt_using_str = Counter(lst1 + lst2)
# 如果存在2和大小王"B"、"C"
# 因为不影响顺子的判断，可以直接删去
del cnt_using_str["2"]
del cnt_using_str["B"]
del cnt_using_str["C"]


# 构建将字符转换为数字的哈希映射
convert_dic = {f"{num}": num for num in range(3, 11)}
convert_dic["J"] = 11
convert_dic["Q"] = 12
convert_dic["K"] = 13
convert_dic["A"] = 14


# 构建将数字转换为字符的哈希映射
convert_dic2 = {num: f"{num}" for num in range(3, 11)}
convert_dic2[11] = "J"
convert_dic2[12] = "Q"
convert_dic2[13] = "K"
convert_dic2[14] = "A"


# 将cnt_using_str里的key转化为int类型，对应的value不变
# 储存在一个新的哈希表cnt_using_num中
cnt_using_num = defaultdict(int)
for k, v in cnt_using_str.items():
    cnt_using_num[convert_dic[k]] = v


# 初始化三个变量
# 当前顺子长度、最长顺子长度、最长顺子对应的答案ans
cur_length = 0
max_length = 0
ans = "NO-CHAIN"

# 考虑3-15的所有数字
# 其中J、Q、K、A分别对应11、12、13、14
for i in range(3, 16):
    # 数字i被用完的情况，即在cnt_using_num中的值为4
    # 之所以把15也加入考虑
    # 是因为i取14时，由于后续没有仍然可以延长cur_length的牌
    # 会进入else中的分支，而无法实现ans的更新
    # 换句话说，当顺子最后一张牌是14的时候，需要做一次更新
    if cnt_using_num[i] == 4 or i == 15:
        # 若此时cur_length大于之前储存的max_length
        # 且cur_length大于等于5（顺子长度最低的要求）
        if cur_length >= max_length and cur_length >= 5:
            # 此时顺子为：i-cur_length, ..., i-3, i-2, i-1
            # 更新答案，注意这里要使用convert_dic2哈希表
            # 把数字重新转回字母后，再合并
            ans = "-".join(convert_dic2[j] for j in range(i-cur_length, i))
            max_length = cur_length
        # 顺子当前长度需要重置为0
        cur_length = 0
    # 数字i没被用完的情况，可以继续延长顺子
    # cur_length+1
    else:
        cur_length += 1

print(ans)
