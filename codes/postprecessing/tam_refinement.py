#This Python file uses the following encoding: utf-8
'''
Refines cclda output by taking top 5 words on every topic based on word similary measured using pre-trained word embeddings.
Run the code as python tam_refinement.py embeddings_dictionary inputDir/
Where inputDir is the directory containing tam post processed outputfiles.txt and embeddings_dictionary is a dictionary containing pretrained embeddings saved to disk using pickles
'''

import codecs, sys, pickle, os, csv
import operator as op
import numpy as np
reload(sys)
sys.setdefaultencoding('utf8')


#Get the command line arguments
embeddings = sys.argv[1]
inputDir = sys.argv[2]

#Load dictionary to memory
dictionary = pickle.load( open(embeddings, "rb" ) ) 

def pairDistance(arg1, arg2):
    try:
       v1 = dictionary[arg1]
    except:                 
       print ("%s not in embeddings" %(arg1))
       return 0
    try:
       v2 = dictionary[arg2]
    except:
       print ("%s not in embeddings" %(arg2))
       return 0
    try:
       a = map(lambda x: float(x),v1)
    except:
       print 'v1 could not be converted to float'
       return 0
    try:
       b = map(lambda x: float(x),v2)
    except:
       print ' v2 could not be converted to float'
       return 0
    if len(a) == len(b):
       distance = cos_sim(a,b)
       return distance
    else:
       print 'length not equal'
       return 0


def bestAddition(currentArray, topic):
    currtArray = currentArray
    max_aveD = 0 
    toBeAdded = ''
    for i in range(len(topic)):
        currtArray.append(topic[i])
        aveD = averageDistance(currtArray)
        if aveD > max_aveD:
           max_aveD = aveD
           toBeAdded = topic[i]
        currtArray.remove(topic[i])
    return toBeAdded


def cos_sim(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)


def averageDistance(array):
    summ = 0
    for j in range(len(array)):
        for i in range(j+1,len(array)):
            summ = summ + pairDistance(array[j], array[i])
    average = summ//len(array)
    return average


def bestPair(words):
    maxD = 0 
    bestPair = ()
    for j in range(len(words)):
        for i in range(j+1,len(words)):
            distance = pairDistance(words[j],words[i])
            if distance > maxD:
               maxD = distance
               bestPair = (words[j], words[i], distance)
    return bestPair

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom


#Get topic words from tam output file
for file in os.listdir(inputDir): 
    inputfile = os.path.join(inputDir, file) 
    outputfile1 = inputfile + 'refined'
    outputfile2 = inputfile + 'plot'
    t=False # t stands for isTopic
    p=False # p stands for isPerspective
    topics = []
    topic = []
    with codecs.open(inputfile, encoding='utf-8', mode='r', errors='ignore') as inputFile:
	     for line in inputFile:
		 line = line.strip()
		 if not line: continue
		 if line[0:7] == '--Topic':
		    t=True
		    p=False
		 else:
		    if t==True:                             
		       if line[0:6] == 'Aspect' or line[0:8] == '--Aspect':
		           t=False
		           p=True
		           topics.append(topic) 
		           topic = []
		       else: 
		           topic.append(line) 
		    else:
		        continue
	

    #find the best 5 coherent topic words
    topwords = []
    allTopicsTopwords = []
    for topic in topics:
	bestPair = bestPair(topic)
        topwords.append(bestPair[0])
        topwords.append(bestPair[1])
        topic.remove(bestPair[0])
        topic.remove(bestPair[1])
	for i in range(3):
                try:
                   addition = bestAddition(topwords, topic)
                   topwords.append(addition)
                   topic.remove(addition)
                except:
                   continue
        allTopicsTopwords.append(topwords)
        topwords = []
    
	    

    #print top topic words to a file
    with codecs.open(outputfile1, encoding='utf-8', mode='w', errors='ignore') as outputFile:
	     for topic in allTopicsTopwords:  
		 outputFile.write("\nTopic %s \n" %(allTopicsTopwords.index(topic) + 1))
		 for word in topic:
		     outputFile.write('%s \n' %(word))
	     

    #print averages pairwise cosine similarity to another file    
    averages = []
    for topic in allTopicsTopwords: 
	average = averageDistance(topic)
	averages.append(average)

    with codecs.open(outputfile2, encoding='utf-8', mode='w', errors='ignore') as outputFile:
	 for item in averages:
	     outputFile.write('%s \n' %(item))



