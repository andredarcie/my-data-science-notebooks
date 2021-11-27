#!/usr/bin/env python3

import sys
from itertools import groupby
from operator import itemgetter

SEP = "\t"

# c. Quais aeroportos cada companhia passou
class Reducer(object):

	def __init__(self, infile=sys.stdin, separator=SEP):
		self.infile = infile
		self.sep = separator

	def emit(self, key, value):
		sys.stdout.write(f"{key}{self.sep}{value}\n")

	def reduce(self):
		for current, group in groupby(self, itemgetter(0)):
			try:
				airports_comp = []
				for item in group:
					for airport in item[1].split(','):
						if airport not in airports_comp:
							airports_comp.append(airport)
				
				self.emit(current, airports_comp)
			except:
				pass

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