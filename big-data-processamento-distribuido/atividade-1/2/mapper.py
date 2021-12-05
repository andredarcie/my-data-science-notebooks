#!/usr/bin/env python3

import sys

SEP = '\t'

class Mapper(object):

    def __init__(self, infile=sys.stdin, separator=SEP):
        self.infile = infile
        self.sep = separator

    def emit(self, key, value):
        sys.stdout.write(f"{key}{self.sep}{value}\n")

    def map(self):
        cont_line = 1

        for line in self:
           line.split('\n')

           for word in line.split():
               word = ''.join(e for e in word if e.isalnum()).lower()
               
               self.emit(word, cont_line)
           cont_line += 1

    def __iter__(self):
        for line in self.infile:
            yield line.split(self.sep, 1)[1]

if __name__ == "__main__":
    mapper = Mapper()
    mapper.map()
