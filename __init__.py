from flask import Flask, render_template
import corpus
import generator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/')
def play():

	source_headlines = "nyt.dill"

	# Load corpus object into memory and set headlines
	corpus_obj = corpus.Corpus(path='corpus_small.p')
	corpus_obj.set_headlines(source_headlines)

	# Load generator object into memory
	generator_obj = generator.Generator(corpus_obj.headlines[:100])
	print(generator_obj.map_entity)
	print(generator_obj.map_chunk)

	return render_template('play.html')