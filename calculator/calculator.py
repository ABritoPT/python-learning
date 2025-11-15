def simpleMult():
    print('Enter the first number:')
    num1 = gatherIntInput()
        
    print('Enter the second number:')
    num2 = gatherIntInput()

    multiply([num1, num2])
    return

def complexMult():
    print('Enter one interger per line, minimum two. When you\'re done, press Enter one more time.')

    numbers = []
    while True:
        num_input = gatherIntInput(True)
        if num_input == '':
            break
        else:
            numbers.append(num_input)

    if len(numbers) < 2:
        print('Fewer than two numbers provided. Can\' multiply.')
        return
    
    multiply(numbers)
    return

def gatherIntInput(allowEmpty=False, allowRetries=True):
    while True:
        num_input = input()
        if num_input.isnumeric():
            return int(num_input)
        elif num_input == '' and allowEmpty:
            return ''
        elif allowRetries == False:
            return None
        else:
            print('That\'s not a number. Try again:')
            continue

    return None

def multiply(numbers):
    res = 1
    for num in numbers:
        res *= num

    mult_str = 'x'.join(map(str,numbers))
    print('Result of ' + mult_str + ' is ' + str(res))
    return

# Intro
print('--Multiplication--')
print('Choose a module:')
print('1. Simple multiplication (multiplies two integers)')
print('2. Complex multiplication (multiplies multiple integers together)')

option = input()
if option == '1':
    simpleMult()
elif option == '2':
    complexMult()
else:
    print('Invalid option')
