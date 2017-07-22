#! /usr/bin/env python
import sys

# Legge un file.
in_file = open("test.txt","r")
text = in_file.read()
in_file.close()

#input comes from STDIN
#remove leading and trailing whitespace
#line=text.strip()
#split the line into words
words=text.split()
#increase counters
for word in words:
		#write results to STDOUT (standard output)
		#what we output here will be the input for the reduce, i.e. input for reducer.py
    print '%s\t%s' %(word, 1)
