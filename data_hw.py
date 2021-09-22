

import numpy
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob


def recupcom():   #this definition use bs4 to extract from the html file reviews)
    Lcom=[]
    
    for sub_heading0 in soup.find_all('div',class_='the_review'): #the class use to store review is the_review, contain the text from the review
        Lcom.append(sub_heading0.text)

    return Lcom #return list of review (List of strings)



print("Choose movie review: \n1) Hacksaw ridge\n2) Suicide Squad(2016)\n3) Batman Begins \n4) The circle") #a basic selection menu to choose between 4 pre-set movies
url=int(input(":"))
   
if url==1:
    url=["https://www.rottentomatoes.com/m/hacksaw_ridge/reviews","Hacksaw ridge"] #List to store url of RottenTomates and name of the movie
if url==2:
    url=["https://www.rottentomatoes.com/m/suicide_squad_2016/reviews","Suicide Squad(2016)"]
if url==3:
    url= ["https://www.rottentomatoes.com/m/batman_begins/reviews","Batman Begins"] 
if url==4:
    url =["https://www.rottentomatoes.com/m/the_circle_2017/reviews","The circle"]
        
    
page = requests.get(url[0]) #use requests to reserv the html file from the server
soup = BeautifulSoup(page.text, 'html.parser') #convert the package receive into text


print("=============================")
print("Considering reviews...")

Polarity_Score=[]
n=0
for i in recupcom(): #for each review a score of positivity is given using tokenriser and words analysis include in TextBlob
    n+=1
    blob=TextBlob(i)
    Polarity_Score.append(blob.sentiment.polarity)
# print(Polarity_Score)

result=numpy.mean(Polarity_Score) #making a mean value of positivity 
# print(result)

if result>=0.1: #estimate value between a bad and good movie, find using different movies as example 
    print(url[1]+"is a Good movie") 
else:
    print(url[1]+"is a Bad movie")