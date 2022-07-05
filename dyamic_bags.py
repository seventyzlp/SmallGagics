import random

bag = 10  # 设置初始背包的格子为10
cargo = []
price = []
i = 0
# 初始化背包设定
while i <= 10:
    i += 1
    cargo.append(random.randint(1, 10))  # 奇数位是物品的大小
    price.append(random.randint(1, 100))  # 偶数位是物品的价值
# 进行分析处理，首先要进行排序
print(cargo)
for j in range(1, len(cargo) + 1):  # 总循环次数
    for i in range(-1, -len(cargo) - 1 + j, -1):
        if cargo[i] < cargo[i - 1]:
            t = cargo[i - 1]
            cargo[i - 1] = cargo[i]
            cargo[i] = t
print(cargo)