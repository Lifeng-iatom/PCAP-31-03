#!/usr/bin/env python3.11
from functools import reduce

domain = [1,2,3,4,5]
# function x+1
ourrange = map(lambda num:num*2,domain)
print(list(ourrange))

evens = filter(lambda num: num % 2 ==0,domain)
print(list(evens))

the_sum = reduce(lambda acc,num:acc + num,domain,0)
print(the_sum)

words = ['Boss','a','Alf','fig','Daemon','gid']
print(sorted(words))
print(sorted(words,key=lambda s: s.lower()))

words.sort(key=str.lower,reverse=False)
print(words)