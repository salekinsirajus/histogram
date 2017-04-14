def stemmer(word_list):

	""" This is a very primitive stemmign fucntion.
 	We first went through the most common prefixes,
 	and then most common suffixes. The aim was to
 	reduce the words into a singular, simpler, mostly noun form
 	as opposed to to the "root" of the word. This is
 	done considering the aim of the lab: finding the most
 	frequent words. In order to get a get a better result
 	in respect to the lab's goal while keeping only
 	roots of the words, we need a more sophisticated algorithm
 	which is perhaps out of the scope of the lab.

 	Usage of this feature is very easy:
 	when you run the driver.py program, it will ask for enabling
 	stemming. Type y if you want it enabled.

	In order to use this feature standalone, you need to
 	pass a python list of words to the function stemmer()
 	and it will return a list of stemmed words."""

	vowels = ['a', 'e', 'i', 'o', 'u']
	semi_vowels = ['w', 'y']
	vowel_sounds = vowels + semi_vowels
	consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']

	stemmed = []
	# Most common prefixes
	for element in stemmed:
		if element [:6] == 'extra-':
			stemmed.append(element[6:])     # stripping extra off
		elif  element [:5] == 'trans':
			stemmed.append(element[5:])     # transmission to mission
		elif element [:5] == 'under':
			stemmed.append(element[5:])     # underestimate to estimate
		elif element [:2] == 'un':
			stemmed.append(element[2:])     # undo to do 
		elif element [:5] == 'inter':
			stemmed.append(element[:5])     # international to national
		elif element [:2] == 'in':
			stemmed.append(element[2:])     # indirect to direct
		elif element [:2] == 'il':
			stemmed.append(element[2:])     # illegal to legal
		elif element [:2] == 'ir':
			stemmed.append(element[2:])     # irregular to regular
		elif element [:3] == 'dis':
			stemmed.append(element[3:])     # disservice to service
		elif element [:2] == 'de':
			stemmed.append(element[2:])     # defront to frost
		elif element [:2] == 'em':
			stemmed.append(element[2:])     # emblaze to blaze
		elif element [:2] == 'en':
			stemmed.append(element[2:])     # encage to cage
		elif element [:3] == 'non':
			stemmed.append(element[3:])     # nonhuman to human
		elif element [:4] == 'over':
			stemmed.append(element[4:])     # overuse to use
		elif element [:5] == 'super':
			stemmed.append(element[5:])     # superman to man
		elif element [:3] == 'sub':
			stemmed.append(element[3:])     # subpar to par
		elif element [:3] == 'pre':
			stemmed.append(element[3:])     # preapprove to approve
		elif element [:4] == 'semi':
			stemmed.append(element[4:])     # semifinal to final
		elif element [:3] == 'mis':
			stemmed.append(element[3:])     # misjudge to judge
		elif element [:3] == 'mid':
			stemmed.append(element[3:])     # midway to way
		elif element [:4] == 'fore':
			stemmed.append(element[4:])     # foresee to see
		elif element [:5] == 'anti-':
			stemmed.append(element[5:])     # anti-matter to matter
		else:
			stemmed.appned(element)
	# Most common suffixes
	for element in word_list:
		stemmed.append( element)
		if len(element) <= 3:	# too small to have any suffix/prefix
			stemmed.append(element)
		elif element [-3:] == 'ies': # usually plural
			stemmed.append(element [:-3]+ 'y')
		elif element [-4:] == 'less':
			stemmed.append(element [:-4])
		elif element [-5:] == 'iness':	# words like happiness
			stemmed.append(element [:-5])
		elif element [-4:] == 'ness':	# words like darkness
			stemmed.append(element[:-4])
		elif element[-2:] == 'es':	# checking if it ends at 
						# either 's,x,ch,sh'
			if element [-3:] == 'ses': 
				stemmed.append(element[:-2])
			elif element [-3:] == 'xes': 
				stemmed.append(element[:-2])
			elif element [-3:] == 'ches': 
				stemmed.append(element[:-2])
			elif element [-3:] == 'shes': 
				stemmed.append(element[:-2])
			else:			# if not, it's not probably a plural word
				pass
		elif element[-2:] == 'cs':	#this usually means not plural
			stemmed.append(element)
		elif element[-2:] == "'s":	# possesives: Jack's to Jack
			stemmed.append(element[:-2])	
		elif element[-1:] == 's':	#cutting the s's off
			stemmed.append(element[:-1])
		elif element [-2:] == 'ed':	# ending with 'ed'
			if element [-3:-2] == element [-4:-3]:
				stemmed.append(element[:-3])	# dropped to drop 
			elif element [-3:-2] in consonants and element[-4:-3] in vowels:
				stemmed.append(element[:-1])	# v-c-e rule, smiled to smile
			else:
				stemmed.append(element[:-2]) 	# ended to end (just omit the -ed)
		elif element[-5:] =='thing':	# words that end with a 'thing'
			stemmed.append(element[:-5])
		elif element[-4:] == 'eing':	# for example, freeing to free
			stemmed.append(element[:-3])
		elif element[-4:] == 'ying':	# y stays, like playing
			if len(element) == 5:
				stemmed.append(element[:-4]+'ie')	#like dying, lying
			else:
				stemmed.append(element[:-3])
		elif element[-3:] == 'ing':	# general 'ing'
			if len(element) == 4:	#it's too small, like ping
				stemmed.append(element)
			if element [-4:-3] == element [-5:-4]:
				stemmed.append(element[:-3])    # dropping to drop 
			elif element [-4:-3] in consonants and element[-5:-4] in vowels:
				stemmed.append(element[:-1])    # v-c-e rule, smiling to smile
			else:
				stemmed.append(element[:-3])
			#need to go through silent cases

		elif element[-5:] == 'ships':	# friendships
			stemmed.append(element[:-5])
		elif element [-4:] == 'ship':	# courtship
			stemmed.append(element[:-4])
		elif element [-4:] =='iful':
			stemmed.append(element[:-4]+'y')	#plentiful to plenty
		elif element [-3:] == 'ful':	# soulful
			stemmed.append(element[:-3])
		elif element [-3:] == 'yed':	#as in played, stayed
			stemmed.append(element[:-2])
		elif element [-3:] == 'ied':
			stemmed.append(element[:-3]+'y')	#as in carried
		elif element [-4:] == 'ment':
			stemmed.append(element[:-4])	# amamzement to amaze
		elif element [-2:] == 'er' and len(element)>3 :
			stemmed.append(element[:-2])	# worker, player to work, play
		elif element [-4] == 'iest':		# happiest to happy
			stemmed.append(element[:-3]+'y')
		else:
			 stemmed.append(element)
	return stemmed