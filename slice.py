#slicing
pyList = ['P', 'y', 't', 'h', 'o', 'n']
pyTuple = ('P', 'y', 't', 'h', 'o', 'n')

sObject = slice(1, 5, 1)
print(pyTuple[sObject])

#searching lists
vowels = ["a", "e", "i", "o", "u"]
index = vowels.index("e")
print("the index of e is:", index)

#sorting lists
randomlist = [1, 2, 3, 4] #have to be the same everything
randomstrlist = ["cat", "dog", "panda"]
print(randomlist, randomstrlist)
randomlist.sort(reverse = True)
randomstrlist.sort()
print('sorted list (in descending):', randomlist)
print('string sorted list', randomstrlist)

#tuples
tup = ("python", "geeks")
print(tup)
tuple3 = ("python",)*3
print(tuple3)
