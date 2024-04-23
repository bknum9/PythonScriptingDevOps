#!/usr/bin/python3.6
from player_actions import *
# firstname = 'brian'
# lastname = 'k'
# print(firstname.title() + '' + lastname.title())

# fruits = ['apple', 'banana', 'mango', 'pear']
# print(fruits[-1])
# fruits[1] = 'pineapple'
# print(fruits)
# fruits.append('grapes')
# print(fruits)
# fruits.insert(1, 'kiwi')
# print(fruits)
# #removedItem = fruits.pop(1)
# #print(removedItem)
# print(fruits)
# removedItem = fruits.remove('mango')
# print(removedItem)
# print(fruits)

# users = ['james', 'alex', 'peter', 'victor', 'david']
# users.sort()
# print(users)
# for i in users[2:]:
#     print('current user is ',i)
# new_list = [item + ' is the best' for item in users if len(item) > 4]
# print(new_list)

# if len(users) > 5 and 'alex' in users:
#     print('true')
# else:
#     print('false')

# player = {
#     'name': 'Messi',
#     'age' : 30,
#     'team': 'Barcelona',
#     'position': 'forward'
# }
# print(player['age'])
# for key,value in player.items():
#     print(key,value)

# def multiply(a = 2,b = 3):
#     result = a*b
#     return result

# retunred_value = multiply(10,3)
# print(retunred_value)

# def printName(firstName, lastName):
#     return firstName + ' ' + lastName

# print(printName('messi', 'leo'))

# def print_list(*args):
#     for i in args:
#         print(i)
# print_list(1,2,3,4,5, 'brian')

players = [
    {'name': 'messi', 'club': 'barcelona'},
    {'name': 'maradona', 'club': 'napoli'},
    {'name': 'pele', 'club': 'santos'}
]

print(findPlayer('suarez', players))



