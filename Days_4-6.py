import csv
from collections import defaultdict, Counter
import os

top_directors = defaultdict(list)
directors = defaultdict(list)
data = os.path.abspath(os.path.join('.', 'data', 'movie_directors.csv'))


def dict_builder(data):
    # Builds dictionary of all directors and movies
    with open(data) as csvdata:
        reader = csv.DictReader(csvdata)
        for row in reader:
            if row['title_year'] == "" or int(row['title_year']) < 1960:
                continue
            else:
                directors[row['director_name']].append([row['movie_title'], row['title_year'], row['imdb_score']])
    return directors


def director_weed_out(directors):
    # deletes directors with less than 4 movies
    for record in list(directors):
        total = 0
        i = 0
        length = len([item for item in directors[record] if item])
        if length < 4:
            del directors[record]
        else:
            for movie in directors[record]:
                total += float(movie[2])
                i += 1
            average = total / i
            top_directors[record].append(average)
    return top_directors


def pretty_printer(top_directors):
    i = 1
    for top in Counter(top_directors).most_common(20):

        print("{:02d} {:<54} {:03.1f}".format(i, top[0], top[1][0]))
        print("-" * 60)
        i += 1
        for movie in directors[top[0]]:
            print("{}]  {:<49}  {:03.1f}".format(movie[1], movie[0], float(movie[2])))
        print('\n')


def main():
    directors = dict_builder(data)
    top_directors = director_weed_out(directors)
    pretty_printer(top_directors)


if __name__ == '__main__':
    main()

# ---------- Alternate method -------------

import warnings

warnings.simplefilter(action='ignore')
import pandas as pd

MOVIE_DATA = 'movie_directors.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960


def get_movies_by_director(MOVIE_DATA):
    '''Extracts all movies from csv and stores them in a dataframe
    where the index is directors, and values is a list of movies (named tuples)'''
    data = os.path.abspath(os.path.join('.', 'data', MOVIE_DATA))
    df = pd.read_csv(data, index_col='director_name',
                     usecols=['director_name', 'movie_title', 'title_year', 'imdb_score'],
                     encoding='latin-1')
    df = df[df['title_year'].notnull() & (df['title_year'] >= 1960)]
    df_counts = df.groupby(['director_name']).count()
    directors = df[df_counts['movie_title'] >= 4]
    return directors


def get_average_scores(directors):
    '''Calculates average score and returns top results'''
    director_averages = directors.groupby(['director_name']).mean()
    return director_averages.nlargest(NUM_TOP_DIRECTORS, 'imdb_score')


def print_results(director_averages, directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    i = 1
    for director, avg in director_averages.iterrows():
        print("{:02d}. {:<53} {:.1f}".format(i, director, avg['imdb_score']))
        print('-' * 60)
        for year, movie in directors.loc[director, 'movie_title':'imdb_score'].iterrows():
            print("{:.0f}]  {:<50} {}".format(movie['title_year'], movie['movie_title'], movie['imdb_score']))
        print("\n")
        i += 1


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director(MOVIE_DATA)
    director_averages = get_average_scores(directors)
    print_results(director_averages, directors)


if __name__ == '__main__':
    main()

#--------- METHOD FROM PYBITES ----------------

import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = r'data\movie_directors.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """
    Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)
    """
    movies_by_director = defaultdict(list)
    with open(MOVIE_DATA, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                director_name = row["director_name"]
                movie_title = str(row["movie_title"])
                title_year = int(row["title_year"])
                movie_score = float(row["imdb_score"])
            except ValueError:
                continue

            if title_year >= MIN_YEAR:
                movie_details = Movie(title=movie_title, year=title_year, score=movie_score)
                movies_by_director[director_name].append(movie_details)

    return movies_by_director


def get_average_scores(directors):
    """
    Filter directors with < MIN_MOVIES and calculate average score
    """

    directors_scores = {director: _calc_mean(movies) for director, movies in directors.items()
                        if len(movies) >= MIN_MOVIES}

    return sorted(directors_scores.items(), key=lambda x: x[1], reverse=True)


def _calc_mean(movies):
    """
    Helper method to calculate mean of list of Movie namedtuples
    """

    movie_scores = [movie.score for movie in movies]
    return round(sum(movie_scores) / len(movies), 1)


def print_results(directors, directors_avg_score):
    """
    Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    """
    for counter, director in enumerate(directors_avg_score):
        print("\n{}. {:<52} {}".format(counter + 1, director[0], director[1]))
        print('-' * 60)
        for movie in sorted(directors[director[0]], key=lambda x: x.score, reverse=True):
            print("{}] {:<50} {}".format(movie.year, movie.title, movie.score))

        if counter == NUM_TOP_DIRECTORS - 1:
            break


def main():
    directors = get_movies_by_director()
    directors_avg_score = get_average_scores(directors)
    print_results(directors, directors_avg_score)


if __name__ == '__main__':
    main()






# from collections import defaultdict, namedtuple, Counter, deque
# import csv
# import random
# from urllib.request import urlretrieve
#
# user = ('bob', 'coder')
# print(f'{user[0]} is a {user[1]}')
#
# User = namedtuple('User', 'name role')  # first name of tuple, then attributes
# user = User(name='bob', role='coder')
# print(user.role)
# users = {'bob': "coder"}
# print(users['bob'])
# # print(users['julian']) keyerror
# # print(users.get("julian")) is None
#
#
# challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
#                    ('mike', 11), ('julian', 8), ('bob', 6)]
#
# print(challenges_done)
# challenges = defaultdict(list)
# for name, challenge in challenges_done:
#     challenges[name].append(challenge)
# print(challenges)
#
# # most common words/or letters
# words = """Asymmetrical sartorial normcore migas direct trade gastropub vaporware neutra before they sold out salvia pork belly blue bottle. Bushwick XOXO air plant before they sold out. 90's scenester prism, microdosing selvage farm-to-table narwhal deep v. Umami hexagon vegan retro.
#
# Kale chips brunch poutine, air plant tbh four loko beard. +1 pinterest chillwave irony kickstarter try-hard cardigan neutra. 90's whatever williamsburg vaporware, hexagon flexitarian viral tousled mlkshk. Flannel YOLO tumeric, tbh pop-up lomo 3 wolf moon godard tote bag taiyaki put a bird on it. Humblebrag craft beer keytar, salvia pok pok occupy normcore."""
# print(Counter(words.split()).most_common(1))
#
# ### deques (decks) stacks and queues
# lst = list(range(10000000))
# deq = deque(range(10000000))
# def insert_and_delete(ds):
#     for _ in range(10):
#         index = random.choice(range(100))
#         ds.remove(index)
#         ds.insert(index,index)
#
# # Named Tuples, Defaultdict, Counter, deque
