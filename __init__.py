from flask import Flask, render_template
import json
import corpus
import generator
import game

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/')
def play():

	# Set seed headlines for game
	seed_headlines = [
        "Leah Vukmir: Trump is bringing people together",
        "Alaska Catholic official orders sexual misconduct review",
        'Florida middle school girls plotted to kill up to 15 students, drink their blood, police say',
        "Republican Katie Arrington on contentious South Carolina race",
        "McSally on how border security impacts Arizona Senate race",
        "Crime, extreme poverty in El Salvador driving migration",
        "Pakistan gets $6 billion from Saudis, still needs IMF loan"
    ]

    # Set corpus headline source, options are:
	# nyt, breitbart, cnn, fox, buzzfeed
	corpus_headlines = "breitbart.dill"

	# Load corpus object into memory and set headlines
	corpus_obj = corpus.Corpus(path='corpus_small.p')
	corpus_obj.set_headlines(corpus_headlines, 200)

	# Load generator object into memory
	generator_obj = generator.Generator(corpus_obj.headlines, seed_headlines)

	# Load game object into memory
	game_obj = game.Game(generator_obj, seed_headlines)

	return render_template('play.html', inputs=json.dumps(game_obj.inputs))
	# return render_template('play.html')