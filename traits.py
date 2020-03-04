import random
import math



trait_list = []

def traits():

	list.clear(trait_list)

	roll_1 = [random.randint(1, 6) for x in range(1)]
	first_num = (roll_1)
	trait_list.append(first_num)

	roll_2 = [random.randint(1, 20) for x in range(1)]
	second_num = (roll_2)
	trait_list.append(second_num)

	return(trait_list)



def again():
	calc_again = input("""
Do you want to roll for another trait?
Y / N 
""")

	if calc_again.upper() == "Y":
		traits()

	elif calc_again.upper() == "N":
		print("Good luck, you'll need it!")

	else:
		again()

traits()
again()