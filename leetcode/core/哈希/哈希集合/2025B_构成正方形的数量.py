# https://r07na4yqwor.feishu.cn/docx/YG5VdhAs5oDQe5xwknncxEA5nYd

def check(x1, x2, y1, y2, xy):
    a = ((x2-x1) + (y2-y1)) / 2
    b = ((x2-x1) - (y2-y1)) / 2
    x3 = x1 + b
    y3 = y1 + a
    x4 = x1 + a
    y4 = y1 - b
    if (x3, y3) in xy and (x4, y4) in xy:
        return 1
    else:
        return 0


xy = []
n = int(input())
for i in range(n):
    (a, b)= map(int, input().split())
    xy.append((a, b))
# print(xy)

ans = 0

# 枚举所有点 两个为一组 求正方形数量
for i in range(n):
    x1, y1 = xy[i]
    for j in range(i+1, n):
        x2, y2 = xy[j]
        ans += check(x1, x2, y1, y2, xy)

# 会出现重复求的情况 例如求完 1，2组点的搭配3，4组点 因为是枚举所以求3，4组点的时候又会再次求1，2组点的搭配也记录到答案里
print(ans // 2)