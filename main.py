import random

letters_list = ['a','b','c','d','e','f','g']
i = 50
while not i==0:

	n1 = random.randint(0,6)
	n2 = random.randint(0,6)
	n3 = random.randint(0,6)
	n4 = random.randint(0,6)
	n5 = random.randint(0,6)
	n6 = random.randint(0,6)
	n7 = random.randint(0,6)

	key = (letters_list[n1],letters_list[n2],letters_list[n3],letters_list[n4],letters_list[n5],letters_list[n6],letters_list[n7])
	

	print(f'unique_key_string: {key[0]}{key[1]}{key[2]}-{key[3]}{key[4]}{key[5]}-{key[6]}')

	i = i - 1

print('end')
print(type(key))