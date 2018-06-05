#This Python file uses the following encoding: utf-8
'''
Measures topic coherance (lcp, pmi, npmi and cosine similarity) for every topic in the given refined cclda,cptm or tam refined file. 
Run the code as python coherence_measures.py inputDir/
Where inputDir is the directory containing refined outputfiles in .txt format.
'''

import codecs, sys, pickle, os, string
from gensim.topic_coherence import probability_estimation, direct_confirmation_measure, indirect_confirmation_measure
reload(sys)
sys.setdefaultencoding('utf8')
punctuation1 = """.—:-"""

#Get the command line arguments
inputDir = sys.argv[1]

#Load corpus from disc
corpus = pickle.load(open("wiki_corpus.p", "rb"))

#Load dictionary from disc
w2id = pickle.load(open("wiki_w2id.p", "rb"))

#Get topic words from tam refined output files
for file in os.listdir(inputDir): 
    inputfile = os.path.join(inputDir, file) 
    outputfile1 = inputfile + 'lcp'
    outputfile2 = inputfile + 'pmi'
    outputfile3 = inputfile + 'cosim'
    outputfile4 = inputfile + 'npmi'
    topics = []
    topic = []
    with codecs.open(inputfile, encoding='utf-8', mode='r', errors='ignore') as inputFile:
         for line in inputFile:
             line = line.strip()
	     if not line:continue
             if line[0:5] != 'Topic':
                puncFree = ''.join([ch if ch not in punctuation1 else ' ' for ch in line])
                tokenized = puncFree.split()
                filtered = filter(lambda x:x[0].isdigit() == False , tokenized)
                if filtered[0] not in topic: topic.append(filtered[0])
                if filtered[1] not in topic: topic.append(filtered[1])
             else:
                topics.append(topic)
                topic = []
    topics.append(topic)
    topic = []
    topics = topics[1:]


    #Make segmented & unsegmented topics
    segmented_topic = []
    segmented_topics = []
    unsegmented_topic = []
    unsegmented_topics = []
    for k in range(len(topics)):
	for j in range(len(topics[k])):
	    for i in range(j+1,len(topics[k])):  
		try:
		   w1 = w2id[topics[k][j]]
		except:                 
		   print ("%s not in corpus" %(topics[k][j]))
		   continue
		try:
		    w2 = w2id[topics[k][i]]
		except:                 
		    print ("%s not in corpus" %(topics[k][i]))
		    continue
		tupl = (w1,w2)
                unsegmented_topic.append(w1)
		segmented_topic.append(tupl)             
	segmented_topics.append(segmented_topic)
        unsegmented_topics.append(unsegmented_topic)
	segmented_topic = []
        unsegmented_topic = []


    #Make accumulator
    accumulator = probability_estimation.p_boolean_document(corpus, segmented_topics)   
  
 
    #Perform the measurements and print results
    
    lcp = direct_confirmation_measure.log_conditional_probability(segmented_topics, accumulator)

    with codecs.open(outputfile1, encoding='utf-8', mode='w', errors='ignore') as outputFile:
         for item in lcp:
             outputFile.write('%s \n' %(item))

    pmi = direct_confirmation_measure.log_ratio_measure(segmented_topics, accumulator)

    with codecs.open(outputfile2, encoding='utf-8', mode='w', errors='ignore') as outputFile:
         for item in pmi:
             outputFile.write('%s \n' %(item))

    cosim = indirect_confirmation_measure.cosine_similarity(segmented_topics, accumulator, unsegmented_topics, 'nlr', 1)    

    with codecs.open(outputfile3, encoding='utf-8', mode='w', errors='ignore') as outputFile:
         for item in cosim:
             outputFile.write('%s \n' %(item))
    
    npmi = direct_confirmation_measure.log_ratio_measure(segmented_topics, accumulator, normalize=True)

    with codecs.open(outputfile4, encoding='utf-8', mode='w', errors='ignore') as outputFile:
         for item in npmi:
             outputFile.write('%s \n' %(item))
 

    

    
