# https://og7kl7g6h8.feishu.cn/docx/TEB6dxDfboFmvnxbg7xcmqXjn8c

# 数据类型还是数组 要先简化数据为单个数据再做二分 


# 自动转换为新数组
from typing import List


def new_img(img:list,k:int)->int:
    new_img = [i + k for i in img] 
    # 加完后要自动归到[0,255]
    for i in range(len(img)):
        if new_img[i] < 0:
            new_img[i] = 0
        elif new_img[i] > 255:
            new_img[i] = 255
    return sum(new_img)/len(img) # 返回均值 //是向下取整 这里不需要
    
# 多个k满足则输出最符合的
# - 因此，存在一个特定的k = ans，能够使得新数组的所有像素值的平均值恰好大于等于128。
# 此时k = ans和k = ans - 1这两个数，都是有可能使得像素值最接近128的结果，再加上一个判断即可。
# 也就是要不然找大于等于的值和前一个值 要不然找小于等于的值和后一个值 这个也是二分实现 一般都是取大于等于的第一个数
def highb(img:List[int]):
    global k
    left,right = -255,255 # 全闭 这个地方理解错了 我们在用二分法猜k的值 k是可以取负的 这个是k的范围 不是img的范围
    
    while left <= right:
        mid = (left + right)//2
        # 要传img到highb函数 highb函数内部调用new_img函数才能取到img
        if new_img(img,mid) >= 128: # 找第一个大于等于128的数  所以往左缩 当前值满足且全闭区间 直接赋值mid
            right = mid -1
        else:
            left = mid + 1 # 返回时left是第一个满足条件的值
    k=left
   
k = 0
img = list(map(int,input().split()))
n=len(img)
highb(img)

if abs(128-new_img(img,k)) < abs(128-new_img(img,k-1)):
    print(k)
elif abs(128-new_img(img,k)) > abs(128-new_img(img,k-1)):
    print(k-1)
else:
    print(min(k, k-1))  # 如果差距相等，输出较小的k
