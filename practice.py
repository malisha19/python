#生成斐波那契数列的前20个数
a = 0
b = 1
for _ in range(20):
    a, b = b, a+b
    print(a,end=' ')
# 求2~99之间的所有素数
import math

for num in range(2,100):
    is_prime = True
    for factor in range(2,int(math.sqrt(num))+1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num,end=' ')
#求找出1~9999之间的所有完美数
#完美数是除自身外其他所有因子的和正好等于这个数本身的数
import math 
for num in range(1,10000):
    result = 0
    for factor in range(1,int(math.sqrt(num))+1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)