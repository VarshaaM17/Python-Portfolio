import csv

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#To get a clean tweet
def strip_punctuation(word):
    for character in punctuation_chars:
        word= word.replace(character, '')
    
    return word

#To get clean postive words from the file
def get_pos():
   positive_words = []
   with open ("/Users/varshaamuralidharan/Downloads/positive_words.txt", 'r') as fp:
     readFp= fp.readlines()
   #print (readFp)
     for line in readFp:
       if line[0]!=';' and line[0]!='\n':
        positive_words.append(line.strip())

   return  positive_words      
        
pos_words= get_pos()

#To get clean negative words from the file
def get_neg():
   negative_words = []
   with open ("/Users/varshaamuralidharan/Downloads/negative_words.txt", 'r') as fn:
     readFn= fn.readlines()
     #print (readFn)
     for line in readFn:
       if line[0]!=';' and line[0]!='\n':
        negative_words.append(line.strip())

   return  negative_words      
        
neg_words= get_neg()


with open ("/Users/varshaamuralidharan/Downloads/project_twitter_data.csv", 'r') as f:
  with open ("/Users/varshaamuralidharan/Downloads/resulting_data.csv", 'w') as output:

   writer= csv.writer(output)
   writer.writerow (['Number of Retweets', 'Number of Replies', 'Positive Score', 'Negative Score', 'Net Score'])

   reader= csv.reader(f) #reads the file
   rows= next(reader)     #skips header row
    #print (rows) #To check if header row is printed
   for row in reader:
    #print (row) #displayed in form of a list
    current_tweet= row[0] #To get the cursor at first value in the list
    clean_tweet= strip_punctuation(current_tweet)
    clean_tweet= clean_tweet.lower() #convert the clean tweet to lowercase
    clean_tweet= clean_tweet.split()

    positive_score=0
    negative_score=0

    for each_word in clean_tweet:
      if each_word in pos_words:
        positive_score+=1
      elif each_word in neg_words:
        negative_score+=1

    netscore= positive_score-negative_score

    writer.writerow ([row[1], row[2], positive_score, negative_score, netscore])

  output.close()
  f.close()






    



    

