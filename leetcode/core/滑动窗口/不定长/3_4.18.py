# 无重复字符的最长子串 kmp算法
# 哈希表 字符串 滑动窗口

# 给定一个字符串s ，请你找出其中不含有重复字符的最长子串的长度。

# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


# 滑动窗口right遍历数组
# 如果right碰到相同的元素left就向右移动 然后记录max_len



# 哈希表 集合 字典 字符串
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        print('mine 用的哈希字典键值匹配 滑动窗口')
        # 初始化哈希表 字典 记录索引和字符
        s = list(s) # 也不用转表 字符串本身就可以索引
        n = len(s)
        str_dic = {}

        max_len = 0
        print(s)

        if n <= 1:
            return n

        # 初始化滑动窗口
        left = 0
        right = 0
        while right < n and left <= right:
            # 右指针向右移动


            if s[right] in str_dic.keys():

                index = str_dic.get(s[right]) # 找到重复字符的索引
                print('index:',index)
                for i in range(left, index+1):
                    str_dic.pop(s[i]) # 前面的要清空

                left = index + 1 # 左指针向右移动 跳过重复字符
                str_dic[s[right]] = right # 更新索引 且前面的要清空




            max_len = max(max_len, right - left+1) # 记录最大长度
            str_dic[s[right]] = right  # 记录索引和字符 字符是键索引是值 字典是通过键匹配找值
            right += 1 # 右指针向右移动




        print(str_dic)


        return max_len # 因为left-right+1才是长度


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print('\n\nod 解法 集合')
        # 集合的优点 在于会自动去重 无需额外处理

        # 滑动窗口模板化解题，五步走策略

        # 【1、定义需要维护的变量】

        # 对于此题来说，要求是最大长度
        maxLen = 0

        # 同时又涉及去重用集合，因此需要一个哈希表
        # 用集合判断如果 在集合里存在则重复

        hash = set()

        # 【2、定义窗口的首尾端 (start, end)or(left,right)， 然后滑动窗口】

        # 窗口的左端位置从 0 开始
        start = 0

        # 窗口的右端位置从 0 开始，可以一直移动到尾部
        for end in range(len(s)):

            # 【3、更新需要维护的变量, 有的变量需要一个 if 语句来维护 (比如最大最小长度)】

            # 【4、如果题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题】
            #  如果当前窗口不合法时, 用一个 while 去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法

            # 如果哈希表中存储了即将加入滑动窗口的元素

            while s[end] in hash: # 集合和字典都是不可索引的 用的查找方式是键值匹配

                '''
                # 一直减小窗口大小 遍历的形式
                # 1、不用集合：直到遇到重复的元素
                # 2、*****用集合：直到集合中找不到重复的元素 此时就能保证把重复前的元素清空*****
                    循环移除
                
                '''
                # 把 s.charAt(start) 移除记录
                hash.remove(s[start])
                #remove(key) 移除字典中键对应的值，如果不存在则抛出KeyError异常
                # remove()函数只删除第一个匹配项

                # 窗口左端向右移动 窗口缩小
                start += 1

            # 此时，滑动窗口可以接纳 s.charAt(end)
            hash.add(s[end])

            # 维护变量 maxLen
            maxLen = max(maxLen, end - start + 1)

        # 【5、返回所需要的答案】
        return maxLen


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print('\n\nleetcode 解法 字典')
        dic, res, left = {}, 0, -1 #
        for right in range(len(s)):
            if s[right] in dic: # 都是用键匹配 主要数据部分是值
                # 直接更新下标呢
                # left = dic[s[right]] # 更新左指针 left

                # 会出错 当连续碰到重复元素的时候 left和right会撞到一起 字典里保存的时上个重复元素的索引
                # 直接赋给left还是会有重复元素 所以要取最大值保证一定没有重复元素

                # 对于字典而言因为是哈希表 根据关键字匹配的所以不能有重复的关键字 出现重复的关键字会覆盖之前的

                 left = max(dic[s[right]], left) # 更新左指针 left
            dic[s[right]] = right # 哈希表记录   键是字符 值是索引  字典一般都是这样的因为键可以匹配搜索得到值
            res = max(res, right - left) # 更新结果
        return res



s = "abba"
print(Solution().lengthOfLongestSubstring(s))
print(Solution2().lengthOfLongestSubstring(s))
print(Solution3().lengthOfLongestSubstring(s))



class Test:
    def test(self):

        print('\n\ntest')
        nums = [1, 2, 3, 10, 5, 6, 7, 8, 9, 10]
        print( nums[0:3])
        t = 'abcabcbb'
        print(t.index('b'))
        print(list(t))
        k = {}
        for i in range(len(nums)):
            k[nums[i]] = i
        print(k)
        print(k.keys()) # 字典前面是键 后面是值 且字典不允许重复键
        print(k.get(10))
# print(Test().test())