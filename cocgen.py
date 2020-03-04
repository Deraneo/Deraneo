
import random
import math

def rolling():

	stat_list = []

	while len(stat_list) < 5:
		roll_4d6 = [random.randint(1, 6) for x in range(0, 4)]
		roll_4d6.sort()
		roll_num_4d6 = sum(roll_4d6[1:])
		stat_list.append(roll_num_4d6)

	while len(stat_list) < 7:
		roll_3d6 = [random.randint(1, 6) for x in range(0, 3)]
		roll_3d6.sort()
		roll_num_3d6 = sum(roll_3d6[1:])
		stat_list.append(roll_num_3d6+6)

	while len(stat_list) < 8:
		roll_4d6_3 = [random.randint(1, 6) for x in range(0, 4)]
		roll_4d6_3.sort()
		roll_num_4d6_3 = sum(roll_4d6_3[1:])
		stat_list.append(roll_num_4d6_3+3)

	print("The list: ",stat_list)
	return stat_list

stats = rolling()

# List numbers for stats:
# 0 - Strength | 1 - Constitution | 2 - Power | 3 - Dexterity | 4 - Appearance | 5 - Size | 6 - Intelligence | 7 - Education

def derived_stats(stats):
	print("""
Here are the ability scores for your character: """)
	print("Strength: ",stats[0])
	print("Constitution: ",stats[1])
	print("Power: ",stats[2])
	print("Dexterity: ",stats[3])
	print("Appearance: ",stats[4])
	print("Size: ",stats[5])
	print("Intelligence: ",stats[6])
	print("Education: ",stats[7])

	#All derived stats from here
	stat_sanity = (stats[2] * 5)
	stat_idea = (stats[6] * 5)
	stat_luck = (stats[2] * 5)
	stat_know = (stats[7] * 5)
	stat_hp = ((stats[0] + stats[1]) / 2)
	occ_skill = (stats[7] * 20)
	hob_skill = (stats[6] * 10)
	dodge_skill = (stats[3] * 2)

	#Printing all derived stats
	print("""
Here are the stats derived from your ability scores: """)
	print("Sanity: ",stat_sanity)
	print("Idea: ",stat_idea)
	print("Luck: ",stat_luck)
	print("Knowledge: ",stat_know)
	print("Hit Points: ",math.ceil(stat_hp))
	print("Magic Points: ",stats[2])
	print(" ")

	#Printing all skill points
	print("Here are your skill points:")
	print("Occupational: ",occ_skill)
	print("Hobby: ",hob_skill)
	print("Dodge: ",dodge_skill)

def dmg_bonus(stats):
	print(""" 
Calculating melee damage bonus: """)
	dmg_bonus_stat = (stats[0] + stats[5])
	print("Strength + Size = ",dmg_bonus_stat)
	if dmg_bonus_stat >= 2 and dmg_bonus_stat <= 12:
		print("Your total is within the 2 to 12 range")
		print("Your damage bonus is: -1D6")
	elif dmg_bonus_stat >= 13 and dmg_bonus_stat <=16:
		print("Your total is within the 13 to 16 range")
		print("Your damage bonus is: -1D4")
	elif dmg_bonus_stat >= 17 and dmg_bonus_stat <= 24:
		print("Your total is within the 17 to 24 range")
		print("Your damage bonus is: 0")
	elif dmg_bonus_stat >= 25 and dmg_bonus_stat <= 32:
		print("Your total is within the 25 to 32 range")
		print("Your damage bonus is: +1D4")
	elif dmg_bonus_stat >= 33 and dmg_bonus_stat <= 40:
		print("Your total is within the 33 to 40 range")
		print("Your damage bonus is: +1D6")
	else:
		print("Your total is above 40")
		print("Your damage bonus is: +2D6")

rolling()
derived_stats(stats)
dmg_bonus(stats)