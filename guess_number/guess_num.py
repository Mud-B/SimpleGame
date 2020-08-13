from random import randint
import math

# user records
history = {}

def start():
    username = input('请输入用户名: ')
    # check user is registered
    if username not in history.keys():
        history[username] = []
        print(username + ' ,欢迎注册')
    else:
        print(username + ' ,欢迎回来')
    try_max_num = int(input('请设定随机生成数的最大值：'))
    try_to_guess(username, randint(0, try_max_num), try_max_num)

def try_to_guess(name, answer, max_num):
    try_num = 0
    while try_num < math.log2(max_num):
        guess_answer = int(input('请输入一个数字：'))
        if guess_answer < answer:
            print('你输入的数字小了。')
        elif guess_answer == answer:
            print('回答正确。 ')
            history[name].append('成功')
            break
        else:
            print('你输入的数字大了。')
        try_num += 1
    else:
        print('猜错次数过多，失败。 ')
        history[name].append('失败')

def show_history():
    name = input('请输入需要查询的用户名：')
    if history.get(name):
        print('用户：' + name + '，记录如下：[', end='')
        for username, records in history.items():
            for record in records:
                if username == name:
                    print(record + ',', end='')
        print(']')
    else:
        print('用户不存在。')

def default():
    select_dict = {'1': show_history, '2': start, '3': exit}
    while True:
        select = input('1.历史记录\n2.继续游戏\n3.退出游戏\n输入数字选择：')
        select_dict.get(select, default)()

default()
