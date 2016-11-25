#coding=utf-8
import easygui
money = raw_input("how much your buy :")
if int(money) <= 10:
    print 'your 10%,your pay for :' + str(int(money) * 0.9)
else:
    print 'your 20%,your pay for :' + str(int(money) * 0.8)

student = raw_input("enter your sex ,m or f")
if student == 'm' :
    print '你不符合条件'
else:
    age = raw_input("enter your age :")
    if 10 <= int(age) <= 12:
        print "欢迎加入！"
    else:
        print "你的年龄不符合！"
