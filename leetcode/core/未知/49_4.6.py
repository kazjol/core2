# 异位词
# 给你一个字符串数组，请你将字母异位词组合在一起。可以按任意顺序返回结果列表。
# 字母异位词是由重新排列源单词的所有字母得到的一个新单词。
# 把字母组成相同的单词构成一个列表返回

# 对列表中的每个字符串进行统计并生成关键字 例如ate->a1t1e1 然后遍历字符串把关键字相同的字符串放到一起也就是把他们的value并起来然后作为列表返回
import collections
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #collections 是 Python 的一个内置模块，提供了一些额外的容器数据类型，用于简化常见的编程任务。
        # defaultdict 是 collections 模块中的一个子类，它继承自 dict（字典）。defaultdict 的特性是，当访问不存在的键时，它会自动创建该键，并且为其赋予一个默认的值。
        # 这在处理需要动态添加键值对的数据结构时特别有用，可以避免由于访问不存在的键而引发的 KeyError 异常。一般初始化一个空字典时访问不存在 的键会出错，而使用 defaultdict 可以避免这种情况。


        map1 = collections.defaultdict(list)
        counts = [0]*26# 统计每个字母出现的次数
        for s in strs:# 遍历字符串列表
            counts = [0] * 26  # 统计每个字母出现的次数 counts要在循环里定义
            for c in s:# 遍历字符串

                counts[ord(c)-97]+=1# 统计每个字母出现的次数
            key = ''.join(['#'+str(i) for i in counts]) # 遍历counts然后加到字符串里生成关键字存到map1里
            # 把key作为key 存到map1里
            # 把字符串s 存到map1里 作为value部分

            map1[key].append(s) # 把字符串s 存到map1里对应的key的value部分 
        return list(map1.values())# 把map1里的value部分取出来组成列表返回


strs = ["eat", "tea", "tan", "ate", "nat", "bat"] # 列表是可以索引的
print(Solution().groupAnagrams(strs))






print('/////////////////////////////////////////////////////////////////////////////')
strs = ["eat", "tea", "tan", "ate", "nat", "bat"] # 列表是可以索引的
print(strs[0])
print(Solution().groupAnagrams(strs))
for s in strs:
    print(s) # 可以直接遍历列表元素 因为列表时可索引的
