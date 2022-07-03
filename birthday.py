# 运用随机数的生成来解决24人，在实验10000次时，概率为0.5372
import random

n = int(input("请输入样本数量:"))
m = int(input("请输入实验次数:"))
people = []
percent = []
t = 0
for j in range(m):
    birth = [0] * 366  # 重置生日情况
    people = []  # 每趟运行重置生日情况
    for i in range(n):
        people.append(random.randint(1, 365))  # 随机设置n人初始的生日情况
    for i in people:  # 桶
        birth[i] += 1
    for i in birth:
        if i >= 2:
            t = 1
    percent.append(t)  # t为1说明这一趟下来有重复生日的情况
    t = 0
t = 0
for i in percent:  # t是累计成功次数
    t += i
print("最终统计得出的概率为" + str(t / m))

