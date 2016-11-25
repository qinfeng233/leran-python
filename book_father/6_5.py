#coding=utf-8
import random,easygui
secret = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox('''AHOY !    I have a secret!
It is a number from 1 to 99, I'll give you 6 tries''')
while guess != secret and tries < 6 :
    guess = easygui.integerbox("What you guess?")
    if not guess : break
    if guess < secret :
        easygui.msgbox(str(guess) + "太小")
    elif guess > secret :
        easygui.msgbox(str(guess) + "太大")
    tries += 1
if guess == secret :
    easygui.msgbox("You Win")
else:
    easygui.msgbox("no more times,you lose! The number is " + str(secret))