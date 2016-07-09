# -*- cooding: utf-8 -*-

from sys import argv # 模块引入

script, filename = argv # 定义参数变量

txt = open(filename) # 读取文件并将文件名赋予给变量txt

print ('Here\'s your file %r:' % filename) # 打印文件名
print (txt.read()) # 打印文件内容
txt.close()

print ('Type the filename again:') # 再输入一遍文件名字
file_again = input ('> ') 

txt_again = open(file_again) # 打开将文件名字赋予变量txt_again
print (txt_again.read()) # 读取文件内容并打印
txt_again.close()