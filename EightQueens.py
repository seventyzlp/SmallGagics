# 使用回溯法，求解N皇后的解法数量，在之后应该会更新turtle版本
n = int(input("请输入皇后的数量:"))
pos = [0] * n  # 数组下标是列，数组值是行
x = n
j = n


def check(x, y):
    global pos
    flag = True
    for i in pos:
        if i == y:
            flag = False
        for j in range(i + 1):  # 检测斜着的情况
            if pos[x - len(pos) * j - 1] != 0 or pos[x - len(pos) * j + 1] != 0:
                flag = False
        for j in range(len(pos) - i):
            if pos[x + len(pos) * j - 1] != 0 or pos[x + len(pos) * j + 1] != 0:
                flag = False
    return flag


def place(n):
    global pos
    global j
    if j == 0:  # 每一个都安置完毕了
        print(pos)
    else:
        for i in range(x):  # 一共要放n个
            if check(n, i):  # 通过检查可以放下
                pos[n] = i
                place(n - 1)
