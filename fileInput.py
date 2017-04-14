# file_input_handling() function works
# as an input handler. It renders the command
# line arguments: .txt file or web url as
# the source of words, and the stop word lists.
# 
# This function split the text file into 
# words and then lowercase them, and if the 
# stop words list is provided it filter out those
# words from the list and return a list of words
# that could be used by other functions.
#
import argparse
import re
import urllib
import validators
import os
import string
from caseNeutralizer import lower_casing
from ignoreWords import stop_words

def file_input_handling():
	parser = argparse.ArgumentParser()
	parser.add_argument('inputFile', help="Enter the input file's name here")
	parser.add_argument('stopFile', help="File with stop words, default to None", nargs='?', default='Empty')
	args = parser.parse_args()
	infile = args.inputFile
	stop_file = args.stopFile

	if validators.url(infile) is True:
		fileObject = urllib.urlopen(infile)
	elif os.path.isfile(infile) is True:
		fileObject = open(infile, 'r')
	else:
		raise IOError("Make sure you enter the correct  file or web url.")

	crudeList = []
	for line in fileObject:
		crudeList.extend(re.findall("\\w+(?:'\\w+)?",line))
	fileObject.close()
	lower_cased = lower_casing(crudeList)

	if os.path.isfile(stop_file) is True:
		f =  open(stop_file, 'r') 
		stop_list = [line.strip() for line in f]
		final_list = stop_words(stop_list, lower_cased)
		return final_list
	else:
		return lower_cased
