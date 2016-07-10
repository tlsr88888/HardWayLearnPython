# -*- coding: utf-8 -*-
'''
def append (max):
        i = 0
        numbers = []

        while i < max:
                print ('At the top i is %d' % i)
                numbers.append(i)

                i = i + 1
                print ('Numbers now: ', numbers)
                print ('At the bottom i is %d' % i)

        print ('The numbers: ')
        for num in numbers:
                print (num)

append(8)
'''

def append (max):
        numbers = [num for num in range(0, max)]
        for i in numbers:
                print (i)

append(8)
