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
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	#hw()
	l_s = lines(sent_file)
	l_t = lines(tweet_file)
	scores = {}
	sent_file.seek(0,0)
	tweet_file.seek(0,0)
	#creating dic. for affinn terms with (terms, senti.)
	for line in sent_file:
		term, score = line.split("\t")
		scores[term] = int(score)
	
	#print scores.items()
	
	#creating list for lines in output.json file
	data = []
	#with open('output.json') as json_data:
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
	
	#creating dic with non-sentiment terms with initial senti. 0
	nst = {}	
	for items in tweets:
		wordlist = re.sub("[^\w]", " ", items).split()
		for word in wordlist:
			word = word.lower()
			if scores.has_key(word):
				skip = 0
			else:
				nst[word] = 0.0
	
	nst_len = len(nst)
	#generating sent values for non_sent_terms
	for terms in tweets:
		wl = re.sub("[^\w]", " ", terms).split()
		
		wl_len = len(wl)
		c = 0
		for w in wl:
			if scores.has_key(w):
				if c == 0:
					try:
						nst[wl[c+1]] = nst[wl[c+1]] + (scores[w]/nst_len)
					except:
						skip = 0
				elif c == (wl_len - 1):
					try:
						nst[wl[c-1]] = nst[wl[c-1]] + (scores[w]/nst_len)
					except:
						skip = 0
				elif c == 1:
					try:
						nst[wl[c-1]] = nst[wl[c-1]] + (scores[w]/nst_len)
					except:
						skip = 0
					try:
						nst[wl[c+1]] = nst[wl[c+1]] + (scores[w]/nst_len)
					except:
						skip = 0
				else:
					try:
						nst[wl[c-1]] = nst[wl[c-1]] + (scores[w]/nst_len)
					except:
						skip = 0
					try:
						nst[wl[c+1]] = nst[wl[c+1]] + (scores[w]/nst_len)
					except:
						skip = 0
		
			c = c + 1

	nst_keys = nst.keys()
	for k in nst_keys:
		print k," ",nst[k]



if __name__ == '__main__':
    main()