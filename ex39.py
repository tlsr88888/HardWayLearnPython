# -*- coding: utf-8 -*-
class Song(object):

        def __init__(self, lyrics):
                self.lyrics = lyrics

        def sing_me_a_song(self):
                for line in self.lyrics:
                        print (line)
h_lyc = ['Happy birthday to you',
        'I don\'t want to get sued',
        'So i\'ll stop right there']

Song(h_lyc).sing_me_a_song()
'''
happy_bday = Song(h_lyc)

b_lyc = ['They rally around the family',
        'With pockets full of shells']
bulls_on_parade = Song(b_lyc)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
'''