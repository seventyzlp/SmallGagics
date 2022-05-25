#  泛凯撒密码的单纯解密操作
Code = input('请输入密文：')
key = int(input('请输入解密口令（默认请输入3）：'))
STR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str = "abcdefghijklmnopqrstuvwxyz"
ans=''
for i in Code:
    if i in STR:
        ans += STR[STR.find(i)-key]
    elif i in str:
        ans += str[str.find(i)-key]
    else:
        ans += i
print(ans)
