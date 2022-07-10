import keyword

file = input("请输入想要修改的文件路径，若在同一个文件夹下，输入文件名:")
t = open(file, "r+", encoding='utf-8')
txt = t.read()
print("原始文件内容是：")
print(txt.rstrip())
j = 0
i = ''
word = ['']
# 网络上的方法大多就是新建新文件，替换掉旧文件来实现文字替换，这里是选择修改源文件
data = txt
while j < len(txt):
    if txt[j] == "\n" or txt[j].isspace():
        word.append(i)
        i = ''
    elif txt[j + 1] == '.' or txt[j + 1] == '(':  # 限制函数名和库引用的名字不变
        i = ''
    elif txt[j].islower():  # 是大写字母也不用改了
        i += txt[j]
    j += 1
x = ''
if 'import' in word:
    word.remove(word[word.index('import') + 1])
elif 'def' in word:  # 自己定义的函数名字也不变
    word.remove(word[word.index('def') + 1])
for x in word:
    if x not in keyword.kwlist:
        y = x.upper()
        data = data.replace(x, y)
print("------------------")
print(data)
t.seek(0)
t.write(data)
