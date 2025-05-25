# 第一次输入 为输入的数据的个数
# 后面两行为一组数据 输出结果为一组数据的第二行的和



a = int(input()) # 读取输入的数据组数

for i in range(0,2*a): # 循环读取每组数据 因为每组数据有两行 所以range是2*a
    b = list(map(int,input().split())) # 求每行元素和
    if i % 2 == 1: # 如果是奇数行 则代表当前组数据的第二行 则输出和
        print(sum(b))