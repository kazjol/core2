'''
python 常用内置函数https://zhuanlan.zhihu.com/p/666496949
'''
# 常用快捷键
# ctrl s 保存当前文件
# ctrl n 新建文件
# ctrl / 注释当前行
# ctrl x 剪切当前行到剪切板
# ctrl z 撤销上一次操作
# ctrl y 粘贴剪切板内容
# ctrl a 全选文档
# ctrl y 复制当前行
# ctrl d 复制当前行到下一行
# ctrl g 跳转到指定行
# ctrl f 搜索关键字
# ctrl h 替换关键字
# ctrl shift k 删除当前行到结尾
# ctrl shift d 复制当前行到下一行并删除当前行
# ctrl shift j 合并当前行和下一行
# ctrl shift a 查找
# ctrl shift h 全局替换关键字
# ctrl shift c 复制当前行到下一行并注释掉当前行
# ctrl shift t 交换当前行和上一行
# ctrl shift - 展开折叠代码块
# ctrl shift v 选择要粘贴的内容
# ctrl shift 数字 添加书签



# 终端命令
# You are using pip version 10.0.1, however version 24.0 is available.
# You should consider upgrading via the 'python -m pip install --upgrade pip' command.
# python -m pip install --upgrade pip 先输入python再输入命令

# python 库函数地址 C:\Users\lsj>c:\users\lsj\appdata\local\programs\python\python313\lib

# 右下角有解释器的地址 点进去可以配置解释器还可以下软件包 增加功能和要用的函数u
s=5
while s:
    s-=1
    if  s<2:
        break
print("Hello, world!")
# break 会结束当前循环，并跳出循环体整个循环



print('\n//////////////////////////////////////////////////////////////////')
nums = [1, 2, 3, 4, 5]
for i in range(len(nums)):
    if nums[i] < 4:
        continue # continue会直接跳过当前循环，继续下一次循环
    print(nums[i])

