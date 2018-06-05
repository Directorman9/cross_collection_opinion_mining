#This Python file uses the following encoding: utf-8
'''
Calculated sentiment scores for each topic and perspective 
Run the code as python cclda_sentiment_measure.py cclda_post_processed_outputfile
Where cclda_post_processed_outputfile is the file obtained after post processing cclda output. 
'''

import codecs, sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
reload(sys)
sys.setdefaultencoding('utf8')

#Get the command line arguments
inputfile = sys.argv[1]
outputfile = inputfile + 'sents'

#Get opinion words from cclda post processed output file
c=False # p stands for isCollection
topics = []
topic = []
col = [[],[],[],[],[],[]]
with codecs.open(inputfile, encoding='utf-8', mode='r', errors='ignore') as inputFile:
     for line in inputFile:
         line = line.strip()
         if not line: continue
         if c == True:
            if line[0:11] == '-Collection':
               topic.append(col[i])
               col[i] = []
               i = int(line[12])
            else:
               if line[0:5] == 'Topic': 
                  topic.append(col[i])                 
                  topics.append(topic)
                  c = False
                  col[i] = []
                  topic = []
               else:
                  col[i].append(line)
         else:                            
            if line[0:11] == '-Collection':
               i = int(line[12])
               c = True
     topic.append(col[i])
     topics.append(topic)


def listTosentence(listItem):
    sentence = ''
    for item in listItem:
        sentence = sentence + ' ' + item
    return sentence

def sentiment(sentence):
    scores = analyser.polarity_scores(sentence)
    compound = scores['compound']
    return compound

sent_topics = [[sentiment(listTosentence(opinion_words)) for opinion_words in topic] for topic in topics]


#print pairwise distances to a file
with codecs.open(outputfile, encoding='utf-8', mode='w', errors='ignore') as outputFile:
     outputFile.write("sentiment scores for each topic and perspective \n")
     for topic in sent_topics:           
         for opinion in topic:
             outputFile.write('%s, ' %(opinion))
         outputFile.write('\n')


