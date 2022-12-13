import numpy as np
from pymongo import MongoClient
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import StandardScaler, Normalizer
import skimage
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
import cv2
import mlflow
import mlflow.sklearn
from skimage import color
from skimage.feature import hog
from urllib.parse import urlparse


class RGB2GrayTransformer(BaseEstimator, TransformerMixin):
	'''
 	Convert array of RGB images to grayscale
	'''

	def __init__(self):
		pass

	def fit(self, X, y=None):
		return self

	def transform(self, X, y=None):
		# print(type(X))
		if type(X) != list and type(X) != np.ndarray:
			img = np.asarray(X.inputs[0].data).reshape(224, 224, 3)
			print(img.shape)
			return np.array([color.rgb2gray(img) for img in X])


class HogTransformer(BaseEstimator, TransformerMixin):
	'''
 	Expects an array of 2d arrays
	Calculates hog features for each img
	'''

	def __init__(self,
	             y=None,
	             orientations=9,
	             pixels_per_cell=(8, 8),
	             cells_per_block=(3, 3),
	             block_norm='L2-Hys'):
		self.y = y
		self.orientations = orientations
		self.pixels_per_cell = pixels_per_cell
		self.cells_per_block = cells_per_block
		self.block_norm = block_norm

	def fit(self, X, y=None):
		return self

	def transform(self, X, y=None):

		def local_hog(X):
			return hog(X,
			           orientation=self.orientations,
			           pixels_per_cell=self.pixels_per_cell,
			           cells_per_block=self.cells_per_block,
			           block_norm=self.block_norm)

		if X.shape == (224, 244):
			X = X.reshape(224, 224)
			return np.array(local_hog(X)).reshape(1, 23328)
		else:
			try:
				print(np.array([local_hog(img) for img in X]).shape)
				return np.array([local_hog(img) for img in X])
			except:
				return np.array([local_hog(img) for img in X])
