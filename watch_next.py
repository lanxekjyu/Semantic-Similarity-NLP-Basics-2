# Import spaCy module
import spacy

# Load the English language module 'en_core_web_md' and store it in variable 'nlp'
nlp = spacy.load('en_core_web_md')

# Define class Movie 
class Movie():

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.similar = 0

# Define function that prints out the most similar movie to watch next
def next_movie(description):
    
    init_movie_desc = nlp(description)
    
    for movie in movie_list:
        movie_desc = nlp(movie.description)
        movie.similar = movie_desc.similarity(init_movie_desc)

    most_similar_movie = max(movie_list, key = lambda s: s.similar)
    print(f' ► Watch next: "{most_similar_movie.title}"')

# Create an empty list to store movie objects
movie_list = []

# Open 'movies.txt' file then for every line, use the data to create a new movie object, then append this object to 'movie_list'
with open('movies.txt', encoding = 'utf-8') as f:
    for line in f:
        title, description = line.strip().split(' :')
        movie = Movie(title, description)
        movie_list.append(movie)

# Initialize what movie has just been watched
init_movie = Movie('Planet Hulk' , '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.''')

# Suggest the next movie to watch based on similarity to previous movie
next_movie(init_movie.description)
