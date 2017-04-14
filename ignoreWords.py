def stop_words(stop_list, lower_cased_list):
	"""This function filter outs the words provided
	in the stop_list from the lower_cased_list and
	return the filtered list"""
	for word in stop_list:
		lower_cased_list [:] = (value for value in lower_cased_list if value != word)
	return lower_cased_list
