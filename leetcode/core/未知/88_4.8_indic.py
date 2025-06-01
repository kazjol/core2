# 双指针  指针就是索引

# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。


# 给定数组是递增有序数组，因此可以用双指针来合并两个数组 两个数组各设定一个指针
# 每次比较两个指针指向的元素大小，将较大的元素放到 nums1 的末尾，逆序遍历 否则可能出现覆盖的情况



from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1
        j=n-1
        cur = m+n-1 # 增加插入位置的指针更易读 current 指针当前插入位置
        while i>=0 and j>=0:
            if nums2[j] < nums1[i]:
                nums1[cur]=nums1[i]
                i-=1
                cur-=1

            else:
                nums1[cur]=nums2[j]
                j-=1
                cur-=1
        while j >= 0 > i: # j>=0 and i<0 说明 nums2 已经遍历完了，但是 nums1 还有剩余元素，需要将剩余元素填充到 nums1
            nums1[cur]=nums2[j]
            j-=1
            cur-=1

        print(nums1)
nums1 = [0]
m = 0
nums2 = [1]
n = 1
Solution().merge(nums1, m, nums2, n)

nums3 = [1,2,3,0,0,0]
reverse_nums3 = nums3[::-1] # 反转数组 切片操作默认包含起始不包含结束 且默认起始是第一个默认结束是最后一个 默认步长为1

print(reverse_nums3)


