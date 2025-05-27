# 题目：2025A-寻找重复代码
# 分值：100
# 作者：闭着眼睛学数理化
# 算法：动态规划（LCS问题）
# 代码看不懂的地方，请直接在群上提问


text1 = input()
text2 = input()

# 获取 text1 的长度
m = len(text1)

# 获取 text2 的长度
n = len(text2)

# 设置数组 dp，用来存储 text1 和 text2 公共的、长度最长的子串的长度
# dp[0][0] 表示 text1 前 0 个元素和 text2 前 0 个元素的公共的、长度最长的子串的长度
# dp[2][3] 表示 text1 前 2 个元素和 text2 前 3 个元素的公共的、长度最长的子串的长度
# dp[i][j] 表示 text1 前 i 个元素和 text2 前 j 个元素的公共的、长度最长的子串的长度
# 前 i 个元素的区间为 [0, i-1]
# dp[m][n] 表示 text1 前 m 个元素和 text2 前 n 个元素的公共的、长度最长的子串的长度
# 前 m 个元素的表示区间为 [0, m]，前 n 个元素的表示区间为 [0, n]
# 因此，dp 数组的长度为 m + 1 和 n + 1
dp = [[0] * (n + 1) for _ in range(m + 1)]

# maxLength 表示 dp 数组中的最大值
maxLength = 0

# 初始化答案变量为空串
ans = ""

# 1. 初始化dp数组
# dp[0][0] 表示 text1 前 0 个元素和 text2 前 0 个元素的公共的、长度最长的子串的长度
# text1 text2 也没有元素
# 因此，公共的、长度最长的子串的长度为 0
dp[0][0] = 0

# text1 没有元素 或者 text2 没有字符时，公共的、长度最长的子串的长度都为 0
for i in range(1, m + 1):
    dp[i][0] = 0

for j in range(1, n + 1):
    dp[0][j] = 0

# i 从 1 开始，直到 m 位置，遍历 text1 的前 i 个元素
for i in range(1, m + 1):
    # j 从 1 开始，直到 n 位置，遍历 text2 的前 j 个元素
    for j in range(1, n + 1):

        # 2. 动态转移方程
        # 如果发现 text1 的当前元素，即位置为 i - 1 的元素
        # 与 text2 的当前元素，即位置为 j - 1 的元素【相同】
        # 此时，找到了一个公共元素，公共的、长度最长的子串的长度加 1
        if text1[i - 1] == text2[j - 1]:

            # dp[i][j] 表示 text1 前 i 个元素和 text2 前 j 个元素的公共的、长度最长的子串的长度
            # dp[i - 1][j - 1] 表示 text1 前 i - 1 个元素和 text2 前 j - 1 个元素的公共的、长度最长的子串的长度
            dp[i][j] = dp[i - 1][j - 1] + 1

            # 更新最长的子串的长度
            if maxLength < dp[i][j]:
                maxLength = dp[i][j]
                # 最长子串长度为maxLength，对于text1而言，
                # 当前结束位置为i，当前开始位置为i-maxLength
                # 这里换成text2[j-maxLength: j]也是一样的
                ans = text1[i - maxLength: i]

# 返回结果
print(ans)