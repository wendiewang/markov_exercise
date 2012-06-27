import random 

def process_file(filename):
	output = open(filename, "r")
	line = output.read()
	output.close()
	words = line.split()
	#print words
	
	markov = {}

 
	for i in range(len(words)-2): 
		prefix = (words[i], words[i+1]) 
		suffix = words[i+2]
		# markov[prefix] = suffix

		if prefix in markov.keys():
			markov[prefix].append(suffix)
		else:
			markov[prefix] = [suffix]
	
	return markov

def shift(t, new_element):
	return (t[1], new_element)

def build_sentence(mdict): 
	prefix = random.choice(mdict.keys())
	suffix = mdict[prefix]
	l = [prefix[0], prefix[1], suffix[0]]
	sentence = " ".join(l)
	return sentence


def main():
	mdict = process_file("sample2.txt")
	print build_sentence(mdict)
	#print mdict
	pass



#for bottom of file
if __name__ == "__main__":
		main()


# 		# (a, b) + (c, )  
# 		# (a, b, c )