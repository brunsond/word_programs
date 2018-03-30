filename = raw_input("Name of file: ")
textpage = open(filename,'r')
count = 0
for line in textpage:
    count += len(line.split())

print "Number of words: {}".format(count)


