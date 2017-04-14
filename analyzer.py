import operator

def sorter(mapped_dict):
	"""This function uses python default sorted function
	to sort a mapped dictionary {..,(word, frequency),...}
	based on the frequency and return a list or sorted tuples
	"""
	sorted_list = sorted(mapped_dict.items(), key=operator.itemgetter(1), reverse= True)
	return sorted_list
