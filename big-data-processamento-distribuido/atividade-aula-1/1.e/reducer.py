#!/usr/bin/env python3

import sys

from itertools import groupby
from operator import itemgetter

SEP = "\t"

# e. Qual é o vôo mais frequente de cada companhia
class Reducer(object):

	def __init__(self, infile=sys.stdin, separator=SEP):
		self.infile = infile
		self.sep = separator

	def emit(self, key, value):
		sys.stdout.write(f"{key}{self.sep}{value}\n")

	def reduce(self):
		for current, group in groupby(self, itemgetter(0)):

			flights_comp = []
			for item in group:
				flights_comp.append(item[1])

			most_frequent = max(set(flights_comp), key = flights_comp.count)
			self.emit(current, most_frequent)

	def __iter__(self):
		for line in self.infile:
			try:
				parts = line.split(self.sep)
				yield parts[0], parts[1]
			except:
				continue

if __name__ == '__main__':
	reducer = Reducer(sys.stdin)
	reducer.reduce()
