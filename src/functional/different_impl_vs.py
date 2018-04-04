# 需求：3辆车比赛，每辆车有70%的概率可以往前走一步，一共有5次机会，然后打印每一次这3辆车的前行状态

from random import random


# 指令式实现
# time = 5
# car_positions = [1, 1, 1]
# while time:
#     '''decrease time'''
#     time -= 1
#     print('')
#     for i in range(len(car_positions)):
#         '''move car'''
#         if random() > 0.3:
#             car_positions[i] += 1
#         '''draw car'''
#         print('', car_positions[i])
#
# print('------------')


# 向函数模块的演进实现
# def move_cars():
#     for j, _ in enumerate(car_positions):
#         if random() > 0.3:
#             car_positions[j] += 1
#
#
# def draw_car(car_position):
#     print('-' * car_position)
#
#
# def run_step_of_race():
#     global time
#     time -= 1
#     move_cars()
#
#
# def draw():
#     print('')
#     for car_position in car_positions:
#         draw_car(car_position)
#
#
# time = 5
# car_positions = [1, 1, 1]
# while time:
#     run_step_of_race()
#     draw()

# 代码逻辑封装成了自解释的函数，但是依赖共享的变量来同步状态。
# 每次进入函数必须推演当前变量值才能知道真正程序逻辑，也就是说函数间必须知道其他函数是怎么修改他们之间的共享变量的，所以这些函数是有状态的


# 函数式实现
def move_cars(car_positions):
    return map(lambda x: x + 1 if random() > 0.3 else x, car_positions)


def output_car(car_position):
    return '-' * car_position


def run_step_of_race(state):
    return {'time': state['time'] - 1, 'car_positions': move_cars(state['car_positions'])}


def draw(state):
    print('')
    print('\n'.join(map(output_car, state['car_positions'])))


def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))


race({'time': 5, 'car_positions': [1, 1, 1]})

# 这些函数都是函数式的：1 它们之间没有共享变量 2 函数之间通过参数和返回值来传递数据 3 在函数里没有临时变量 4 for循环被递归取代了
# 递归是函数式编程常用的技术，递归本质是描述问题是什么
