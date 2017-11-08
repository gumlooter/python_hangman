
''' A revised game of hangman with two game modes. You can guess words at 3
difficulty levels or guess a common phrase. In each mode you only have 6
chances to guess the right letter. You also have the option to play again. '''

import random
import sys

#Global Game Vars
#Update in the 'Reset_values' method if you change these
chances = 6
missed = []
discovered = []
display = ""
#these are never reset during a session
wins = 0
losses = 0


'''
Allows the user to choose between the two game types: words or phrases. 
'''
def choose_game_type():
	options = ['p', 'w', 'P', 'W']
	choice = raw_input("Choose game type: w for words. p for phrases: ")
	if choice.isalpha():
		if len(choice) ==1:
			if choice in options:
				choice = choice.lower()
			else:
				print "That's not one of the options I game you. You never listen. Goodbye"
				sys.exit()
		else:
			print "I only need one letter. You never listen. Goodbye"
			sys.exit()
	else: 
		print "Letters only, gosh. You never listen. Goodbye"
		sys.exit()

	return choice



''' Allows the user to choose the difficulty of a word game. chooses between
easy, medium and hard wordlists. There is only one difficulty level for
phrases. '''

def choose_difficulty():
	options = ['e', 'E', 'n', 'N', 'h', 'H']

	choice = raw_input("Choose difficulty: e for easy. n for normal. h for hard. ")
	if choice.isalpha():
		if len(choice) ==1:
			if choice in options:
				choice = choice.lower()
			else:
				print "That's not one of the options I game you. You never listen. Goodbye"
				sys.exit()
		else:
			print "I only need one letter. You never listen. Goodbye"
			sys.exit()
	else: 
		print "Letters only, gosh. You never listen. Goodbye"
		sys.exit()


	return choice


''' Allows the user to choose the topic of the phrases for a phrase. Currently
hardcoded to i for idioms ''' 
def choose_topic():     
	options = ['i', 'I', 's', 'S']

	choice = raw_input("Choose difficulty: i for idioms. s for slogans: ")
	if choice.isalpha():
		if len(choice) ==1:
			if choice in options:
				choice = choice.lower()
			else:
				print "That's not one of the options I game you. You never listen. Goodbye"
				sys.exit()
		else:
			print "I only need one letter. You never listen. Goodbye"
			sys.exit()
	else: 
		print "Letters only, gosh. You never listen. Goodbye"
		sys.exit()


	return choice
	
'''
Set up game by choosing the target word from a file based on difficulty
'''

def word_game_setup(difficulty):

	all_text = ""

	if(difficulty) == 'e':
		with open('easy_hang_words.txt', 'r') as open_file:
		    all_text = open_file.read()
	elif difficulty == 'n':
		with open('normal_hang_words.txt', 'r') as open_file:
		    all_text = open_file.read()
	elif difficulty =='h':
	#read in options
		with open('hang_words.txt', 'r') as open_file:
		    all_text = open_file.read()

	word_list = all_text.split("\n")
	#choose random word
	target = word_list[random.randrange(0,len(word_list))]
	#print target
	return target

'''
Set up game by choosing the target phrase from a file based on topic
'''

def phrase_game_setup(topic):
	all_text = ""

	if(topic) == 'i':
		with open('idioms.txt', 'r') as open_file:
		    all_text = open_file.read()
	elif(topic) == 's':
		with open('slogans.txt', 'r') as open_file:
		    all_text = open_file.read()


	phrase_list = all_text.split("\n")
	#choose random word
	target = phrase_list[random.randrange(0,len(phrase_list))]
	#try lowercasing the target
	target = target.lower()
	#print target
	return target


"""
Asks the user to submit a letter guess, then validates the input,
shows the letters they missed or reveals the word with the letters
they correctly guessed.

"""

def guess(targeted):
	correct_guess_text = ["You guessed it!", "Nice job!","That's right!","I see what you did there.", "Keep it up!", "Just a few more to go!"]
	global chances 
	global display
	target = targeted
	display = ""

	guess = raw_input("Guess a letter: ")


	if guess.isalpha():
		if len(guess) ==1:
			guess = guess.lower()
			#print "You guessed:  %s" % guess 
			if guess not in target:
				if guess not in missed:
					missed.append(guess)
					print "That's not right. Try again"
					chances -=1
				else:
					print "You already guessed that. Try again"
				print "Missed Letters: ",				
				print missed
			else:
				if guess not in discovered:
					discovered.append(guess)
					print correct_guess_text[random.randrange(0, len(correct_guess_text))]
				else:
					print "You already guessed that. Try again"

		else:
			if guess == "exit" or guess == "quit":
				sys.exit()
			else:
				print "You can only guess one letter at a time"
	else:
		print "Try guessing a letter"

	for n in target:
		if n in discovered:
			display+= n + ' '
		else:
			#if its a space put a space if its a letter put an underscore
			if n == ' ':
				display+=' / '
			else:
				display+='_ '
	print display 


'''Starts the game, reviews the guessing progress and shares the victory or
defeat message'''

def play():

	global wins
	global losses

	game_type = choose_game_type()

	if game_type == 'w':
		difficulty = choose_difficulty()
		target = word_game_setup(difficulty)
	elif game_type == 'p':
		topic = choose_topic()
		target = phrase_game_setup(topic)
		#print target
		#print len(target)


	while chances >0:

		current_guess = ""

		guess(target)
		print "You hace %s guesses remaining." % chances


		#grab the words
		target_words = display.split("/")
		#take out the spaces
		for word in target_words:
			current_guess  += word.replace(" ", "") +" "
		#print len(test)

		#remove trailing space
		if current_guess [len(current_guess )-1] == ' ':
			current_guess  = current_guess [0:len(current_guess )-1]
		#print the new string
		#print current_guess
		#print len(current_guess)

		#what to do if you get the word/phrase right
		if current_guess == target:
			if game_type == 'p':
				print "That's right! The correct phrase was: %s" % target
			else:
				print "That's right! The correct word was: %s" % target
			print "You win!"
			wins+=1
			print "You've won %d times" % wins
 			play_again()	
	else:
		print "Game Over! You Lose"
		print "The correct word was: %s" % target
		losses+=1
		print "You've lost %d time(s)" % losses

		play_again()


'''
Asks the user if they want to play again. Kicks off a new game or ends the game session
It also shares the win percentage and times played when leaving the session.
'''

def play_again():
	again = raw_input("Wanna play again? Y/N: ")
	if again.isalpha():
		if len(again) ==1:
			if again.lower() == 'y':
				reset_values()
				play()
			else:
				print "Thanks for playing!"
				rounds = wins+losses
				percent =(float(wins)/(rounds)) * 100
				print "You played %d times" % rounds
				print "You won %0.1f%% of games!" % percent
				sys.exit()
		else:
			print "I only wanted one letter. You never listen. Goodbye"
			sys.exit()
	else:
		print "C'mon I asked for letters. You never listen. Goodbye"
		sys.exit()

'''
Resets global game value variables
'''

def reset_values():
	global chances
	global missed
	global discovered
	global display

	chances = 6
	missed = []
	discovered = []
	display = ""


print "Welcome to Hang_words." 
print "You can quit the game by typing 'exit' or 'quit' instead of guessing a letter. "
print 
play()
