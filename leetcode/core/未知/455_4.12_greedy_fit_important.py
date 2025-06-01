# 分发饼干
# 贪心 数组 双指针 排序

# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
# 对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。
# 如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
# 你的目标是满足尽可能多的孩子，并输出这个最大数值。

# 匹配问题 要尽可能实现更多匹配

# s = [1,2]
# g = [1,2,3]

# i移动j也跟着移动到分配的饼干的下一个位置 因为如果前面的饼干连小胃口都满足不了那么后面的胃口一定满足不了
# 因为先排序了所以不用往后看 所以之后看到最好匹配问题应该也首先想到先排序

print("mine")
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0 # 胃口指针 和 饼干指针
        count = 0 # 记录满足的数量

        while i < len(g) and j < len(s):

            # 胃口满足 胃口和饼干都移动
            if s[j] >= g[i]: # >= 和 <= 这种运算符=一直在右边
                count += 1
                i += 1
                j += 1

            # 胃口不动遍历饼干
            else:

                j += 1



        return count

s = [1,1,1] # 饼干
g = [1,2] # 小孩
print(Solution().findContentChildren(g, s)) # 1


print('\n\n贪心 双序列匹配 灵神')
class Solution2:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        i = 0

        # 通过饼干的大小来判断是否满足胃口
        # 遍历每一块饼干 如果当前饼干的大小连当前待匹配的最小胃口都匹配不了 则跳过当前饼干
        # 否则 匹配成功 胃口指针+1 饼干指针+1
        for x in s:
            if i < n and g[i] <= x:
                i += 1
        return i

s = [1,1,1] # 饼干
g = [1,2] # 小孩
print(Solution2().findContentChildren(g, s)) # 1


print("\n\nfor i in s 的用法")
s = [1,1,1,2,3,4,5,]
for x in s:
    print(x)
print('\n\n')
s = 'abcde' # 字符串可索引
for i in s:
    print(i)