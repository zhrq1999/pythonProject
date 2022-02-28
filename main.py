import numpy as np
import matplotlib.pyplot as plt

# a = 1
# t = np.linspace(0, 2*np.pi, 1024)
# X = a*(2*np.cos(t)-np.cos(2*t))
# Y = a*(2*np.sin(t)-np.sin(2*t))
# plt.plot(Y, X, color='r')
# plt.show()


# a = 16
# b = 5
# # 三元运算符
# d = a if a > 15 else b
# print(d)

# # 列表 有序
# stu = ['LiSi', 'zs']
# stu1 = ['make', 'john']
# # 插入
# stu.insert(0, "wangWu")
# # 列表合并
# stu.extend(stu1)
# # 列表嵌套
# stu.insert(2, [1, 2, 3])
# # del 删除
# del stu[2][1]
# # pop删 默认删除最后一个元素并返回被删除的值
# print(stu.pop())
# print(stu.pop(0))
# # 修改
# stu[0] = "蔡徐坤"
# stu[-1] = "肖战"
# print(stu)
#
# for i in stu:
#     print(i)

# 字典

# 创建法一
person = {"name": "alex", 'age': 20}

# 创建法二
person = dict(name='seven', age=20)
print(person)

# 创建法三:批量生成默认value
keys = [1, 2, 3, 4, 5]
print({}.fromkeys(keys, 100))

# 新增
person["job"] = "Teacher"
print(person)


