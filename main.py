from random import randint
from time import sleep

def random_string_generator():

	letters_list = ['a','b','c','d','e','f','g']

	n1 = randint(0,6)
	n2 = randint(0,6)
	n3 = randint(0,6)
	n4 = randint(0,6)
	n5 = randint(0,6)
	n6 = randint(0,6)
	n7 = randint(0,6)

	key_tuple = (letters_list[n1],letters_list[n2],letters_list[n3],letters_list[n4],letters_list[n5],letters_list[n6],letters_list[n7])
	return key_tuple

	print(f'unique_key_string: {key[0]}{key[1]}{key[2]}-{key[3]}{key[4]}{key[5]}-{key[6]}')


def random_string_printer(i):
	while i != 0:
		key = random_string_generator()

		print(f'unique_key_string: {key[0]}{key[1]}{key[2]}-{key[3]}{key[4]}{key[5]}-{key[6]}')

		i = i-1
		sleep(0.5) #for waisting time for no reason


def input_trigger():
	print()
	print ('Enter how many strings do you want?')
	print()
	sleep(1)
	string_number = int(input('Enter an Integer: '))
	print()	
	sleep(1)
	print ('You entered ' + str(string_number))
	print()
	sleep(1)
	print ('Printing ' + str(string_number) + ' random strings get ready:')
	sleep(1)
	print()
	random_string_printer(string_number)


input_trigger()

print()
print()
print('end of code')


