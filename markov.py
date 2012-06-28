import random 

def process_file(filename):
	output = open(filename, "r")
	line = output.read()
	output.close()
	words = line.split()
	#print words
	
	markov = {}

	for i in range(len(words)-2): 
		#print i, len(words)
		prefix = (words[i], words[i+1]) 
		suffix = words[i+2]
		# markov[prefix] = suffix

		if markov.get(prefix):
			markov[prefix].append(suffix)
		else:
			markov[prefix] = [suffix]
	
	return markov

def shift(t, new_element):
	return (t[1], new_element)

def build_sentence(mdict): 
	prefix = random.choice(mdict.keys())
	suffix = random.choice(mdict[prefix])
	l = [prefix[0], prefix[1], suffix]
	while True:
		if suffix[-1] in "!?.": 
			break
		else:
			prefix = shift(prefix, suffix)
			suffix = random.choice(mdict[prefix])
			l.append(suffix)
	sentence = " ".join(l)
	sentence = sentence[0].capitalize()
	return sentence

def build_paragraph(mdict, n):
	sentences = []
	for i in range(n):  
		sentences.append(build_sentence(mdict))
	paragraph = " ".join(sentences)
	return paragraph

def build_tweet(mdict):
	tweet = build_sentence(mdict)
	while len(tweet) > 140:
		tweet = build_sentence(mdict)
	return tweet 

def main():
	mdict = process_file("emma.txt")
	print build_sentence(mdict)
	print build_paragraph(mdict, 3)
	#print mdict
	pass



#for bottom of file
if __name__ == "__main__":
		main()


# 		# (a, b) + (c, )  
# 		# (a, b, c )