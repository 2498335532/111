# 0~100的和
a = 0
b = 0
while a <= 100:
    b = b + a
    a = a + 1
print("0~100的和为:%s" % b)

# 0~100中奇数的和
a = 0
b = 0
while a <= 100:
    if a % 2 == 0:
        b = b + 0
    else:
        b = b + a
    a = a + 1
print("0~100中奇数的和为:%s" % b)

# 0~100中偶数的和
a = 0
b = 0
while a <= 100:
    b = b + a
    a = a + 2
print("0~100中偶数的和为:%s" % b)



