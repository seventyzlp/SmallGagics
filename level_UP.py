t = open("test.txt", "r+", encoding='utf-8')
txt = t.read()
print("原始文件内容是：")
print(txt.rstrip())
j = ''
for i in txt:
    if i.islower():
        j += chr(ord(i) - 32)
    else:
        j += i
t.seek(0)  # 网络上的方法大多就是新建新文件，替换掉旧文件来实现文字替换，这里是选择修改源文件
t.write(j)
