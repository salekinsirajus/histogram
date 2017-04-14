# This is a driver file for the better maintainance
# and organization of the histogram program

from core import freq_mapper_to_dict, freq_mapper_Counter, maxheap_magic
from fileInput import file_input_handling
from caseNeutralizer import lower_casing
from analyzer import sorter
from ignoreWords import stop_words
from histogramGraphics import hist_graphic
from asciiArt import ascii_hist
from stemming import stemmer
import time
import os


def pure_dictionary(case_neutral_list, visual):
	start = time.time()
	freq_mapped_dict = (freq_mapper_to_dict(case_neutral_list))	# gets the dictionary with frequency mapped to word
	sorted_list = sorter(freq_mapped_dict)		# gets the sorted list based on decreasing frequency
	top_ten = sorted_list[:10]					# slices first ten values to represent
	end = time.time()
	runtime = str(end-start)
	log_file.write("pure_dictionary, ")
	log_file.write("# of words: "+str(len(case_neutral_list))+" ")
	log_file.write("time: "+runtime+"\n")

	ascii_hist(top_ten)

	if visual is True:
		hist_graphic(top_ten)

def collections_Counter(case_neutral_list, visual):
	start = time.time()
	freq_mapped_list = freq_mapper_Counter(case_neutral_list)	# get mapped list using collections.Counter
	top_ten = freq_mapped_list.most_common(10)			# use Counter.most_common(n) to get top ten freq word
	end = time.time()
	runtime = str(end-start)
	log_file.write("collections_Counter, ")
	log_file.write("# of words: "+str(len(case_neutral_list))+" ")
	log_file.write("time: "+runtime+"\n")

	ascii_hist(top_ten)

	if visual is True:
		hist_graphic(top_ten)


def heap_heapq(case_neutral_list, visual):
	start = time.time()
	freq_mapped_dict = (freq_mapper_to_dict(case_neutral_list))		# gets the dictionary with frequ mapped to word
	freq_mapped_list = [((-value, key)) for key, value in freq_mapped_dict.items()]		# converting to a list of (frequncey, word) tuples
	top_ten = maxheap_magic(freq_mapped_list)			# Gets the top ten frequent list
	end = time.time()
	runtime = str(end-start)
	log_file.write("heap_heapq, ")
	log_file.write("# of words: "+str(len(case_neutral_list))+" ")
	log_file.write("time: "+runtime+"\n")

	ascii_hist(top_ten)

	if visual is True:
		hist_graphic(top_ten)

#output log data to a file
if os.path.isfile('runtime.log'):
	log_file = open ('runtime.log', 'a')
else:
	log_file = open('runtime.log', 'w')


if __name__ == '__main__':
	final_words = file_input_handling()	# Getting the workable list prepared

	print ("This program will help you find top 10 most frequent words in a text file.")
	print ("Tap Ctrl+C to quit anytime.")
	quit = True
	algorithm = 0


	while quit:
		print("Which algorthm you want to use?")
		print("Type 1 for the one uses python dictionary and sorted() function ")
		print("Type 2 for the one uses collections.Counter library")
		print("Type 3 for the one uses a heap")
		
		algorithm = raw_input("Enter your algorithm choice:\n")
		visual = raw_input("Do you want a graphical output? Type y for yes, and n for no.:\n")
		stemming = raw_input("Enable stemming? Tap y for yes, any other key for no: ")

		if stemming in ('y','Y'):
			final_words = stemmer(final_words)

		if visual in ('y','Y'):
			if algorithm is '1':
				pure_dictionary(final_words, True)
			elif algorithm is '2':
				collections_Counter(final_words, True)
			elif algorithm is '3':
				heap_heapq (final_words, True)
			else:
				print ("Emter a valid choice between 1-3.")

		elif visual in ('n', 'N'):
			if algorithm is '1':
				pure_dictionary(final_words, False)
			elif algorithm is '2':
				collections_Counter(final_words, False)
			elif algorithm is '3':
				heap_heapq (final_words, False)
			else:
				print ("Emter a valid choice between 1-3.")
		else:
			print ("Enter either y or n for graphical output.")

		quit_msg = raw_input("If you want to quit the program, type Q. Tap any other key to stay on the program.\n")
		if quit_msg in ('q','Q'):
			quit = False
		else:
			quit = True
