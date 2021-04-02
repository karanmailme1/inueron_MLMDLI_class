# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:26:50 2021
@author: 17jan

python program practice 2
"""

#Q1.
#Write a Python program to check if all dictionaries in a list are empty or not.
my_list1 = [{},{},{}]
my_list2 = [{123,2345},{},{}]

[not d for d in my_list1]
print(all(not d for d in my_list1))
print(all(not d for d in my_list2))
        

#Q2.
#Write a Python program to remove duplicates from a list of lists.
import itertools as it

num = [[110, 120], [240], [330, 456, 425], [310, 220], [133], [240]]
num.sort() #sorts in place
num

[i for i,_ in it.groupby(num)] #does not work without sort, why?


#Q3.
#Write a Python program to extend a list without append.
x = [34,24,33,43]
y = [1,2,3,4]
for i in y:
    x = x + [i]
x


#Q4.
#Write a Python program to find the list in a list of lists whose sum of 
#elements is the highest
num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
num[max((sum(j),i) for i,j in enumerate(num))[1]]
#max((i,j) for i,j in enumerate(num))

#or

print(max(num, key=sum))


#Q4.
#Write a Python program to access dictionary key’s element by index.
d = {'a':10, 'b':20, 'c':30}
list(d)
d[list(d)[0]]


#Q5.
#Write a Python program to iterate over two lists simultaneously.
x = [34,24,33,43]
y = [1,2,3,4]

for (i,j) in zip(x,y):
    print(i,j)


#Q6.
#write a program to insert a string at the begining of every elements in a list
lst = [5,6,7,8]
#enter customer before each element
print(['customer{0}'.format(i) for i in lst])


#Q7.
# write a program to take two lists and print if they have at least one common member
x = [34,24,33,43,4]
y = [1,2,3,4]

any([(i in x) for i in y])

#or

def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result
print(common_data([121,222,332,432,125], [125,236,457,678,779]))
print(common_data([1,2,3,4,5], [6,7,8,9]))


#Q7.
# compute all permutations in a list
import itertools as it

x = [34,24,3]
list(it.permutations(x))


