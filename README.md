# Fact-Finding

This project explores disinformation's dangers by testing whether users can spot fake and automatically-generated news headlines.

## Getting Started

### Requirements

This project uses `Python 3.x`. I recommend install dependencies with the [pip package manager](https://pip.pypa.io/en/stable/installing/).

### Installation

Download this project's code here:
```
$ git clone https://github.com/drewleonard/engl080.git
```
Then, create a virtual environment and install dependencies:
```
$ virtualenv venv
$ source venv/bin/activate/
(venv) $ pip install -r requirements.txt
```

### Usage
To run this project locally, invoke the executable:
```
$ ./run.sh
```
Then, navigate to the local server in your browser. For example:
```
http://127.0.0.1:5000/
```
Adjust the game's input parameters (such as news source) by navigating to:
```
app.py
```

## Built With
* Backend framework: [Python Flask](http://flask.pocoo.org/)
* Backend computation: [Python spaCy](https://spacy.io/)
* Frontend: from-scratch JavaScript, HTML5, and CSS3
* Data source: [Princeton's Center for Information Technology Policy](https://freedom-to-tinker.com/2016/09/14/all-the-news-thats-fit-to-change-insights-into-a-corpus-of-2-5-million-news-headlines/)

## Acknowledgements

I created this project for Dartmouth College's English 080: Writing with Algorithms course, taught by Professor Kyle Booten during Fall Term 2018. Two similar projects provided inspiration: [Bad News](https://getbadnews.com/#intro) and [The New York Times' disinformation quiz](https://www.nytimes.com/interactive/2018/09/04/technology/facebook-influence-campaigns-quiz.html).