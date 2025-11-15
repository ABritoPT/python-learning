from generator import PasswordGenerator

print('-- Password Generator by ADB --')

print('Enter the length of the password (at least 4):')
pass_len = 0
while True:
    len_input = input()
    if len_input.isnumeric():
        pass_len = int(len_input)
        if pass_len >= 4:
            break
    print('Invalid input. Try again:')

print('Include upper case letters? [y/N]')
opt_uppercase = input().lower() == 'y'

print('Include numbers? [y/N]')
opt_numbers = input().lower() == 'y'

print('Include special characters? [y/N]')
opt_special_chars = input().lower() == 'y'

pg = PasswordGenerator(pass_len, opt_uppercase, opt_numbers, opt_special_chars)
password = pg.generate()

print('Password: ' + password)