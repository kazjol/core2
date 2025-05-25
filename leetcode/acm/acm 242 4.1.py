# 有效字母异位词 两个字符串是否包含相同字母只是顺序不同
# 首先判断两个字符串长度是否相同
# 初始化一个数组从0到25，分别记录每个字母出现的次数初始化为全0  eg：0索引对应a 0处存的值为a在第一个字符串的出现次数

# 这个通过ASCII码来判断字母是否相同，ASCII码的范围是0-127，a的ASCII码是97，b的ASCII码是98，c的ASCII码是99，以此类推，z的ASCII码是122
# 通过用ASCII码减去97，就可以得到字母在数组中的索引，然后将数组对应索引的值加1

# 遍历第二个字符串，如果当前字符在数组中存在，则将其对应索引的值减1，如果当前字符不在数组中，则将其添加到数组中并初始化为1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 判断长度 不同则返回False
        if len(s) == len(t):
            # 初始化数组
            count = [0] * 26# 初始化26个元素为0的数组
            # 遍历第一个字符串
            for i in s:
                # 字符转化为ASCII码
                index = ord(i) - 97# ord()函数返回字符的ASCII码，减去97得到字母在数组中的索引
                # 数组对应索引的值加1
                count[index] += 1# 遇到一次该数组的索引值加1
                # 遍历第二个字符串
            for i in t:
                # 字符转化为ASCII码
                index = ord(i) - 97# ord()函数返回字符的ASCII码，减去97得到字母在数组中的索引
                # 数组对应索引的值减1
                count[index] -= 1# 遇到一次该数组的索引值减1
                # 判断数组里的元素是否全为0
            for i in count:
                if i!= 0:
                    return False
            return True

        else: return False

s = input()
t = input()

print(Solution().isAnagram(s, t))

# input输入返回为字符串 中间加空格也被识别为字符串
# 但是用split()函数时默认把空格作为分隔符  .split(',')就变成用逗号作为分隔符了

list1 = list(map(int,input().split(',')))
print(list1)

