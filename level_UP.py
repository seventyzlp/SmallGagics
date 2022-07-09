import keyword

t = open("test.py", "r+", encoding='utf-8')
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
    elif txt[j + 1] == '.' or txt[j + 1] == '(':
        i = ''
    elif txt[j].islower():
        i += txt[j]
    j += 1
x = ''
if 'import' in word:
    word.remove(word[word.index('import') + 1])
for x in word:
    if x not in keyword.kwlist:
        y = x.upper()
        data = data.replace(x, y)
print("------------------")
print(data)
t.seek(0)
t.write(data)
