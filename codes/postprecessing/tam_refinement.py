#This Python file uses the following encoding: utf-8
'''
Refines tam output by taking top 5 words on every topic based on word similary measured using pre-trained word embeddings.
Run the code as python tam_refinement.py cclda_post_outputfile.txt pretrained_embeddings_file
'''

import codecs, sys
reload(sys)
sys.setdefaultencoding('utf8')

#Get the command line arguments
inputfile = sys.argv[1]
embeddings = sys.argv[2]
outputfile1 = inputfile + 'refined'
outputfile2 = inputfile + 'plot'


#Get topic words from tam post processed output file
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


#Load ambeddings to a dictionary
import numpy as np
dictionary = {}
with codecs.open(embeddings, encoding='utf-8', mode='r', errors='ignore') as inputFile:
     for line in inputFile:
         line = line.strip()
         if not line: continue
         tokenized = line.split()  
         word = tokenized[0] 
         vector = tokenized[-100:]
         dictionary[word] = vector  

#Measure average cosine similarity of topic words
def cos_sim(a, b):
	"""Takes 2 vectors a, b and returns the cosine similarity according 
	to the definition of the dot product
	"""
	dot_product = np.dot(a, b)
	norm_a = np.linalg.norm(a)
	norm_b = np.linalg.norm(b)
	return dot_product / (norm_a * norm_b)


import operator as op
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom



topicD = []
allTopicDs = []
for k in range(len(topics)):
    for j in range(len(topics[k])):
        for i in range(j+1,len(topics[k])):  
            try:
               v1 = dictionary[topics[k][j]]
            except:                 
               print ("%s not in embeddings" %(topics[k][j]))
               continue
            try:
               v2 = dictionary[topics[k][i]]
            except:
               print ("%s not in embeddings" %(topics[k][i]))
               continue
            try:
               a = map(lambda x: float(x),v1)
            except:
               print 'v1 could not be converted to float'
               continue
            try:
               b = map(lambda x: float(x),v2)
            except:
               print ' v2 could not be converted to float'
               continue
            if len(a) == len(b):
               distance = (topics[k][j], topics[k][i], cos_sim(a,b))
               topicD.append(distance)
            else:
               print 'length not equal'
               continue  
    topicD.sort(key=lambda tup: tup[2])
    allTopicDs.append(topicD)
    topicD = []



#Take only top topic words based on calculated pairwise distances
allTopicDs = [topicD[-6:] for topicD in allTopicDs]    
    

#print results to a file
with codecs.open(outputfile1, encoding='utf-8', mode='w', errors='ignore') as outputFile:
     for topicD in allTopicDs:  
         outputFile.write("\nTopic %s \n" %(allTopicDs.index(topicD) + 1))
         for distance in topicD:
             outputFile.write('%s-%s : %s \n' %(distance[0], distance[1], distance[2]))


#print averages distances to another file    
summ = 0
averages = []
for topicD in allTopicDs: 
    for distance in topicD:
        summ = summ + distance[2] 
    average = summ/len(topicD)
    summ = 0
    averages.append(average)

with codecs.open(outputfile2, encoding='utf-8', mode='w', errors='ignore') as outputFile:
    for item in averages:
        outputFile.write('%s \n' %(item))


