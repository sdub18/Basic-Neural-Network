## Created by Sam DuBois August 6th, 2019
## Following the guide by Michael Nielson found here: http://neuralnetworksanddeeplearning.com/chap1.html

## Libraries
import random
import numpy as np

class Network(object):

	def _init_(self, sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases. = [np.random.randn(y, 1) for y in sizes[1:]]
		self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

