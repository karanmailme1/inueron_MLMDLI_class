# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:01:19 2021
@author: 17jan

python program practice 3
"""

#Q1.
#write a program to sort a dictionary by key.
d = {4:'a', 3:'b', 5:'c'}
for key in sorted(d.keys()):
    print("%s:%s" % (key, d[key]))


#Q2.
#Write a Python program to get a dictionary from an object's fields.
class dictObj(object):
    def __init__(self):
        self.x = 'algorithm'
        self.y = 'statistics'
        self.z = 'programming'
        
    def into_dict(self):
        return {'x':self.x, 'y':self.y, 'z':self.z}
    
test = dictObj()
type(test)

test.into_dict()
#or
test.__dict__


#Q3.
# write a program to remove duplicates from Dictionary.
student_data = {'id1':
 {'name': ['Sara'],
 'class': ['V'],
 'subject_integration': ['english, math, science']
 },
'id2':
{'name': ['David'],
 'class': ['V'],
 'subject_integration': ['english, math, science']
 },
'id3':
 {'name': ['Sara'],
 'class': ['V'],
 'subject_integration': ['english, math, science']
 },
'id4':
 {'name': ['Surya'],
 'class': ['V'],
 'subject_integration': ['english, math, science']
 },
}

result = {}

for k,v in student_data.items():
    if v not in result.values():
        result[k] = v

print(result)


#Q4.
# write a program to combine two dictionary adding values for common keys
d1 = {'a': 1000, 'b': 3200, 'c':1300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}

for key in d1.keys():
    #print(key)
    if key in d2:
        d3[key] = d1[key] + d2[key]
    else:
        pass
print(d3)

#or

import itertools as it
{ k:v for k,v in it.chain(d1.items(),d2.items())}


#or

from collections import Counter
d4 = Counter(d1) + Counter(d2)
print(d4)


#Q5.
# write a program to print all unique values from a dictionary in a list
data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, \
        {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

set(v for item_ in data for v in item_.values())


    