# input()
# input()

# print('password {password} is {passwordlength} long')

# input('jayjay')
# input('secret')

# print('{username}, your password {******} is {6} letters long')

# print('*' * 10)

username = input('what is your username?')

password = input('what is your password?')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, your password, {password_length}, is {hidden_password} letters long')

# not working as this all one line there isn't <br>
# print(f'{username}, your
# password, {password}, is {len
#(password)} letters long')


