#  采用维基百科的图围解法,但是循环方向与维基百科的版本做了一定的区分,采用递归的方式求解
#  为了实现turtle的效果，打算使用函数的方法来绘制图像
import turtle
import time
import playsound

n = int(input("请输入盘片的数量："))
A = [i for i in range(n, 0, -1)]  # A柱，其中数字越大表示的盘片越大
A.insert(0, "A")
B = ["B"]
C = ["C"]
count = 0
wide = int(400 / (2 * n))
color = int(200 / n)
m = n
turtle.pensize(wide)
turtle.setup(600, 400, 0, 0)
turtle.colormode(255)
turtle.title('汉诺塔')
turtle.bgpic('bg.gif')
# 使用turtle.bgpic设置背景图像

# 图像初始化
for i in A:
    if i != "A":
        turtle.penup()
        turtle.goto(50 - 300, wide * 0.5 + wide * (len(A) - 1 - i) - 200)  # 设置A柱初始画面
        c = color * i
        turtle.color(c, c, c)
        turtle.pd()
        turtle.forward(100)
        turtle.penup()
playsound.playsound("进入游戏.mp3")  # 搞一个语音提示优化下体验,white进入游戏


def hanoi(n, a, b, c, A, B, C):
    global count
    if n == 1:
        count = count + 1
        print(str(count) + ':' + a, '-->', c)  # 最小的那片一直向C移动
        draw(A, C, A[-1])
        C.append(A[-1])
        A.pop()
        print(str(A))
        print(str(B))
        print(str(C))
    else:
        hanoi(n - 1, a, c, b, A, C, B)  # 把最上面的东西拿到B处
        hanoi(1, a, b, c, A, B, C)  # 动完上面一堆之后要把最下面那个拿过去
        hanoi(n - 1, b, a, c, B, A, C)  # 再把之前拿到B处的定西拿回C的上面


def draw(a, c, n):
    # n为盘子序号
    global wide
    global color
    global m
    turtle.penup()
    turtle.goto(50 + 200 * (ord(a[0]) - ord('A')) - 300, wide * 0.5 + wide * (m - a[-1]) - 200)  # 设置画图的位置
    turtle.down()
    turtle.color("white")  # 先擦除被拿掉的盘子
    turtle.forward(100)
    turtle.penup()

    turtle.goto(50 + 200 * (ord(c[0]) - ord('A')) - 300, wide * 0.5 + wide * (m - a[-1]) - 200)  # 在C画新的盘子
    turtle.down()
    c = color * n
    turtle.color(c, c, c)  # 画上新的
    playsound.playsound('click.wav')  # 提示音
    turtle.forward(100)
    turtle.penup()


hanoi(n, 'A', 'B', 'C', A, B, C)
turtle.done()
