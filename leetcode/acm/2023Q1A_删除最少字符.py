# 删除字符串中出现次数最少的字符 出现次数最少的出现次数一样就都删掉
# 输出：剩余的字符串 如果没有字符，输出empty


# 仍然使用Counter（）

from collections import Counter

lst = input()

cnt = Counter(lst)

min_cnt = min(cnt.values())

del_lst = set()

for ch,num in cnt.items(): # ch character
    if num == min_cnt:
         del_lst.add(ch)
print(del_lst)

ans = list() # 存剩余的字符串

for ch,nums in cnt.items():
    if ch not in del_lst:
        ans.append(ch)

if len(ans) == 0:
    print("empty")

else:
    print(ans)
    print("".join(ans)) # join()函数将列表中的元素连接成字符串


