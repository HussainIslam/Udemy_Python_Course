user_input = input('Enter your name: ')
message = 'Hello %s from first string format!' % user_input
message2 = f'Hello {user_input} from second string format!'
message3 = 'Hello {} from third string format!'.format(user_input)
print(message)
print(message2)
print(message3)