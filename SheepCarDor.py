import random

Door = ['羊1','羊2','车']
n = int(input("输入样本数量:"))
v1 = 0
v2 = 0

for i in range(n):
    random.shuffle(Door)  # 门后内容洗牌
    Choose = random.choice(Door)  # 随机选择一个

    # 不换
    if Choose == '车':
        v1 += 1

    # 进行交换
    if Choose == '羊1' or Choose == '羊2':  # 如果原来选的是车，那么换完一定不是车
        v2 += 1  # 一开始选的是羊，那么在主持人消除掉另外一只羊之后，剩下的一定是车，所以如果交换的话就一定可以选到车

percent1 = v1/n
percent2 = v2/n
print('如果坚持选择，那么获胜的概率为:'+str(percent1))
print('如果交换选择，那么获胜的概率为:'+str(percent2))
