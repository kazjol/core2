# https://og7kl7g6h8.feishu.cn/docx/CWBZd8sw4oMj5OxWemmc90xhnJo
from copy import copy
from typing import List, Counter


def fit(words:List[str],chars:str,n:int)->int:
    ans = 0
    chars = Counter(chars)
    
    # print(every)
    # chars = set(chars) # char的每个字母只能用一次

    for s in words:
        s = Counter(s)
        tmp  = copy(chars)
        for c in s: # 这种默认是遍历关键字 遍历值的话是for i in tmp.value()
            if c not in tmp:
                tmp['?'] -= s[c]
            elif tmp[c] > s[c]:
                tmp[c] -= s[c]
            elif tmp[c] < s[c]:
                 
                tmp['?'] -= s[c] - tmp[c]
                tmp[c] = 0 

        if tmp['?'] >= 0:
            ans += 1
        

    return ans


n = int(input())
words = []
for i in range(n):
    words.append(input())
chars = input()
# print(words, chars)
print(fit(words,chars,n))