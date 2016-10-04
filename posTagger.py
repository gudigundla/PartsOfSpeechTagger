from nltk.corpus import brown
from collections import Counter
from collections import defaultdict
from nltk.util import ngrams
from itertools import product
from math import log

def posTagger():
	tokens, tags = zip(*brown.tagged_words())
	tagCounter = Counter(tags)
	tokenCounter = Counter(tokens)

	tokenTags = defaultdict(Counter)
	for token, tag in brown.tagged_words():
	    tokenTags[token][tag] +=1

	tagTags = defaultdict(Counter)
	posBigrams = ngrams(tags, 2)

	for tag1, tag2 in posBigrams:
	    tagTags[tag1][tag2] += 1

	sentence='time flies like an arrow'
	sTokens=sentence.split()

	#225 combinations
	allCombinations=[]
	allLists=[]
	count=1
	for t in sTokens:
		#count*=len(tokenTags[t].keys())		
		allLists.append(tokenTags[t].keys())
	allCombinations=list(product(*allLists))	
	maxProbability=float("-inf")
	bestCombination=[]
	for currentCombination in allCombinations:
		probability=0.0
		for index,tag in enumerate(currentCombination):
			if index not in [0,len(currentCombination)-1]:
				if tokenTags[sTokens[index]][tag] !=0:
					probability += log(tokenTags[sTokens[index]][tag]/tagCounter[tag]) 
				if tagTags[currentCombination[index-1]][tag] !=0:
					probability += log(tagTags[currentCombination[index-1]][tag]/tagCounter[currentCombination[index-1]]) 
			elif index==0:
				if tagTags['.'][tag]!=0:
					probability+=log(tagTags['.'][tag]/tagCounter['.'])
			elif index==len(currentCombination)-1:
				if tagTags[tag]['.']!=0:
					probability+=log(tagTags[tag]['.']/tagCounter[tag])
		if probability > maxProbability:
			maxProbability=probability
			bestCombination=currentCombination
		print(currentCombination)
		print(probability)
	print(maxProbability)
	print(bestCombination)


posTagger()







