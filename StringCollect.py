# 字符串遍历统计
# 初始化相关变量
Str = input('请输入要统计的字符串：')
str_ = 'abcdefghijklmnopqrstuvwxyz'
a = 0
A = 0
blank = 0
other = 0
ch = 0
num = 0

for i in Str:
    if i in str_:  # 字符串法小写字母统计
        a += 1
    elif i.isupper():  # 使用内置函数进行大写字母统计
        A += 1
    elif i.isspace():  # 内置函数空格统计
        blank += 1
    elif '\u4e00' <= i <= '\u9fff':  # unicode范围中文字符统计
        ch += 1
    elif '0' <= i <= '9':  # 字符串大小比较数字统计
        num += 1
    else:
        other += 1
print("字符串中，小写字母出现的次数为{}次,大写字母出现的次数为{}次,空格出现的次数为{}次,汉字出现的次数为{}次,数字出现的次数为{}次,其他字符串出现的次数为{}次" \
      .format(str(a), str(A), str(blank), str(ch), str(num), str(other)))
