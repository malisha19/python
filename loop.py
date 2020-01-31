# -*- coding: utf-8 -*-
# 用for循环实现1~100求和
sum = 0
for x in range(101):
    sum += x
print(sum)
# #用for循环实现1～100之间的偶数求和
sum = 0
for x in range(2,101,2):
    sum += x
print(sum)
# #用for循环实现1～100之间的偶数求和
sum = 0
for x in range(1,101):
    if x % 2 == 0:
        sum += x
print(sum)
#while 循环
#猜数字游戏：
#计算一个1～100之间的随机数由人来猜
#提示大一点/小一点/猜对了

import random

answer = random.randint(1,100)
guess = 0
while True:
    guess += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else :
        print('恭喜你猜对了')
        break
print('你总共猜对了%d次'% guess)
if guess > 5 :
    print('您的智商很欠费')

输出乘法口诀表
for x in range(1,10):
    for i in range(1,x+1):
        print('%d*%d=%d' % (x, i, i * x) )
    print('\n')
#输入一个正整数判断是不是素数
from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
prime = True
for i in range(2,end+1):
    if num % i == 0:
        prime = False
        break
if prime and num !=1 :
    print('%d是素数' % num)
else :
    print('%d不是素数' % num)
#输入两个正整数，计算他们的最大公约数和最小公倍数
x = int(input('x = '))
y = int(input('y = '))
if x>y:
    x,y = y,x
for factor in range(x,0,-1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % （x,y,factor))      
        print('%d和%d的最大公倍数是%d' % （x,y,x*y // factor))    
        break 
#打印三角形图案
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
