#This Python file uses the following encoding: utf-8
'''
Gets movie by id.
Run it as: python get_movie_by_id.py moviesFile
where moviesFile is the file containing all movies.
Author: Hemed Kaporo.
'''

import codecs, sys
reload(sys)
sys.setdefaultencoding('utf8')

#Get the command line arguments
inputfile = sys.argv[1]


#Get data in the collections
i = 0
with codecs.open(inputfile, encoding='utf-8', mode='r',errors='ignore') as inputFile:    
     for line in inputFile:
	 if i>0 and i<7: 
	    i=i+1
	    continue
	 if i>6: 
	    i=0
	    with codecs.open('schoolhouse_rock.txt',encoding='utf-8',mode='a',errors='ignore') as outputFile: 
	         outputFile.write(line[13:len(line)])
	 if line[19:29] == 'B000063W82':   #Change this id depending on what movie you what to extract.
	    i = i+1  

	  
	   
	     
		

