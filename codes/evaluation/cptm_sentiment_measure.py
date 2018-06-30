#This Python file uses the following encoding: utf-8
'''
Calculated sentiment scores for each topic and perspective 
Run the code as python cptm_sentiment_measure.py cptm_outputfile
'''

import codecs, sys, csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
reload(sys)
sys.setdefaultencoding('utf8')

#Get the command line arguments
inputfile = sys.argv[1]
outputfile = inputfile + 'sents'


#Get topic words from cptm post processed output file
topics = []
opinion = [[],[],[]]

with codecs.open(inputfile, encoding='utf-8', mode='r', errors='ignore') as inputFile:
     reader = csv.reader(inputFile, delimiter=',')
     data = list(reader)
     data = data[1:]

     for row in data:
         if row[0] == '9':
            for i in range(0,3):
                opinion[i].append(row[i+2])
            topics.append(opinion)
            opinion = [[],[],[]]          
         else:
            for i in range(0,3):
                opinion[i].append(row[i+2])
   

      
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


  

