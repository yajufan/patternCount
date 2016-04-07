# patternCount.py


def patternCount(myWords,width):
	patterns = []
	patternCounts = []

	myWordsOnly = myWords.split()
	print myWordsOnly

	n = len(myWordsOnly)

	# Extract patterns with two characters
	for iter in range(0,n): 
		temp = myWordsOnly[iter]
		n2 = len(temp)	
		for iter2 in range(0,n2-(width-1)):
			tempPattern = temp[iter2:iter2+width]
		
			# Check if the pattern exists
			existence = len([p for p in patterns if p == tempPattern])

			pIdx = 0
			for p in patterns:
				if p == tempPattern:
					existence = 1
					patternCounts[pIdx] += 1
				pIdx += 1
	
			if existence != 1:
				patterns.append(tempPattern)
				patternCounts.append(0)
			
	return patterns, patternCounts


# Test on the function patternCount()
myWords = 'This is a good practice.'

# Length of characters 
width = 2 

patterns, patternCounts = patternCount(myWords,width)

for iter in range(0,len(patterns)):
	print patterns[iter] + ":" + str(patternCounts[iter])
