# 最长公共子序列问题
# 字符串 dp
from functools import cache


# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
#
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
#
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

# abcedf bcbcfd
# 最长公共子序列为 "bcd" ，长度为 3


# 状态转移 当字符匹配时 dp[i][j] = dp[i-1][j-1] + 1
# 当字符不匹配时 dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 继承上一轮的值






# 递归 + 保存计算结果 = 记忆化搜索
class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if s[i] == t[j]:
                return dfs(i - 1, j - 1) + 1
            # 选择是重新从头匹配 还是继续匹配
            return max(dfs(i - 1, j), dfs(i, j - 1)) # 动态规划中常见的"选择最优"的思想
        

        return dfs(n - 1, m - 1)

# 1：1翻译成递推式
class Solution2:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(n + 1)] # n+1 行 m+1 列 n+1项[0]*(m+1)   

        for i, x in enumerate(s):
            for j, y in enumerate(t): 
                # f[i][j]累加的更新矩阵  存的是前ij个字符的公共子序列长度



                # 遍历第二个字符串找和第一个字符串匹配的字符然后在矩阵给每行赋值  字符串匹配一样的题
                # 行继续符\ ==else f[i+1][j+1] =  max(f[i][j + 1], f[i + 1][j])
                # 如果不匹配就更新当前状态为左边或上面的最大值 
                # 上面的是第一个字符串部分不动 第二个字符串继续匹配也就是从头匹配
                # 左边的是第一个字符串继续匹配 第二个字符串部分不动也就是继续匹配
                f[i + 1][j + 1] = f[i][j] + 1 if x == y else \
                    max(f[i][j + 1], f[i + 1][j]) 
                # 左边或上边
                
                # 选择是继续匹配还是重新匹配

                # 当字符匹配时，只能从前一个状态转移
                # 当字符不匹配时，只能从左边或上边转移
                # 这种设计确保了字符不会被重复使用
                

        return f[n][m] 


# 优化 双一维 滚动滑行数组 只需之前状态和当前状态
class Solution3:
#  空间优化:
# 原来的 Solution2 使用了 (n+1) x (m+1) 的二维数组
# Solution3 只使用 2 x (m+1) 的二维数组，通过 % 2 操作来循环使用这两行
# 索引解释:
# (i + 1) % 2: 当前要更新的行
# i % 2: 上一行
# (i + 1) % 2: 当前行
# 状态转移:
# 当 x == y 时：
# f[(i + 1) % 2][j + 1] = f[i % 2][j] + 1
# 使用上一行的前一个位置的值 + 1
# 当 x != y 时：
# max(f[i % 2][j + 1], f[(i + 1) % 2][j])
# 取上一行的当前位置和当前行的前一个位置的最大值
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(2)] # 只用两个一维数组
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                f[(i + 1) % 2][j + 1] = f[i % 2][j] + 1 if x == y else \
                                        max(f[i % 2][j + 1], f[(i + 1) % 2][j])
        return f[n % 2][m]
# # 初始状态：
# 行0: [0, 0, 0, 0]
# 行1: [0, 0, 0, 0]

# i=0 (比较 'a'):
# 行0: [0, 0, 0, 0]  <- 上一行 (i%2=0)
# 行1: [0, 1, 1, 1]  <- 当前行 ((i+1)%2=1)
# 因为 'a' 和 'a'/'c'/'e' 比较，只有 'a' 匹配

# i=1 (比较 'b'):
# 行0: [0, 1, 1, 1]  <- 当前行 ((i+1)%2=0)
# 行1: [0, 1, 1, 1]  <- 上一行 (i%2=1)
# 因为 'b' 和 'a'/'c'/'e' 都不匹配，所以保持上一行的值

# i=2 (比较 'c'):
# 行0: [0, 1, 1, 1]  <- 上一行 (i%2=0)
# 行1: [0, 1, 2, 2]  <- 当前行 ((i+1)%2=1)
# 因为 'c' 和 'c' 匹配，所以 f[2][2] = f[1][1] + 1 = 2

# i=3 (比较 'd'):
# 行0: [0, 1, 2, 2]  <- 当前行 ((i+1)%2=0)
# 行1: [0, 1, 2, 2]  <- 上一行 (i%2=1)
# 因为 'd' 和 'a'/'c'/'e' 都不匹配，所以保持上一行的值

# i=4 (比较 'e'):
# 行0: [0, 1, 2, 2]  <- 上一行 (i%2=0)
# 行1: [0, 1, 2, 3]  <- 当前行 ((i+1)%2=1)
# 因为 'e' 和 'e' 匹配，所以 f[4][3] = f[3][2] + 1 = 3


# 优化 一维
class Solution4:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        f = [0] * (len(t) + 1)
        for x in s:
            pre = 0  # f[0]
            for j, y in enumerate(t): # t遍历结束则s也结束所以f的长度为len(t)+1 每 次循环结束都更新一边f的值
                tmp = f[j + 1]
                f[j + 1] = pre + 1 if x == y else max(f[j + 1], f[j])
                pre = tmp
        return f[-1]

#  pre记录上一轮比较 该位置的最长子序列长度  保存左上角的值（即 f[i-1][j-1]）





'''
整体逻辑
第一行为0因为只能从左继承 且无论哪个字符串的前0个字符一定匹配数都为0


逐个遍历字符串a 嵌套遍历字符串b
f[i][j]永远保存的是a字符串的前i个字符到b字符串的第j个字符最多有多长能匹配 永远在更新
后续的状态转移也是由f[i][j]实现的
不匹配的时候只考虑继承 也是为了让后续匹配上后方便更新


匹配上时只会从斜上方继承后加1  这样会避免重复匹配 永远都是上一层没匹配前的状态加1 也就是保存的是上一个匹配状态
不匹配时会从左边或上边继承 



用aceace ace画矩阵观察

'''


s = "aceace"
t = "ace"
print(Solution().longestCommonSubsequence(s,t ))
print(Solution2().longestCommonSubsequence(s,t))
print(Solution3().longestCommonSubsequence(s,t))
print(Solution4().longestCommonSubsequence(s,t))
