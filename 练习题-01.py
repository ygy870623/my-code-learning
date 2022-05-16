"""

count = 0
while True:
    print('11111')
    count += 1
    if count == 5:
        break
###
"""

#第一个练习

times = 0
for i in range(3):
    username = input('请输入您的账号：')
    password = input('请输入您的密码：')

    if username == 'admin' and password == '1234':
        print('密码输入成功！进入界面！')
        break
    print('不好意思！您输入的账号和密码不正确！\n')
    times += 1

    if times == 3:
        print('不好意思！已经超过了三次机会！您的账号已被封锁！')

#第二个练习

total = 0
number = 0

while True:
    price = float(input("请输入价格"))
    number = int(input("请输入数量："))

    total += price * number

    numbers += number

    answer = input("当前商品总额：%.2f，是否继续添加商品？（按q退出）" % total)

    if answer == 'q':
        break

print("所有商品的总额是：%.2f" % total)

#第三个练习

import random

ran = random.randint(1, 50)
count = 0

while  True:
    guess = input('猜一个1-50之间的数字：')
    if int(guess+1 == False):
        print('nono')

    count += 1

    if guess == ran:
        if count == 1:
            print("666")
        elif 2<=count<=5:
            print("可以可以")
        elif count>= 6:
            print('你的运气一般哎')

        print('恭喜猜对啦！')
        break
    elif guess > ran:
        print('猜大了！再小一点！')
    else:
        print('猜小了，再大一点！')
      

#第四个练习

n = 1

while n <= 10:
    print('n')
    n += 1
    if n == 6:
        break
