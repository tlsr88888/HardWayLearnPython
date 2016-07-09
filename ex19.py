# -*- coding: utf-8 -*-
'''
def cheese_and_crackers(cheese_count, boxes_of_crackers):
        print ('You have %d cheeses!' % cheese_count)
        print ('You have %d boxes of crackers!' % boxes_of_crackers)
        print ('Man that\'s enough for a party!')
        print ('Get a blanket.\n')

print ('We can just give the function numbers directly:')
cheese_and_crackers(20, 30)

print ('OR, we can use variables from our script:')
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print ('We can even do math insede too:')
cheese_and_crackers(10 + 20, 5 + 6)

print ('And we can combine the two, variables and math:')
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
'''
dic = {}
def get_personal_message ():
        name = input('Please enter your name:')
        message = ['age', 'height', 'weight']
        dic[name] = []
        for i in message:
                dic[name].append(input('Please enter your %s:' % i))        

for i in range(3):
        get_personal_message()
for i in dic:
        print ('name: %s \t age: %s \t height: %s \t weight: %s' % (i, dic[i][0], dic[i][1], dic[i][2]))