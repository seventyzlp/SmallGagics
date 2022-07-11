# 使用回溯法，求解N皇后的解法数量，在之后应该会更新turtle版本
n = int(input("请输入皇后的数量:"))
pos = [0] * (n + 1)  # 数组下标是列，数组值是行,4*4的方格，其中第一行第一列不用


def check(x, y):
    global pos
    flag = True
    x -= 1
    y -= 1

    for i in range(1, len(pos)):
        if pos[i] == y:
            flag = False
            return flag
        pos[x] = y
        for j in range(1, i + 1):  # 检测斜着的情况,上方
            a = x - j
            b = x + j
            # if a <= -1 or b >= len(pos):  # 撞墙了
            #     break
            # if pos[a] + 1 == pos[a + 1] or pos[b] + 1 == pos[b - 1]:  # 相同时
            #     flag = False
            if a <= 0:
                if pos[b] + 1 == pos[b - 1]:
                    flag = False
                    return flag
            elif b >= len(pos):
                if pos[a] + 1 == pos[a + 1]:
                    flag = False
                    return flag
            else:
                if pos[a] + 1 == pos[a + 1] or pos[b] + 1 == pos[b - 1]:  # 相同时
                    flag = False
                    return flag
        for j in range(1, len(pos) - i - 1):  # 下方
            a = x - j
            b = x + j
            # if a <= -1 or b >= len(pos):  # 撞墙了
            #     break
            # if pos[a] - 1 == pos[a + 1] or pos[b] - 1 == pos[b - 1]:
            #     flag = False
            if a <= 0:
                if pos[b] - 1 == pos[b - 1]:
                    flag = False
                    return flag
            elif b >= len(pos):
                if pos[a] - 1 == pos[a + 1]:
                    flag = False
                    return flag
            else:
                if pos[a] - 1 == pos[a + 1] or pos[b] - 1 == pos[b - 1]:
                    flag = False
                    return flag
    return flag


def place(n):
    global pos
    if n >= len(pos):  # 每一个都安置完毕了
        print(pos)
    else:
        for i in range(1, len(pos)):  # 一共要放n个
            if check(n + 1, i + 1):  # 通过检查可以放下
                pos[n] = i
                n += 1
                place(n)


n = 1
place(n)
