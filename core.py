"""This file contains the three core algorithms that
we employ in the program to analyze and see which produces
the fastest results.
"""
from collections import Counter
import heapq

def freq_mapper_to_dict(raw_words):
	seen_count = 0
	mapper = {}
	for word in raw_words:
		if word not in mapper:
			mapper[word] = 1
		else:
			mapper[word] = mapper[word] + 1
	return mapper

def freq_mapper_Counter(raw_list):
	mapped = Counter(raw_list)
	return mapped

def maxheap_magic(freq_mapped_list):
	heapq.heapify(freq_mapped_list) 
	k = 10
	top_ten = []
	heap = freq_mapped_list
	for i in range(0,k):
		tup = heapq.heappop(heap)
		top_ten.append(tup)
	top_ten = [(word, -freq) for freq, word in top_ten]
	return top_ten