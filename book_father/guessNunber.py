from random import randint
guessNum = randint(1,99)
num = 0
tries = 0
print 'i have gussNum'
print 'It is a number from 1 to 99,I\'ll give you 6 tries.'
print guessNum
while num != guessNum and tries < 6 :
    num = raw_input('enter you number:')
    if num < guessNum :
        print 'too Small'
    elif num > guessNum :
        print 'too Big'
    tries += 1
if num == guessNum :
    print 'YOU WIN !'
else:
    print 'You lose'