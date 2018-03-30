# Takes in a file words.txt with words all in one line and separated by commas and creates
# file words_sorted.txt-the words listed in alphabetical order.
# Runs as is with python3 interpreter.

# Written by Douglas Brunson (2018)

##########################################################################
# Reading in comma-delimited words from user-provided text file words.txt.
##########################################################################
alphabetList = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
myFile = open('words.txt','r')
wordString = myFile.read()
wordString = wordString.lower()
wordList = wordString.split(',')
wordList[-1] = wordList[-1][0:-1]  #Eliminating end-of-line character.
numWords = len(wordList)
##########################################################################
# Function for ordering two inputted words.
# Returns True if word1 < word2.
##########################################################################
def wordCompare(word1,word2):	#Both word1 and word2 are strings.
    if (len(word1) > len(word2)):
        low = len(word2)
    elif (len(word2) > len(word1)):
        low = len(word1)
    else:
        low = len(word1)
    cond = True
    for i in range(0,low):
        if (word1[i] != word2[i]):
            if (alphabetList.index(word1[i]) < alphabetList.index(word2[i])):
                cond = True
                break
            else:
                cond = False
                break
    equal_first_letters = True
    for i in range(0,low):
        if not(alphabetList.index(word1[i]) == alphabetList.index(word2[i])):
            equal_first_letters = False
            break
    if (cond==True and equal_first_letters == True):
        if (len(word1) > len(word2)):
            cond = False
    return cond
##########################################################################
# Sorting algorithm (Implementation of Bubble Sort).
##########################################################################
swapCount = 1	#In order to initiate loop.
while (swapCount > 0):
	swapCount = 0
	for i in range(0,numWords-1):
		if wordCompare(wordList[i],wordList[i+1])==False:
			word1 = wordList[i]
			word2 = wordList[i+1]
			wordList[i] = word2
			wordList[i+1] = word1
			swapCount += 1
##########################################################################
# Writing sorted list of words to file words_sorted.txt.
##########################################################################
myFile.close()
newFile = open('words_sorted.txt','w+')
for word in wordList:
	newFile.write(word)
	newFile.write('\n')
##########################################################################












