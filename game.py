import random
import json

class Game(object):

	def __init__(self, generator_obj, seed_headlines):
		self.generator_obj = generator_obj
		self.seed_headlines = seed_headlines
		self.inputs = None

		self._set_inputs()

	def _get_choice(self):
		choice = True if random.choice([0, 1]) else False
		return choice

	def _set_inputs(self):
		
		# Raise exception for unavailable source data
		if not self.generator_obj or not self.seed_headlines:
			raise Exception("Unavailable source data.")

		# Initialize array for inputs
		self.inputs = []

		# Iterate over seed headlines
		for seed_headline in self.seed_headlines:
			
			# Get choice value
			choice = self._get_choice()

			# Generate false headline if True
			# Keep original headline if False
			seed_headline = self.generator_obj.get_headline(seed_headline) if choice else seed_headline

			# Decode to ascii
			# seed_headline = seed_headline.encode('ascii','ignore')

			# Store randomized seed headline in inputs
			self.inputs.append([choice,json.dumps(seed_headline)])

		return


