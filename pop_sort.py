import random

list = []
for i in range(5):  # 生成需要排序的list序列
    list.append(random.randint(1, 100))
print("需要进行冒泡排序的序列是" + str(list))
n = [0, 0, 0, 0, 0]
m = 0
# 进行冒泡排序，最小的在最前面
for j in range(1, len(list) + 1):  # 总循环次数
    for i in range(-1, -len(list) - 1 + j, -1):  # 考虑到每次循环都会把最小的数字放在最前面，减少范围优化程序
        print("此时，指针位于" + str(list[i]))  # 指针位置
        if list[i] < list[i - 1]:  # 如果指针位置比前一个数字小，那么就进行交换，把更小的数字放到前面
            t = list[i - 1]
            list[i - 1] = list[i]
            list[i] = t
            n[j] += 1
            print("经过第" + str(n[j]) + "次交换后，结果为" + str(list))
    if n[j - 1] == n[j - 2]: # 在一趟遍历中，如果完全没发生交换，那么就说明已经排序完毕，提前跳出
        break
    m += 1
    print("---------------------------------------------")
    print("在经过第" + str(m) + "趟遍历之后，结果为" + str(list))
