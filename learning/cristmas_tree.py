# This program print cristmas tree view max range between 3 to 100 for input

input = int(input("Enter a number: ")) 

def print_tree():
    print('Marry Christmas')
    spaces = input
    start = 1
    end = input + 1
    while  start != end:    
        print( " " * spaces + " *" * start)
        start += 1
        spaces -= 1

# Input validation
if input >=3 and input <= 100:
    print_tree()
else:
    print('Invalid Input. Exiting...')

