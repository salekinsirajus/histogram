def lower_casing(passed_list):
	"""This funnction turns the words 
	in the passed_list to their lowercase
	version. For example: "Dog","doG", "dOg", etc too "dog"
	"""
	lowercased = [word.lower() for word in passed_list]
	return lowercased
