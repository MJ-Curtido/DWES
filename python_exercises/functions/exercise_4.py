import random

#help(random.randint)
#help(random.choice)

dict_cont = {i: 0 for i in range(1, 7)}

for e in range(1, 101):
	random_number = random.randint(1, 6)

	dict_cont[random_number] += 1

print(f'6 appeared: {dict_cont[6]}')
