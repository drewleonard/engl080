import random
import spacy


class Generator(object):
    def __init__(self, headlines, threshold_entity, threshold_chunk):

        self.headlines = headlines
        self.threshold_entity = threshold_entity
        self.threshold_chunk = threshold_chunk
        self.map_entity = None
        self.map_chunk = None

        self.nlp = spacy.load('en')

    def _get_attributes(self, doc):

        entities = [
        	entity for entity in doc.ents
        	if len(self.nlp(e.text)) > self.entity_threshold
    	]
	    chunks = [
	        chunk for chunk in doc.noun_chunks
	        if len(self.nlp(chunk.text)) > self.chunk_threshold
	    ]

    	return entities, chunks

	def _map_kv(self, kv_map, k, v):
		if k not in kv_map:
			kv_map[k] = set()
		kv_map[k].add(v)

    def _set_maps(self):

        # Raise exception if headlines are unavailable
        if not self.headlines:
            raise Exception("No headlines to build maps from.")

        # Initialize maps
        self.map_entity = {}
        self.map_chunk = {}

        # Iterate over headlines
        for headline in self.headlines:

            # Decode text as unicode
            if not isinstance(headline, unicode):
                headline = headline.decode('utf-8')

            # Mark headline with spacy.nlp()
            doc = self.nlp(headline)

            # Get doc's attributes
            entities, chunks = self._get_attributes(doc)

            # Map entities
            [
            	self._map_kv(self.map_entity,entity.label_,entity.text) for
            	entity in entities
            ]

            # Map chunks
            [
            	self._map_kv(self.map_entity,chunk.root.dep_,chunk.text) for
            	chunk in chunks
            ]

            # Iterate over and set entities
         #    for entity in entities:
         #        self._map_kv(self.map_entity,entity.label_,entity.text)
        	# for chunk in chunks:
         #        self._map_kv(self.map_entity,chunk.root.dep_,chunk.text)


