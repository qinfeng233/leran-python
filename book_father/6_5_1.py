#coding=utf-8
import random,easygui

guessNumber = random.randint(1,99)

choice = easygui.buttonbox("猜数字游戏，你想玩吗？",choices=['玩','不想玩'])


yourNumber = 0
times = 0
while yourNumber != guessNumber and times < 3 :
    yourNumber = easygui.integerbox("输入你的数字：")
    if not yourNumber: break
    if yourNumber > guessNumber :
        easygui.msgbox(str(yourNumber) + "太大了！")
    elif yourNumber < guessNumber :
        easygui.msgbox(str(yourNumber) + "太小了！")
    times += 1
if yourNumber == guessNumber :
    easygui.msgbox("恭喜你，猜对了！")
else:
    easygui.msgbox("6次机会用完了~要猜的数字是：" + str(guessNumber))

