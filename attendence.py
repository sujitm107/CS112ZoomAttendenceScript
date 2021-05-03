import os
from os import listdir
import sys
import pandas as pd # MIGHT HAVE TO IMPORT

# SAMPLE RUN: python3 attendence.py <DirectoryName> <SHORT / LONG>
# Example: python3 attendence.py Section12 SHORT

section = sys.argv[1]
form = sys.argv[2]

if not(form=="SHORT" or form=="LONG"):
	exit()

# COLORS FOR PRINTING 
class bcolors:
	GREEN = '\033[92m' #GREEN
	RED = '\033[91m' #RED
	RESET = '\033[0m' #RESET COLOR

print("Generating Attendence Report For", section)

total_Attendence_Table = {}

dirStem = "./" + sys.argv[1]
files = listdir(dirStem)

# For Every Meeting
for file in files:
	if(file == ".DS_Store"):
		continue

	csv_Path = dirStem + "/" + file

	attendence = pd.read_csv(csv_Path)
	for i in attendence["Name (Original Name)"]:
		current = []
		name = str.lower(i)
		if(total_Attendence_Table.get(name) is not None):
			current = total_Attendence_Table.get(name)

		current.append(file)
		total_Attendence_Table[name] = current


for key in total_Attendence_Table:
		count = len(total_Attendence_Table[key])

		str = key + ": "+ f'{count}'

		if form == "LONG":
			str = key + ": "+ f'{count}' + f'{total_Attendence_Table[key]}'

		if(len(total_Attendence_Table[key]) < 10):
			print(bcolors.RED, end="")
			print(str)
			print(bcolors.RESET, end="")
		else: 
			print(str)


	
# print(total_Attendence_Table)
# roster = pd.read_csv("./Section")

