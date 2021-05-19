#decode



shift = int(input('enter the shift:'))

print('note:give a space after each letter')

data= input('enter the data:')



for i in data:

    if i==' ':

        print('', end='')

    else:

        if i.isupper():

            if (ord(i)-shift) > 64:

                print(chr(ord(i)-shift), end='')

            elif (ord(i)-shift) <= 64:

                print(chr(ord(i)-shift+26), end='')

        elif i.islower():

            if (ord(i)-shift) > 96:

                print(chr(ord(i)-shift), end='')

            elif (ord(i)-shift) <= 96:

                print(chr(ord(i)-shift+26), end='')
