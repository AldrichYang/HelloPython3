# sorted(list) function, which takes a list and returns a new list with those elements in sorted order.
# The original list is not changed
a = [1, 8, 2, 4]
aAfterSort = sorted(a)
afterReverse = sorted(a, reverse=True)
# print a
print(aAfterSort)
print(afterReverse)


# key=" specifying a "key" function that transforms each element before comparison.
# The key function takes in 1 value and returns 1 value,
#   and the returned "proxy" value is used for the comparisons within the sort
def MyFn(s):
    return s[-1]


strs = ["adde", "bcbfg", "ccccc", "ddddddh"]
print(sorted(strs, key=len, reverse=True))
print(sorted(strs, key=str.lower))
print(sorted(strs, key=MyFn))

# There is also an optional argument "cmp=cmpFn" to sorted()
#   that specifies a traditional two-argument comparison function
#   that takes two values from the list and returns negative/0/positive to indicate their ordering
