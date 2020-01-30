# #用户身份验证
username = input('请输入用户名：')
password = input('请输入口令：')
#用户名必须是admin且密码得是123456否则验证失败
if username == 'admin' and password == '123456':
    print('您好，欢迎您')
else:
    print('身份验证失败') 
#分段函数求值
#         3x - 5  (x > 1)
# f(x) =  x + 2   (-1 <= x <= 1)
#         5x + 3  (x < -1)
x = float(input('x = '))
if x > 1 :
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f'%(x,y))  
# #英制单位隐村与公制单位厘米的转换
value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%.1f英寸 = %.1f厘米' %(value,value*2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.1f厘米 = %.1f英寸'%(value,value/2.54))
else:
    print('请输入有效单位')
#百分制成绩转化为等级制成绩
score = float(input('请输入成绩：'))
if score >= 90:
    grade = '优秀'
elif score >= 80:
    grade = '良好'
elif score >= 70:
    grade = '一般'
elif score >= 60:
    grade = '合格'
else:
    grade = '不合格'
print('对应的等级是：',grade)
#输入三条边长，如果能构成三角形就计算周长和面积
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长：%d' % (a+b+c))
    p = (a+b+c)/2
    a = (p*(p-a)*(p-b)*(p-c))**0.5
    print('面积：%f'%(a))
else:
    print('不能构成三角形') 