# -*- coding: utf-8 -*-

from sys import argv

script, user_name, smart = argv
prompt = '** '

print ('Hi %s, I\'m the %s script.' % (smart + ' ' + user_name, script))
print ('I\'d like to ask you a few questiongs.')
print ('Do you like me %s?' % smart + ' ' + user_name)
likes = input (prompt)
print ('Where do you live %s' % smart + ' ' + user_name)
lives = input (prompt)

print ('What kind of computer do you have?')
computer = input (prompt)

print ('''
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
''' % (likes, lives, computer))