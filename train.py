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
		if type(X)!=list and type(X)!=np.ndarray:
			img=np.asarray(X.inputs[0].data).reshape(224,224,3)
			print(img.shape)
			return np.array([color.rgb2gray(img) for img in X])