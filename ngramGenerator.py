# This file contains the fuunctions to get
# histograms of different n-grams.
# --------------------------------------
# find_ngrams() function does the actual
# task creating n-grams
#
# hist_to_ngram() function produces
# the histogram from the input given.
#
# and welcome_text() function introduces
# user to the program
#
# USAGE:
# This script works the same way as the main program:
# python ngramGenerator.py fileA stop-words
# It will ask for the length of n-gram you want to generate,
# and then present the result in a histogram format
#
from core import freq_mapper_Counter
from fileInput import file_input_handling
from asciiArt  import ascii_hist

def find_ngrams(input_list, n):
	return zip(*[input_list[i:] for i in range(n)])

def hist_to_ngram(n):
	raw_word_list = file_input_handling ()
	ngrams = find_ngrams(raw_word_list, n)
	freq_mapped = freq_mapper_Counter(ngrams)
	top_ten = freq_mapped.most_common(10)
	top_ten_formatted = [[]]	# formatting list for appropriate ascii_art input
	for i in range(len(top_ten)):
		ngram = top_ten[i][0]
		concat_string = ""
		for j in range (0,n):
			concat_string = concat_string +" " + ngram [j] + " "
		top_ten_formatted.append((concat_string, top_ten[i][1]))
	ascii_hist(top_ten_formatted)

def welcome_text():
	print ("This a script to find the top ten frequent ngrams in a given text.")
	print ("Enter the n-gram you want: (e.g.: 2,3,7 etc.)")
	n = raw_input ()
	n = int(n)
	return n

if __name__ == '__main__':
	n = welcome_text()
	hist_to_ngram(n)
