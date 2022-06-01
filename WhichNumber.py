import random


def Check_1(asr):
    while True:  # 通过使用异常状态处理来判定字符
        try:
            asr_int = int(asr)
            break
        except:
            asr = input("数据类型错误，请在输入一遍捏：")
    return int(asr)


def Check_2(asr):
    i = ''
    flag = True
    while flag:  # 使用遍历字符串的形式来判定字符，但是效率不高
        for i in asr:
            if not (i in '1234567890'):
                break
        if i == asr[-1]:
            break
        else:
            asr = input("数据类型错误，请在输入一遍捏：")
    return int(asr)


key = random.randint(0, 100)
answer = input("猜猜这个数是什么捏：")
answer_int = Check_2(answer)

n = 1
while True:
    if answer_int == key:
        print("这个数是" + str(key))
        print("你小子猜了" + str(n) + "次就猜中了，真厉害啊")
        break
    elif answer_int > key:
        print("真遗憾，猜大了，再试试吧！")
        n += 1
    elif answer_int < key:
        print("真遗憾，猜小了，再试试吧！")
        n += 1
    answer = input("这个数是？：")
    answer_int = Check_1(answer)  # 考虑到每次输入之后都要验证字符的正确性
