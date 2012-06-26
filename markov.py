

def process_file(filename):
	output = open(filename, "r")
	line = output.readline()
	output.close()
	line = line [0: -1]
	words = line.split(" ")
	#print words
	
	markov = {}
	
	if len(line) > 3: 
		prefix = (words[0], words[1]) 
		suffix = [words[2]]
		markov[prefix] = suffix
	
	return markov

def shift():	
		# t = (words[0], words[1])
		# tuple_shifted = process_file(words)
		# print tuple_shifted
	

def main():
	#print process_file("sample2.txt")
	pass

#for bottom of file
if __name__ == "__main__":
		main()


		# (a, b) + (c, )  
		# (a, b, c )