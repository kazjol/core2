# https://wv8qmy18z4.feishu.cn/docx/BG7VdnLq8okrmSx3ZeccUl0jn1f


# 输入：输入：books = 20,16,15,11,10,10,9,10
# 第一本书： 20 16 长宽
# 同面试题17.08马戏团人塔 做双重排序


# 动态规划

books = list(map(int,input().split(',')))
long = [books[i] for i in range(len(books)) if i % 2 == 0] # 除常数取余得间隔数
wide = [books[j] for j in range(len(books)) if j % 2 == 1] 
# 元素类型为tuple的列表
books = list(zip(long,wide)) # 先按长排序后面只用考虑宽 宽度要降序

'''
    简化写法
    # books = [(lst[i], lst[i+1]) for i in range(0, len(lst), 2)] 步长为2
'''

books.sort(key=lambda x: (x[0],-x[1])) # key是关键字代表此时的lambda函数作为输入参数
# print(books)
dp = [1] * len(books) # 初始化dp数组  每本书都可以叠在自己上面

for i in range(1,len(books)):
    temp = 0
    for j in range(i): # 遍历之前的全部状态取最大值
        if books[i][1] > books[j][1]: # 如果当前书的长宽都小于等于之前的书(只用比较tuple[1]宽)，则可以叠到当前书上  ***不能加等于因为要求的是只有大于
            temp = max(temp,dp[j]) # 取最大值
            '''
                简化写法 直接更新dp[i]就行
            '''
            dp[i] = max(dp[i],dp[j]+1)

    dp[i] = temp + 1 # 当前书可以叠到当前i本书上 
print(max(dp)) # 输出最多可以叠放多少本书



# 贪心+二分

lst = list(map(int,input().split(',')))
books = [(lst[i],lst[i+1]) for i in range(0,len(lst),2)]

books.sort(key=lambda x: (x[0],-x[1])) # key=lambda x: (x[0],-x[1])参于sort的输入元素 这里key关键字也就是说明参数x是指调用的变量books的元素  其实也就是key=x x就是books的key然后lambda函数对x做操作
ans = [books[0][1]] # 答案列表 装最后的叠哪些书
def binary_search(ans,target): # 这里输入的插入列表是ans
    left,right = 0,len(ans) # 左闭右开区间写法
    
    while left < right: # 左闭右开区间写法，取不到右边界，避免死循环
        mid = (left+right)//2 # mid = (left+right)>>1
        if ans[mid] >= target: # 中间值大于target 取左半表才能找到第一个大于等于target的值
            right = mid # 因为mid可能是答案，所以right = mid
        else:
            left = mid + 1 # mid不可能是答案，所以left = mid + 1
    ans[left] = target # 最后left和right相等，就是我们要找的位置


# 贪心 遍历列表每次取最优的序列也就是插入到最优的位置
for i in range(1,len(books)): # for l, w in books遍历元组的元素
    if books[i][1] > ans[-1]: # 最后一个元素都大 可以被之前的书叠
        ans.append(books[i][1])
    else:# 当前书的重量 找到插入位置则可以使已有的书能叠到更多的重量之上
        binary_search(ans,books[i][1])
    
print(len(ans))










            
            




