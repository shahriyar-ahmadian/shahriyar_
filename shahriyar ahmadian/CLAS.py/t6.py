print('1.   +')
print('2.   -')
print('3.   *')
print('4.   /')

op = input( 'please enter operator: ')

if (op ==  '1')  or  (op ==  '+'):
    a=float(input('enter first number :  '))
    b=float(input('enter second number:  '))

    answer= a+b
    print(answer)

elif (op ==  '2')  or  (op ==  '-'):
    a=float(input('enter first number :  '))
    b=float(input('enter second number:  '))

    answer= a-b
    print(answer)
elif (op ==  '3')  or  (op ==  '*'):
    a=float(input('enter first number :  '))
    b=float(input('enter second number:  '))

    answer= a*b
    print(answer)
elif   (op ==  '4')  or  (op ==  '/'):
    a=float(input('enter first number :  '))
    b=float(input('enter second number:  '))

    if b != 0:
        answer= a/b
        print(answer) 

else:
    answer =  ('error')
    print(answer)
