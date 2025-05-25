# 集五福 0和1组成长度为5的字符串代表每个人集到的福卡 每一位代表一种福卡 1表示已经得到该福卡 单类型福卡不超过1张
# 随机抽一个小于10人的团队 求团队最多集齐多少套五福
# 输入：若干由0和1组成的长度为5的字符串，每个字符串代表一个人的福卡集齐情况
# 输出：团队最多能集齐多少套五福



# 把输入的字符串按索引位置存入新的数组，遍历数组取最小索引值

# 用到counter

from collections import Counter # 统计元素出现的次数

lst = input().split(',') # 输入的字符串按逗号分割 一个字符串代表一个人

cnt = Counter() # Counter是一个字典类型 Counter（）能创建一个Counter类的对象 这个对象可以用Counter的特点

for person in lst: # 遍历每个人
    for i,card in enumerate(person): # enumerate函数可以同时获得索引和值 i是索引card是值
        if card == '1': # 如果该人已经得到该福卡
            cnt[i] += 1 # 则该福卡计数器加1 i该卡的索引也就是类型
print(cnt)

# Counter()是一个字典类型 所以可以调出values()方法来查看关键字出现次数 也可以调用keys()方法来查看关键字
# Counter()可以允许值为0 但是dict()不允许 需要做初始化
print(f"最多可以集齐{min(cnt.values())}套五福") # min函数取最小值



