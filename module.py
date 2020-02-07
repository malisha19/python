#实现计算求最大公约数和最小公倍数的函数
def gys(x,y):
    (x,y) = (y,x) if x > y else (y,x)
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor
def gbs(x,y):
    return x*y // gys(x,y)
 
#实现判断一个数是不是回文数的函数
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10 
        temp //= 10
    return total == num
#判断一个数是不是素数
def is_prime(num):
    for factor in range(2,num):
        if num % factor == 0:
            return False
    return True if num != 1 else False
#写一个程序判断输入的正整数是不是回文素数
    if _name_ == '_main_':
        num = int(input('请输入正整数：'))
        if is_palindrome(num) and is_prime(num):
            print('%d是回文素数' % num)
#

     
        

