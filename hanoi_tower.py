#  采用维基百科的图围解法,但是循环方向与维基百科的版本做了一定的区分,采用递归的方式求解

n = int(input("请输入盘片的数量："))
m = n
count = 0


def hanoi(n, a, b, c):
    global count
    global m
    if n == 1:
        count = count + 1
        print(str(count) + ':' + a, '-->', c)  # 最小的那片一直向C移动
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)


hanoi(n, 'A', 'B', 'C')
