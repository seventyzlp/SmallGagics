import random

n = int(input("请输入样本数量:"))
m = int(input("请输入实验次数:"))
people = []
percent = []
t = 0
for j in range(m):
    birth = [0] * 366  # 重置生日情况
    for i in range(n):
        people.append(random.randint(1, 365))
    for i in people:
        birth[i] += 1
    for i in birth:
        if i >= 2:
            t += 1
    percent.append(t / n) # 算出每一次的成功几率
t = 0
for i in percent:
    t += i
print("最终统计得出的概率为" + str(t / m))
