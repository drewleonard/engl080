from flask import Flask, render_template
import json
import corpus
import generator
import game

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
	return render_template('about.html')

@app.route('/play/')
def play():

    # Set corpus headline source
	# options: nyt, breitbart, cnn, fox, buzzfeed
	corpus_headlines = "fox.dill"

	# Load corpus object into memory and set headlines
	corpus_obj = corpus.Corpus(path='corpus_small.p')
	corpus_obj.set_headlines(corpus_headlines, 500)

	# Load generator object into memory
	generator_obj = generator.Generator(corpus_obj.headlines)

	# Load game object into memory
	game_obj = game.Game(generator_obj, corpus_obj.headlines)

	return render_template('play.html', inputs=json.dumps(game_obj.inputs))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)