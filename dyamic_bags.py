import random

bag = 10  # 设置初始背包的格子为10
cargo = []
price = []
percent = []
i = 0
# 初始化背包设定
while i < 10:
    i += 1
    cargo.append(random.randint(1, 10))
    price.append(random.randint(1, 100))
# 进行分析处理，首先要进行排序
print(cargo)
print(price)
for i in range(10):
    percent.append(price[i] / cargo[i])  # 收益比率
print(percent)
for j in range(1, len(cargo) + 1):  # 进行一个排序
    for i in range(-1, -len(cargo) - 1 + j, -1):
        if cargo[i] < cargo[i - 1]:
            t = cargo[i - 1]
            cargo[i - 1] = cargo[i]
            cargo[i] = t
            t = price[i - 1]
            price[i - 1] = price[i]
            price[i] = t
            t = percent[i - 1]
            percent[i - 1] = percent[i]
            percent[i] = t
print("cargo:" + str(cargo))
print("price" + str(price))
print("percent" + str(percent))
pickup = [[0] * 10] * 10  # 创建二维数组


#  动态规划找最大值情况
#  j为当前背包装下的东西，i为第i个物品
def fmax():
    global pickup
    for i in range(0, 10):
        for j in range(0, bag):
            if j < cargo[i]:  # 装不下，那么总价值不变
                pickup[i][j] = pickup[i - 1][j]
            else:  # 装得下，比较是不是应该装这个东西
                pickup[i][j] = max(pickup[i - 1][j], pickup[i - 1][j - cargo[i]] + price[i])


fmax()
print("-------------------------------")
print("价值最高的背包总价为:" + str(pickup[9][9]))  # 输出最终结果
