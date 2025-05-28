# https://wv8qmy18z4.feishu.cn/docx/SPHfdxiOyogP0zx52HycAvrEnHb

# 只有两个班
lst = list(input().split()) # 分开每个小朋友的字符串
n = len(lst)
child = [] # 元素为元组
for i in range(n):
    # 分割字符串，第一个元素转为整数，第二个保持字符串
    parts = lst[i].split('/')  # 分割后返回的是字符串列表
    child.append((int(parts[0]), parts[1]))

# 用两个列表分别存储两个班级的学生
class1 = []
class2 = []

# 处理第一个学生
class1.append(child[0][0])

# 处理剩余学生
for i in range(1, n):
    if child[i][1] == 'Y':  # 如果当前学生要和前一个学生同班
        # 找到前一个学生所在的班级
        if child[i-1][0] in class1:
            class1.append(child[i][0])
        else: # 否则放入第二个班
            class2.append(child[i][0])
    else:  # 如果当前学生要和前一个学生不同班
        # 将当前学生放入另一个班级
        if child[i-1][0] in class1: # 如果前一个学生在一班因为不同班 所以当前学生在二班
            class2.append(child[i][0])
        else:
            class1.append(child[i][0])

# 对两个班级的学生编号进行排序
class1.sort()
class2.sort()

# print(' '.join(map(str,class1)))
# print(' '.join(map(str,class2)))

# 输出结果
# 如果两个班级都有学生，第一个编号小的班级先输出 无需输出第一个编号小的班级
if class1 and class2:
    if class1[0] < class2[0]:
        print(' '.join(map(str, class1)))
        print(' '.join(map(str, class2)))
    else:
        print(' '.join(map(str, class2)))
        print(' '.join(map(str, class1)))
else:
    # 如果只有一个班级有学生
    if class1:# 输出一班
        print(' '.join(map(str, class1)))
        print()  # 空行
    else:
        print(' '.join(map(str, class2)))
        print()  # 空行



# 动态规划
# 我们考虑动态规划三部曲：
# 1. dp数组的含义是什么？
# - dp数组是一个长度为n的一维列表，dp[i]是布尔变量True或者False。如果
#   - dp[i] = True表示第i个小朋友分在1班
#   - dp[i] = False表示第i个小朋友分在2班
# 2. 动态转移方程是什么？
# - dp[i]只跟dp[i-1]以及child[i][1]有关系。若
#   - 第i个小朋友和第i-1个小朋友同班，即child[i][1] == "Y"，那么dp[i] = dp[i-1]
#   - 第i个小朋友和第i-1个小朋友不同班，即child[i][1] == "N"，那么dp[i] = not dp[i-1]
# 只有两个班
lst = list(input().split()) # 分开每个小朋友的字符串
n = len(lst)
child = [] # 元素为元组
for i in range(n):
    # 分割字符串，第一个元素转为整数，第二个保持字符串
    parts = lst[i].split('/')  # 分割后返回的是字符串列表
    child.append((int(parts[0]), parts[1]))

# 用两个列表分别存储两个班级的学生
class1 = []
class2 = []

# 初始化dp数组 默认第一个小朋友在1班 则dp[0] = True
dp = [False] * n
dp[0] = True

# 遍历数组更新dp 从第二个小朋友开始
for i in range(1, n):
    if child[i][1] == 'Y': # 如果当前小朋友和前一个小朋友同班
        dp[i] = dp[i-1]
    else: # 如果当前小朋友和前一个小朋友不同班
        dp[i] = not dp[i-1] # 因为是bool类型只有两个值

# 遍历dp更新班级
for i in range(n):
    # 三元运算符写法 class1.append(child[i][0]) if dp[i] else class2.append(child[i][0])
    if dp[i]: # 如果dp[i]为True 则当前小朋友在1班
        class1.append(child[i][0]) # 要记录的是当前小朋友的编号
    class2.append(child[i][0])

class1.sort()
class2.sort()

if class1 and class2:
    if class1[0] < class2[0]:
        print(' '.join(map(str, class1)))
        print(' '.join(map(str, class2)))
    else:
        print(' '.join(map(str, class2)))
        print(' '.join(map(str, class1)))
else: # 只有一个班有学生
    if class1:# 一班不为空
        print(' '.join(map(str, class1)))
        print()
    else:
        print(' '.join(map(str, class2)))
        print()
        
