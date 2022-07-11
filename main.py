from random import randint
from time import sleep

def rand():
	number = randint(0,9)
	return number

def random_string_generator():
	letters_list = ['a','b','c','d','e','f','g','h','i','j']
	key_tuple = (letters_list[rand()], letters_list[rand()], letters_list[rand()], letters_list[rand()], letters_list[rand()], letters_list[rand()], letters_list[rand()], letters_list[rand()], letters_list[rand()], letters_list[rand()])
	return key_tuple

def duplicate_checker(starting_index):
	print("Will now check for duplicates")
	sleep(1)
	lines_set = set()	
	for line in open('strings.txt'):
		lines_set.add(line)
	print("Set length: " + str(len(lines_set)))
	if len(lines_set) < starting_index:
		print("Error Duplicates found")
	else:
		print("Good! Found no duplicates!")

def random_string_printer(i):
	starting_index = i
	my_file = open('strings.txt','w+')
	while i != 0:
		key = random_string_generator()
		joined_key_string = "".join([key[0],key[1],key[2],'-',key[3],key[4],key[5],'-',key[6],key[7],key[8],'-',key[9]])		
		print(f'unique_key_string {starting_index - i + 1}: {joined_key_string}')
		my_file.write(joined_key_string + '\n')
		i -= 1
	my_file.close()
	duplicate_checker(starting_index)


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


