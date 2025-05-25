# 最小覆盖字串
# 哈希表 字符串 滑动窗口
# 窗口大小可变


# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。子串是顺序不能变的
# 如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。


# 示例1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串"BANC"包含来自字符串t的 'A'、'B'和'C'。
# 示例2：
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串s是最小覆盖子串。
# 示例3:
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t中两个字符'a'均应包含在s 的子串中，因此没有符合条件的子字符串，返回空字符串。
import collections
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        res_final = s
        left, right = 0, 0
        dictmid = collections.defaultdict(int) # 中间字典
        # 哈希表 先统计t中每个字符出现的次数 Counter
        t_count = Counter(t)
        s_count = Counter(s)
        # print(t_count)
        # print(s_count)
        for ch in t: # 字典是键匹配制的
            if s_count[ch] < t_count[ch]:
                return ""


        #滑动窗口固定for 套 while
        for right in range(0,len(s)):
            dictmid[s[right]] += 1  # 记录窗口中字符出现的次数


            if s[right] in t_count.keys():
                # 判断集合子集
                # # 使用 issubset() 方法
                # is_subset = set(t_count.keys()).issubset(set(dictmid.keys()))
                #
                # # 或者使用 <= 运算符
                # is_subset = set(t_count.keys()) <= set(dictmid.keys())
                if all(t_count[key] == dictmid[key] for key in t_count):  # t里面的字符必须全部出现在dic中 遍历关键字 结果是个bool值
                    res = s[left:right + 1]  # 记录最小覆盖子串 切片操作

                    if len(res) < len(res_final):
                        res_final = res


                    # right += 1  # 右移窗口
                elif dictmid[s[right]] > t_count[s[right]]:  # 全部出现但出现次数超了

                    while set(t_count) == set(dictmid) and dictmid[s[right]] > t_count[s[right]] :  # 窗口中字符出现的次数超了
                        dictmid[s[left]] -= 1  # 窗口中字符出现的次数减1 按照窗口从左到右的顺序
                        left += 1  # 左移窗口
                        # 每次都要清多余的尾端元素

            while s[left] not in t_count.keys():
                dictmid[s[left]] -= 1
                left += 1
                # 清完还应该加个判断
                # 最后判断一下是否满足条件 因为假如最后一个才满足无法返回for循环里的判断 否则会越界
            if all(t_count[key] == dictmid[key] for key in t_count):  # t里面的字符必须全部出现在dic中 遍历关键字 结果是个bool值

                res = s[left:right + 1]  # 记录最小覆盖子串 切片操作

                # min() 函数在字符串上的使用并不是按照长度来比较的，
                # 而是按照字典序来比较的。因此，这段代码并不能保证 res_final 会被赋值为更短的字符串。
                if len(res) < len(res_final):
                    res_final = res

            right += 1





        return res_final


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        # 使用整型数组来表示每个字符在 t 中的数量，初始化都为 0，利用 ASCII 码的方式把字符存储到整型数组中
        # 这个就是不用哈希表（字典 和 Counter对象）的方法 用ASCII就是代替哈希表
        # 数组的长度设置为 128
        # 其中 65 ～ 90 号为 26 个大写英文字母，97 ～ 122 号为 26 个小写英文字母，其余为一些标点符号、运算符号等
        # 由于 t 是由英文字母组成，所以数组中有些位置的值始终不会被操作，造成了空间的浪费，比如 map[20]map[30]
        # 但这样做方便理解，比如看到 map[98] = 5 ，能知道 b 出现的频次是 5 次

        # 防止访问到没有的关键字时报错
        map = collections.defaultdict(int)

        # 开始统计 t 中每个字符出现的频次 map统计的是t中每个字符出现的次数
        for ch in t:  # 初始化需要的必要字符数量
            map[ch] += 1 # ch时是关键字

        # 记录滑动窗口的长度，并且不断更新获取最小的那个
        windowLength = len(s) + 1

        # 滑动窗口的左端
        left = 0

        # 滑动窗口的右端
        right = 0

        # t 中字符的总个数***
        count = len(t)

        # 滑动窗口左端新的位置
        start = 0

        # 滑动窗口的右端开始移动
        while right < len(s):

            # 获取此时将要加入到滑动窗口的元素
            c = s[right]

            # 如果说 map 数组中 c 出现的频次大于了 0，说明此时字符 c 加入到滑动窗口距离找到这样一个子串更近了一步
            # 那么滑动窗口需要搜罗的特定元素个数变少了

            # t中还有没出现完的字符 直到map中字符出现的次数都为0就满足条件可以记录了
            # ***主要这里有关键的一点是 t中的所有元素都要包括 包括t中的重复部分 所以统计次数一直减到0
            if map[c] > 0:
                # 需要搜罗的和 t 中字符一样的元素个数变少了
                count -= 1

            # 既然滑动窗口中新增了一个字符 c，那么 map 数组中对应的频次就需要减 1
            map[c] -= 1

            # 如果此时 count == 0 ，表明滑动窗口中包含了 t 中全部的字符
            # 此时，找到了一个符合条件的子串
            # 但想尝试一下，能否满足条件的情况下子串更短一些
            # 于是，去尝试把滑动窗口的左端向右移动一下
            # 可以移动的前提是，滑动窗口的左端元素抛弃后剩下的元素依旧满足条件
            # 意思就是实际上左端元素是多余的
            # 而如果这个元素对应的值在 map[] 数组中小于 0，说明它是一个多余元素
            # 反复的删除这些多余的元素

            # count不是单独一个字符的出现次数是全部的出现次数

            # 清除尾端元素 因为count是t中全部元素的计数 如果删除的元素不在t里那么count会一直不变
            # 遍历移动左端口
            while count == 0:

                # 如果当前的这个窗口值比之前维护的窗口值更小，需要进行更新
                if right - left + 1 < windowLength:
                    # 更新滑动窗口的长度
                    windowLength = right - left + 1

                    # 更新滑动窗口起始位置，来到了 left 这个位置
                    start = left

                # 接下来左端位置开始向右移动，也就是一个删除操作
                # 删除操作需要执行以下三个步骤
                # 如果这个元素不是多余的元素，比如滑动窗口为 ADBC，t 为 ABC
                # 移除了 A，那么滑动窗口又需要去新增其它的元素了
                # 所以通过 map[s.charAt(left)] == 0 来判断它是否是多余的元素

                # 如果当前删除的这个左端元素是需要的元素 并且这个元素个数刚好等于 t 中该元素的个数 那么删除之后还需要补上

                """
                # ***eg：s='ACBBABA' t='AB' 当遍历到ACB时 count==0 更新window 到left的位置
                # 因为每次当匹配时 也就是count==0时 while循环每次都删一个左边元素 直到左端指针指向的不是多余的元素 其实这个思想和我的一样 做尾端元素处理
                # 如果此时删除的元素不是多余的元素 那么所需要凑的元素就多一个 所以 count += 1
                """
                if map[s[left]] == 0:

                    # 需要搜罗的和 t 中字符一样的元素个数要增加一个了，因为删除了关键元素
                    count += 1

                # 2、这个元素离开了滑动窗口，那么在 map 中这个的值就需要加 1
                # 对应着上面新增一个元素到滑动窗口，map[c]--
                # map 需要搜找的元素个数增加一个
                map[s[left]] += 1

                # 3、left 向右移动，那么这个元素就离开了
                left += 1

            # 可以开始查看新的元素了
            right += 1 # 每次遍历左端口也是动的

        # 根据 s 中是否涵盖了 t 所有字符的子串来获取结果



        # 这个判断语句非常好用 可以省略很多代码
        return '' if windowLength == (len(s) + 1) else s[start:start + windowLength]
s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"

# 请选择 Python3 提交代码，而不是 Python
class Solution3:
    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_right = -1, len(s)
        cnt_s = Counter()  # s 子串字母的出现次数 初始化空 最后比较子串和匹配串
        cnt_t = Counter(t)  # t 中字母的出现次数

        left = 0
        for right, c in enumerate(s):  # 移动子串右端点 enumerate解决边界问题
            cnt_s[c] += 1  # 右端点字母移入子串

            # 字典这里 用是否涵盖可以直接判断 非常关键

            while cnt_s >= cnt_t:  # 涵盖 说明cnt_t的全部关键字都在cnt_s中出现过且次数相同或更小  等同于这句的意义all(t_count[key] == dictmid[key] for key in t_count):
                if right - left < ans_right - ans_left:  # 找到更短的子串 子串比上一组更短->更新
                    ans_left, ans_right = left, right  # 记录此时的左右端点
                cnt_s[s[left]] -= 1  # 左端点字母移出子串 一直移到数量不多于t 也就是当前没有出现多余的元素的最小情况
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]


print("mine 没解出来",Solution().minWindow(s, t))
print("\n\nod",Solution2().minWindow(s,t)) # print在多参数输出的时候会自带空格
print("\n\n灵神",Solution3().minWindow(s,t))








class Test:
    def test(self):
        a = "abc"
        a = list(a)
        a.append("1")
        print('\n\n',a[0])
        print(a)
        a = str(a)

        b = "123"
        print(b)
        # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        b = "".join(b + x for x in a )

        print(b)


        s = "ADOBECODEBANC"
        t = "ABC"
        print('min：',min(s,t))
# print(Test().test())