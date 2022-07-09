import keyword

t = open("test.py", "r+", encoding='utf-8')
txt = t.read()
print("原始文件内容是：")
print(txt.rstrip())
data = ''
j = ''
i = ''
word = ['']
# 网络上的方法大多就是新建新文件，替换掉旧文件来实现文字替换，这里是选择修改源文件
data = txt
for j in range(len(txt)):
    if txt[j].islower():
        i += txt[j]
    elif word[-1] != 'import':
        word.append(i)
        i = ''
    else:
        i = ''
        word.append(i)
x = ''
for x in word:
    if x not in keyword.kwlist:
        y = x.upper()
        data = data.replace(x, y)
print("------------------")
print(data)
# t.write(data)
