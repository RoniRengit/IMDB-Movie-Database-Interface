"""*****************MOVIE DATABASE INTERFACE(MDI)**********************
An interface to check out all movie/serial information. You can
search by movie name and year. You can get a hell lot of information
such as language, release date, genre, actors, director, writer,
imdn rating, rotten tomatoes rating, etc. You can also download
the poster of the movie.

I have done error checking but if I have missed something, do let me know

Like always, feel free to modify, share this code. Do give me a
shout if you find any errors. Thank you.

Disclaimer: The script is for educational purposes only. The author
hold no responsibility whatsover for any misuse.
---------------------------------------------------------------------
Credits:
Brian Fritz: Thank you for the OMDB API
Quorans: For giving me the idea
Stack Overflow: For helping me when I am stuck
Python: For being the best
---------------------------------------------------------------------
Created by Roni Rengit
""" 

#/usr/local/bin/python
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from os import path
from os import sys

API=r'http://www.omdbapi.com/?'
movie='t='
year='y='
plot='plot=full' #short or full
rt_rating='tomatoes=true' # Rotten Tomatoes rating
include='&'

#Uses the omdb API
def movie_db():
    
    try:
        movie_name=input("Enter movie name: ")
        if(movie_name.find(" ")):
            movie_name=movie_name.replace(" ", "+")
        choice=input("Do you want to search by year(Y or N): ")
        if (choice=='Y')or(choice=='y'):
            release_year=input("Enter year: ")
            search=API+movie+movie_name+include+year+release_year+include+plot+include+rt_rating
        else:
            search=API+movie+movie_name+include+plot+include+rt_rating
    except:
        print("Movie not found. Try Again")
        input();    
    #Parsing and loading JSON data
    try:
        file=urlopen(search)
        soup=BeautifulSoup(file, "html.parser")
        result=json.loads(str(soup))
    except:
        print("Website Error!!!! Please try again")
        input()

    #Movie Information  
    info=['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre',
          'Director', 'Writer', 'Actors', 'Plot','Language', 'Awards',
         'Poster', 'Metascore', 'imdbRating', 'Type' ]

    for names in info:
        try:
            result[names]
        except KeyError:
            print("Please check the movie name...\n")
            movie_db()
    
    #Formating information
    print(100*'*'+"\n")
    print(str.capitalize(result['Type'])+": ",result['Title']+"\t\t\t\t\t\t\t"+"Runtime: ",result['Runtime'])
    print("Language: "+str.capitalize(result['Language'])+"\t\t\t\t\t\t"+"\t\tRelease Date: "+result['Released'])
    print("Rated: "+result['Rated']+"\t\t\t\t"+"\t\t\t\tGenre: "+result['Genre']+"\t\t\t")
    print("IMDB Rating: "+result['imdbRating']+"\t\t\t\t\t\t\t"+"IMDB votes: "+result['imdbVotes'])
    print("Rotten Tomatoes Rating: "+result['tomatoRating']+"\t\t\t\t\t\t"+"Tomato votes: "+result['tomatoUserReviews'])
    print("Actors: "+result['Actors'])
    print("Director: "+result['Director']+"\n")
    print(100*'-')
    print("Plot:\n")
    print(result['Plot']+"\n")
    print(100*'-')
    print("User Reviews: "+result['tomatoConsensus']+"\n")
    global result
    input()
    poster()

#Option to download poster
def poster():
    download=input("Do you want to download the movie poster?")
    if (download=='Y')or(download=='y'):
        choose=input("The file will be saved in the default directory as the script. If you want to change it.Please press 'Y' or 'N'")
        if(choose=='Y')or(choose=='y'):
            location=input("Where do you want to save it(URL):")
            if(path.isdir(location)):
                pass
            else:
                print("Could not find path.")
                poster()
            try:
                img_name=input("File name:")
                if(img_name==' ')or(img_name=='\n')or(img_name=='')or(img_name==None)or(img_name=='Undefined'):
                    print("File name cannot be empty.")
                    img_name=input("File name:")
                else:
                    save_url=location+"\\"+img_name+".jpg"
                    print("You file has been downloaded to "+save_url)
                    urlretrieve(result['Poster'],str(save_url))
            except:
                print("File name error. Try again")
                poster()
        else:
            urlretrieve(result['Poster'],result['Title']+" poster"+".jpg")
    else:
        exit=input("Do you want to search again(Y or N):")
        if(exit=='Y') or(exit=='y'):
            print("")
            movie_db()
#Downloading torrents                      ############ Working on it ###########          
"""
def torrent_download():
    print(20*"*"+"Torrent Download"+20*"*")
    torrent_url=r'http://ritorrent.com/usearch/' #The url keeps changing so you may have edit this time to time
"""
#Welcome Interface
print(20*"*"+"Welcome to Movie Database Interface(MDI)"+20*"*")
print("Creator: Roni Rengit\n")
movie_db()

print("Thank you")
input()
