import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
	i = len(fp.readlines())
	#print i
	return i

def main():
	tweet_file = open(sys.argv[1])
	#hw()
	l_t = lines(tweet_file)
	scores = {}
	tweet_file.seek(0,0)
	
	#creating list for lines in output.json file
	data = []
	for line in tweet_file:
		data.append(json.loads(line))
	#pprint(data)
	
	#creating list for tweets from data list
	tweets = []
	i = 0
	l = 0
	while i < l_t:
		try:
			tweets.append(data[i]["text"])
			l = l + 1
			i = i + 1
		except:
			i = i + 1
	
	#creating dic with all terms with its occ. as value
	term_occ = {}	
	for items in tweets:
		wordlist = re.sub("[^\w]", " ", items).split()
		for word in wordlist:
			word = word.lower()
			if scores.has_key(word):
				term_occ[word] = term_occ[word] + 1
			else:
				term_occ[word] = 1

	term_occ_keys = term_occ.keys()
	for k in term_occ_keys:
		print k," ",term_occ[k]

if __name__ == '__main__':
    main()
