#  泛凯撒密码的单纯解密操作
Code = input('请输入密文：')
key = int(input('请输入解密口令（默认请输入3）：'))
STR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str = "abcdefghijklmnopqrstuvwxyz"
asc_A = ord('A')
asc_a = ord('a')
ans=''
for i in Code:
    if i in STR:  # 大写
        ans += STR[STR.find(i)-key]
    elif i in str:  # 小写
        ans += str[str.find(i)-key]
    else:
        ans += i
print(ans) # 输出字符串取位循环结果
ans = ''
for i in Code:
    if i in STR:  # 大写字符
        ans += chr((ord(i) - asc_A - key) % 26 + asc_A)  # 这个地方要先减掉基准值，才能在26个字母内循环
    elif i in str:
        ans += chr((ord(i) - asc_a - key) % 26 + asc_a)
    else:
        ans += i
print(ans)  # 输出约瑟夫环运算结果
