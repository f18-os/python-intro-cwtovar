import sys
import re
import collections

if len(sys.argv) is not 3:
	print("Correct usage: wordCount.py <input text file> <output file>")
	exit()

wordCount={}
with open(sys.argv[1], 'r') as inputFile:

	for line in inputFile:
		line = line.casefold()
		line = line.strip()
		words = re.split('[ \W,\t]', line)
		for word in words:
			if word not in wordCount:
				wordCount[word] = 1
			else:
				wordCount[word] += 1
	
wordCountSorted=collections.OrderedDict(sorted(wordCount.items()))

with open(sys.argv[2],"w") as outputFile:
	for i, (k,v) in enumerate(wordCountSorted.items()):
		if i == 0:
			pass
		else:	
			outputFile.write('{0} {1}\n'.format(k,v))