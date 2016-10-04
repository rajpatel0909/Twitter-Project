import sys
import re
import json
from pprint import pprint

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

	for line in sent_file:
		term, score = line.split("\t")
		scores[term] = int(score)

	#print scores.items() 
	data = []
	#with open('output.json') as json_data:
	for line in tweet_file:
		data.append(json.loads(line))
	#pprint(data)
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
	
	tweet_score = []
	for items in tweets:
		local_score = 0
		wordlist = re.sub("[^\w]", " ", items).split()
		for word in wordlist:
			word = word.lower()
			if scores.has_key(word):
				local_score = local_score + scores[word]
		
		tweet_score.append(local_score)
		print local_score

	#print tweets[len(tweets)-5]
	#print tweets[1]

if __name__ == '__main__':
    main()