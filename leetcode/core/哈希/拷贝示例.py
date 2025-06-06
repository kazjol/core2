# 浅拷贝中第一层和深层的区别示例

# 示例1：嵌套列表
print("示例1：嵌套列表")
original = [1, 2, [3, 4], {'a': 5}]  # 包含数字、列表和字典的嵌套结构
shallow_copy = original.copy()        # 浅拷贝
deep_copy = copy.deepcopy(original)   # 深拷贝

print("原始数据:", original)
print("浅拷贝:", shallow_copy)
print("深拷贝:", deep_copy)
print("-" * 50)

# 1. 修改第一层（数字）
print("1. 修改第一层（数字）")
original[0] = 9
print("修改后 - 原始数据:", original)      # [9, 2, [3, 4], {'a': 5}]
print("修改后 - 浅拷贝:", shallow_copy)    # [1, 2, [3, 4], {'a': 5}]  # 不受影响
print("修改后 - 深拷贝:", deep_copy)       # [1, 2, [3, 4], {'a': 5}]  # 不受影响
print("-" * 50)

# 2. 修改深层（嵌套列表）
print("2. 修改深层（嵌套列表）")
original[2][0] = 9
print("修改后 - 原始数据:", original)      # [9, 2, [9, 4], {'a': 5}]
print("修改后 - 浅拷贝:", shallow_copy)    # [1, 2, [9, 4], {'a': 5}]  # 受影响！
print("修改后 - 深拷贝:", deep_copy)       # [1, 2, [3, 4], {'a': 5}]  # 不受影响
print("-" * 50)

# 3. 修改深层（嵌套字典）
print("3. 修改深层（嵌套字典）")
original[3]['a'] = 9
print("修改后 - 原始数据:", original)      # [9, 2, [9, 4], {'a': 9}]
print("修改后 - 浅拷贝:", shallow_copy)    # [1, 2, [9, 4], {'a': 9}]  # 受影响！
print("修改后 - 深拷贝:", deep_copy)       # [1, 2, [3, 4], {'a': 5}]  # 不受影响
print("-" * 50)

# 4. 添加新的深层元素
print("4. 添加新的深层元素")
original[2].append(5)
print("修改后 - 原始数据:", original)      # [9, 2, [9, 4, 5], {'a': 9}]
print("修改后 - 浅拷贝:", shallow_copy)    # [1, 2, [9, 4, 5], {'a': 9}]  # 受影响！
print("修改后 - 深拷贝:", deep_copy)       # [1, 2, [3, 4], {'a': 5}]  # 不受影响
print("-" * 50)

'''
浅拷贝中第一层和深层的区别：

1. 第一层（直接元素）：
   - 浅拷贝会创建新的对象
   - 修改原始对象的第一层元素不会影响浅拷贝
   - 例如：修改 original[0] 不会影响 shallow_copy[0]

2. 深层（嵌套对象）：
   - 浅拷贝只复制引用，不创建新的对象
   - 修改原始对象的深层元素会影响浅拷贝
   - 例如：修改 original[2][0] 会影响 shallow_copy[2][0]

3. 为什么会有这种区别：
   - 浅拷贝只复制第一层，创建新的容器对象
   - 但容器内的对象（深层）只是复制了引用
   - 所以深层对象仍然是共享的

4. 深拷贝的区别：
   - 深拷贝会递归地复制所有层级的对象
   - 每一层都创建新的对象
   - 所以修改任何层级都不会相互影响

5. 实际应用中的注意事项：
   - 如果只需要独立的第一层数据，用浅拷贝
   - 如果需要完全独立的数据，包括嵌套对象，用深拷贝
   - 浅拷贝性能更好，但要注意深层数据的共享问题
''' 