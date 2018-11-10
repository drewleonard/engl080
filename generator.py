import random
import spacy

class Generator(object):

    def __init__(self, headlines, threshold_entity=0, threshold_chunk=0):

        self.headlines = headlines
        self.threshold_entity = threshold_entity
        self.threshold_chunk = threshold_chunk
        self.map_entity = None
        self.map_chunk = None

        self.nlp = spacy.load('en')
        self._set_maps()

    def _get_attributes(self, doc):

        entities = [
            entity for entity in doc.ents
            if len(self.nlp(entity.text)) > self.threshold_entity
        ]
        chunks = [
            chunk for chunk in doc.noun_chunks
            if len(self.nlp(chunk.text)) > self.threshold_chunk
        ]

        return entities, chunks

    def _map_kv(self, kv_map, k, v):
        if k not in kv_map:
            kv_map[k] = set()
        kv_map[k].add(v)
        return

    def _decode_text(self, text):

        if not isinstance(text, unicode):
            text = text.decode('utf-8')

        return text

    def _sample_map(self, kv_map, k):

        return random.sample(kv_map[k],1)[0]

    def _set_maps(self):

        # Raise exception if headlines are unavailable
        if not self.headlines:
            raise Exception("No headlines to build maps from.")

        # Initialize maps
        self.map_entity = {}
        self.map_chunk = {}

        # Iterate over headlines
        for headline in self.headlines:

            # Decode headline
            headline = self._decode_text(headline)

            # Mark headline with spacy.nlp()
            doc = self.nlp(headline)

            # Get doc's attributes
            entities, chunks = self._get_attributes(doc)

            # Map entities
            [
                self._map_kv(self.map_entity, entity.label_, entity.text)
                for entity in entities
            ]

            # Map chunks
            [
                self._map_kv(self.map_chunk, chunk.root.dep_, chunk.text)
                for chunk in chunks
            ]

        return

    def get_headline(self, text, replace_entity=True, replace_chunk=True):

        # Raise exception for unavailable maps
        if self.map_chunk is None or self.map_entity is None:
            raise Exception("Unavailable maps for generating headline.")

        # Decode text
        text = self._decode_text(text)

        # Mark text with spacy.nlp()
        doc = self.nlp(text)

        # Get doc's attributes
        entities, chunks = self._get_attributes(doc)

        # Replace entities
        if replace_entity:
            for entity in entities:
                if entity.label_ in self.map_entity:
                    replacement = self._sample_map(self.map_entity, entity.label_)
                    text = text.replace(entity.text, replacement)

        # Replace chunks
        if replace_chunk:
            for chunk in chunks:
                if chunk.root.dep_ in self.map_chunk:
                    replacement = self._sample_map(self.map_chunk, chunk.root.dep_)
                    text = text.replace(chunk.text, replacement)

        return text