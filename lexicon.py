#Here I will build a program that will examine the validity of the input given by the user
def scan(words):
	directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
	verbs = ['go', 'stop', 'kill', 'eat']
	stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
	nouns = ['door', 'bear', 'princess', 'cabinet']

	
	lex = words.split()
	list1 = []
#To make sure cases don't effect the inputs validity we convert them to lowercase during the check
#If it exists in the dictionary then we append the original input into list1
	for i in lex:
		if i.lower() in directions:
			list1.append(('direction', i))
		elif i.lower() in verbs:
			list1.append(('verb', i))
		elif i.lower() in stop_words:
			list1.append(('stop', i))
		elif i.lower() in nouns:
			list1.append(('noun', i))
		elif i.isdigit():
			list1.append(('number', convert_number(i)))
		else:
			list1.append(('error', i))
	return list1 

def convert_number(s):
	try:
		return int(s)

	except ValueError:
		return None

this = scan('NORTH south cabinet the KILL asdas ok')
print this






#Have different functions that will run depending on what type of word it is
#if its a direction have the function return a list of tuples as (['direction, "their input"'])
