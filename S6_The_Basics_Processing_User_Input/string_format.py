user_input = input('Enter your name: ')
message = 'Hello %s from first string format!' % user_input
message2 = f'Hello {user_input} from second string format!'
print(message)
print(message2)