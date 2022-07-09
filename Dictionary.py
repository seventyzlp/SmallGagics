dic = open("dictionary.txt", 'r+', encoding='utf-8')
Dictionary = dic.read()
TheDictionary = []

j = -1
# 对文件进行一个读取
for i in range(len(Dictionary)):
    if Dictionary[i].isspace() or Dictionary[i] == "\n":
        TheDictionary.append("")
        j += 1
    elif i == 0:
        TheDictionary.append(Dictionary[i])
        j += 1
    else:
        TheDictionary[j] += Dictionary[i]
print(TheDictionary)


def goto():
    global flag
    key = input("输入b来离开字典,输入其他继续查找:")
    if key == 'b':
        flag = False


# 词典功能操作
flag = True
while flag:
    key = int(input("请输入操作指令(1：查询单词，2：查询中文，3：添加释义，4：添加单词) :"))
    if key == 1:
        word = input("进入查询单词功能，请输入想要查找的单词:")
        try:
            print("这个单词的意思是:" + str(TheDictionary[TheDictionary.index(word) + 1]))
            goto()
        except:
            print("在词典中没有找到这个单词，可以考虑添加哦")
            goto()
    elif key == 2:
        word = input("进入查询中文功能，请输入想要查找的词语:")
        try:
            print("这个词语的英文是:" + str(TheDictionary[TheDictionary.index(word) - 1]))
            goto()
        except:
            print("在词典中没有找到这个词语，可以考虑添加哦")
            goto()
    elif key == 3:
        word = input("进入添加释义功能，请输入想要添加释义的英文单词:")
        try:
            print("这个单词现在的意思是:" + str(TheDictionary[TheDictionary.index(word) + 1]))
            t = TheDictionary.index(word) + 1
            word = input("请输入这个单词的其他意义，若想添加多个含义，请用半角逗号分隔:")
            TheDictionary[t] = TheDictionary[t] + "," + word
            print("添加成功")
            goto()
        except:
            print("在词典中没有找到这个单词，可以考虑添加哦")
            goto()
    elif key == 4:
        word = input("进入添加英文单词功能，请输入想要添加的英文单词:")
        if word in TheDictionary:
            print("这个单词已经被添加到词典库，请换个单词再试试吧")
            goto()
        else:
            TheDictionary.append(word)
            word = input("英文添加完毕，请输入这个单词的释义：")
            TheDictionary.append(word)
            print("添加成功")
            goto()
    else:
        print("输入指令有误，请重新输入")
        goto()

# 保存文件
dic.seek(0)
for i in range(len(TheDictionary)):
    if int(i / 2) == i / 2:
        dic.write(TheDictionary[i] + " ")
    else:
        dic.write(TheDictionary[i] + "\n")
