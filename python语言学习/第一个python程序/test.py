Salary = 10

qq = True

while qq:
    M = int (input(' Enter an integer: '))
    
    if M == Salary:
        print('Congratulations,you guessed it.')
        print('But you can not get it.')
        qq = False

    elif M < Salary:
        print('No,it is a little lower than "Salary". ')

    else:
        print('No,it is a little higher than "Salary". ')

else:
    print('Count Over')

