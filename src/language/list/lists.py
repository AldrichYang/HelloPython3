list1 = ['red', 'blue', 'green']
list2 = list1
print(list1 == list2)

list3 = ['black', 'white']
print(list1 + list2)

squares = [1, 2, 4, 6, 9]
sumNum = 0
for num in squares:
    sumNum += num
print(sumNum)

if 1 in squares:
    print('yes')
else:
    print('no')

for num in range(8, 8):
    print(num)

# list = ['larry', 'curly', 'moe']
list = []
list.append('larry')
list.append('curly')
list.append('moe')
list.append('shemp')
list.insert(0, 'xxx')
list.extend(['yyy', 'zzz'])
print(list)
print(list.index('curly'))
list.remove('curly')
print(list.pop(1))
print(list)

list4 = ['a', 'b', 'c', 'd']
print(list4[1:-1])
list4[0:2] = 'z'
print(list4)
