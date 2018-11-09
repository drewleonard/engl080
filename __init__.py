from flask import Flask, render_template
import corpus

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/')
def play():

	# Load corpus object into memory
	corpus_obj = corpus.Corpus(path='corpus_small.p')
	print(corpus_obj.corpus.keys())

	return render_template('play.html')