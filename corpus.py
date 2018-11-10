import pickle
import os

class Corpus(object):
    def __init__(self, path):
        self.path = path
        self.corpus = None
        self.headlines = None

        self._set_corpus()

    def _set_corpus(self):

        # Read corpus into object
        with open(self.path, 'rb') as f:
            self.corpus = pickle.load(f)

        return

    def set_headlines(self, source, threshold):

        # Raise exception for unavailable corpus from object
        if not self.corpus:
            raise Exception("Corpus is unvailable.")

        # Raise exception for unavailable supplied source
        if not source or source not in self.corpus:
            raise Exception("Supplied headline source unavailable.")

        # Set headlines from supplied source
        self.headlines = [part for full in [[
            headlines for headlines in self.corpus[source][text]
            if 'document' not in headlines and 'span' not in headlines
        ] for text in self.corpus[source]] for part in full][:threshold]

        return