from flask import Flask, render_template
import pickle
import json
import corpus
import generator
import game
from game import Game

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/play/')
def play():

    game_obj_inputs_path = "game_obj_inputs_5000.p"

    with open(game_obj_inputs_path, 'rb') as f:
        game_obj_inputs = pickle.load(f)

    return render_template('play.html', inputs=json.dumps(game_obj_inputs))

 #    # Set corpus headline source
    # # options: nyt, breitbart, cnn, fox, buzzfeed
    # corpus_headlines = "fox.dill"

    # # Load corpus object into memory and set headlines
    # corpus_obj = corpus.Corpus(path='corpus_small.p')
    # corpus_obj.set_headlines(corpus_headlines, 500)

    # # Load generator object into memory
    # generator_obj = generator.Generator(corpus_obj.headlines)

    # # Load game object into memory
    # game_obj = game.Game(generator_obj, corpus_obj.headlines)

    # Load game object
    # Precomputed with 5000 Fox News headlines
    #
    # This is for speed in loading the game
    #
    # Uncomment block above to use different news source
    # and compute on the spot


if __name__ == '__main__':
    app.run()