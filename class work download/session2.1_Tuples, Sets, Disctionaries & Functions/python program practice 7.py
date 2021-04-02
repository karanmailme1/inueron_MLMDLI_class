# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:17:12 2021
@author: 17jan

python program practice 7
"""

#Q1.
#create a tuple from multiple data types
t1 = ('k',17,True,0.99,[1,2,3])
type(t1)
print(t1)


#Q2.
#Create a list of length 3 and Create a list of length 4, For each element in the first list,
#Display the corresponding index element of the second list
l1 = [1,2,3]
l2 = ['a','b','c','d']

for i,j in enumerate(l1):
    print(j, '--->', l2[i])
    
#or

for i,j in zip(l1,l2):
    print(i, '--->', j)


#Q3.
# display an example of Nested For Loops Using List Comprehension
[(i,j) for i in l1 for j in l2]


#Q4.
#write a program for breaking and exiting out of loop
# Create a list:
armies = ['Red Army', 'Blue Army', 'Green Army']

for i in armies:
    if i == 'Blue Army':
        break
    else:
        print(i)


#A loop will exit when completed, but using an else statement we can add an action 
#at the conclusion of the loop if it hasn’t been exited earlier.
#for else loop
for army in armies:
    print(army)
    if army == 'Orange Army':
        break
else:
    print('Looped Through The Whole List, No Orange Army Found')



