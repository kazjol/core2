# https://og7kl7g6h8.feishu.cn/docx/CId9dzOzHoQ3guxXZa8cTTbVnAc
from typing import List
class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        lst = sorted(zip(height, weight), key = lambda x: (x[0], -x[1])) # sorted()返回排序完的数组（新建的数组） lst.sort()是对原数组进行排序没有返回值
        w_lst = [w for h,w in lst]
        n = len(w_lst)
        dp = [1] * n
        for i in range(1, n):
            # 遍历之前的所有人的状态 如果当前人i的重量大于之前j的重量 则说明之前的人能踩到当前人上
            # 最后取最大的状态来用作更新当前人的状态
            lst = [ dp[j] for j in range(i) if w_lst[i] > w_lst[j] ]
            if len(lst) > 0:
                dp[i] = max(lst) + 1
        return max(dp)











# 贪心+二分，最长递增子序列LCS轻变式
from typing import List
class Solution:
    def binarySearch(self, ans, num):
        left, right = 0, len(ans) # 左闭右开 初始化 左边界可去右边界取不到 ***闭区间会死循环
        while(left < right): # 只取不到右边按
            mid = (left+right) >> 1
            if ans[mid] >= num: # 中间值大于target 取右半表才能找到第一个大于等于target的值
                right = mid # 因为当前元素满足大于等于target所以直接做表尾不用跳过
            else:# 当前元素小于所以直接跳过该元素设下一个元素为表头
                left = mid + 1
        ans[left] = num

    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        # 贪心 + 二分：最长递增子序列LCS轻变式
        lst = list(zip(height, weight)) # zip函数将两个列表合并成元组 列表元素是元组 元组是可索引的 第一个元素是身高 第二个元素是重量
        # 按照身高升序，重量逆序，对原数组lst进行排序
        # 因为元组首先会以第一个元素排序，如果第一个元素相同，则以第二个元素排序 身高升序，重量逆序所以要用lambda函数
        # lambda函数把每个输入参与排序的元组的第二个元素取负值，使得重量大的在前面
        lst.sort(key = lambda x : (x[0], -x[1])) # 按照身高升序，重量逆序排序 里面的元组已经保证身高排好序了后面的一定比前面高所以只用考虑重量了
        ans = [lst[0][1]] # 初始化第一个人是身高最低重量最小的人
        for h, w in lst:
            if w > ans[-1]: # 如果当前人重量大于等于上一个人的重量 则说明之前的人能踩到当前人上
                ans.append(w) 
            else:
                self.binarySearch(ans, w) # 当前人不满足的情况 用二分法找到插入位置优化答案列表 因为后面的重量更小 已有列表里重量越小则越能多踩一些人***
        return len(ans)
height = [65,70,75,80]
weight = [100,150,190,200]
print(Solution().bestSeqAtIndex(height, weight)) # 3