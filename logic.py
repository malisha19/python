#寻找水仙花数
for i in range(100,1000):
    low = i % 10
    mid = i // 10 % 10
    thr = i // 100
    if i == low ** 3 + mid ** 3 + thr ** 3:
        print(i)
#数字反转：12345-54321
num = int(input('num = '))
r = 0 #78
while num > 0:
    r = r * 10 + num % 10
    num //= 10
    print(r)
#公鸡5块钱1只，母鸡3块钱1只，小鸡1块钱3只，100块钱买100只鸡，公鸡母鸡小鸡各多少只
for x in range(0,20):
    for y in range(0,33):
        z = 100 - x - y
        if x * 5 + 3 * y + z / 3 == 100:
            print('公鸡:%d,母鸡:%d,小鸡：%d' % (x,y,z))
#简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
#Craps赌博游戏
# 我们设定玩家开始游戏时有1000元的赌注
# 游戏结束的条件是玩家输光所有的赌注
from random import randint
money = 1000

while money > 0:
    print('您的总资产：', money)
    need = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    first = randint(1,6) + randint(1,6)
    print('玩家摇出了：%d' % first)
    if first == 7 or first == 11:
        print('玩家胜')
        money += debt
    elif first == 2 or first == 3 or first == 12 :
        print('庄家胜')
        money -= debt
    else:
        need = True
    while need:
        need = False
        current = randint(1,6) + randint(1,6)
        print('玩家摇出了：%d' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        if current == first:
            print('玩家胜')
            money += debt
        else:
            need = True
print('你破产了')