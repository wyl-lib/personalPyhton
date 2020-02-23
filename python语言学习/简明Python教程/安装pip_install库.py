import os
list = {"qiniusdk"}

try:
	for lit in list:
		os.system("pip install "+ lit )
		print(lit)
except:
	print("The {0:^10} Failed Somehow",lit)

