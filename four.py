#输入圆的半径计算周长和面积
import math
r = float(input('请输入圆的半径：'))
p = 2 * math.pi * r
a = math.pi * r * r
print('周长：%.1f' % p)
print('面积：%.1f' % a)

#判断年份是不是闰年
year = int(input('请输入年份:'))
leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(leap)