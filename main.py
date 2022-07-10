from random import randint
from time import sleep

def rand():
	number = randint(0,6)
	return number

def random_string_generator():

	letters_list = ['a','b','c','d','e','f','g']

	key_tuple = (letters_list[rand()], letters_list[rand()], letters_list[rand()], letters_list[rand()], letters_list[rand()], letters_list[rand()], letters_list[rand()])
	return key_tuple


def random_string_printer(i):
	while i != 0:
		key = random_string_generator()
		print(f'unique_key_string: {key[0]}{key[1]}{key[2]}-{key[3]}{key[4]}{key[5]}-{key[6]}')
		i = i-1


def input_trigger():
	print()
	print ('Enter how many strings do you want?')
	print()
	sleep(0.5)
	string_number = int(input('Enter an Integer: '))
	print()	
	sleep(0.5)
	print ('You entered ' + str(string_number))
	print()
	sleep(0.5)
	print ('Printing ' + str(string_number) + ' random strings get ready:')
	sleep(0.5)
	print()
	random_string_printer(string_number)


input_trigger()

print()
print()
print('end of code')


