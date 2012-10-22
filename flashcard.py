import pdb
import random
import sys

def playgame(filename):

	file = open(filename, 'r')
	dlist = file.readlines()
	
	dictionary = {}
	for x in range(len(dlist)):
		dnewlist = dlist[x].split(',')
		key,value = dnewlist[0].strip(), dnewlist[1].strip()
		dictionary[key] = value
	
	print '\nWelcome to FlashCard. Type "Exit" to quit the game.\n'

	loop = True

	while loop:
		ditem = random.choice(dictionary.keys())
		
		if 'capital' in filename:
			print 'What is the capital of '+ ditem + '?'
		elif 'metric' in filename:
			print 'What is the metric value of '+ ditem + '?'
		elif 'french' in filename:
			print 'What is the English translation for '+ ditem + '?'
		
		correct = 0
		while correct == 0:
			answer = raw_input('Answer here: ').lower()
			if answer == dictionary[ditem].lower():
				print 'Correct'
				break;
			elif answer == 'exit':
				loop = False
				break;
			else:
				print 'Wrong answer. Try Again!'
		    	
	loop = False
	

if len(sys.argv) > 1:
	filename = "/users/sandralombardi/downloads/"+ sys.argv[1]
else:
	filename = "/users/sandralombardi/downloads/state_capitals.txt"

playgame(filename)





