# This is a sample of a simple menu
def menu():
    print('[1] Option 1')
    print('[2] Option 2')
    print('[0] Exit')

menu()
option = int(input("Enter option:  ")

while option != 0:
    if option == 1:
        #do option 1 thing
        print('Option 1 has been called.')
    elif option == 2:
        #do option 2 thing
        print('Option 2 has been called.')
    else:
        print('Not an option.')

        print()
        menu()
        option = int(input('Enter your option:  '))
print('Thank you. Goodbye.')

# I can't figure out why line 16 brings up 'invalid syntax'?
