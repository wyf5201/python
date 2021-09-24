a = 0
sum = 0

while a < 101:
    if a % 2:  # if a%2:奇数         if not bool(a % 2)：偶数 if a%2==0：
        sum += a
    a += 1

print('1-100的偶数和：', sum)
