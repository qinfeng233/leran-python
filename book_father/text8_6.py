number = raw_input("enter your number : ")
for i in range(1,11) :
    print str(number) + 'X' +str(i)  + '=' + str(int(number) * i)

while number :
    print number * range(1,11)