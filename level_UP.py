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
t.seek(0)
t.write(j)
