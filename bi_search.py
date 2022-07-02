list = [1, 2, 3, 4, 5]
key = int(input("请在列表" + str(list) + "中选择想要查找的对象:"))
n = 0


def search(l, r, key):
    global list
    global n
    n += 1
    print("第" + str(n) + "次查找，中间值是:" + str(list[int((l + r) / 2)]) + "  要找的值是:" + str(key))
    if list[int((l + r) / 2)] == key:  # 如果直接找到了，那么就输出结果，并且终止循环
        print("找到了！就在列表下标" + str(list.index(key)))
    elif l >= r:
        print("找不到！")
    elif key > list[int((l + r) / 2)]:  # 找的小了，继续往大了找
        search(int((l + r) / 2) + 1, r, key)
    elif key < list[int((l + r) / 2)]:
        search(l, int((l + r) / 2) - 1, key)


search(0, 4, key)
