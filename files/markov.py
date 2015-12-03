import random
import numpy as np
 
class Markov(object):
	def __init__(self, open_file, order=3):
		self.cache = {}
		self.order = order
		self.open_file = open_file
		self.words = self.file_to_words()
		self.word_size = len(self.words)
		self.database()
         
        def file_to_words(self):
		self.open_file.seek(0)
		data = self.open_file.read()
		words = np.array(data.split())
		return words

	def add(self, fil, wordlimit):
		fil.seek(0)
		data = fil.read()
		words = np.array(data.split())[:wordlimit]
		self.words = np.hstack((self.words, words)) 
		self.cache = {}
		self.word_size = len(self.words)
		self.database()
            
        
        def triples(self):
		""" Generates triples from the given data string. So if our string were
			"What a lovely day", we'd generate (What, a, lovely) and then
			(a, lovely, day).
		"""
             
                if len(self.words) < self.order:
			return
          
		for i in range(len(self.words) - self.order):
			yield (self.words[i:i+self.order])
                 
	def database(self):
		for ws in self.triples():
			key = tuple(ws[:-1].tolist(),)
			last = ws[-1]
			if key in self.cache:
				self.cache[key].append(last)
			else:
				self.cache[key] = [last]
                          
	def generate_markov_text(self, size=25):
		seed = random.randint(0, self.word_size-self.order)
		ws  = self.words[seed:seed + self.order - 1]
		gen_words = []
		for i in xrange(size):
			gen_words.append(ws[0])
			new_word = random.choice(self.cache[tuple(ws.tolist())])
			ws = np.roll(ws, -1).copy()
			ws[-1] = new_word
		return ' '.join(gen_words)
                      
                        
#input all the texts you want
fi2 = open("textA.txt", "r")
fi5 = open("textB.txt", "r")

m = Markov(fi2, 3)
m.add(fi5, 1000)
print m.generate_markov_text(250)
