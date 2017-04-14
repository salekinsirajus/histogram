import matplotlib.pyplot as plt

def hist_graphic(words):
	"""This function uses matplotlib to 
	display a graphical version of the
	histogram.
	"""
	wordsdict = {}

	for w in words:
		wordsdict[w[0]]=w[1]

	plt.bar(range(len(wordsdict)), wordsdict.values(), align='edge')
	plt.xticks(range(len(wordsdict)), wordsdict.keys())

	plt.show()
	plt.close()
