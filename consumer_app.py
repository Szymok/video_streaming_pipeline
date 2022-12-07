import threading
from confluent_kafka import Consumer, KafkaError, KafkaException
from consumer_config import config as consumer_config
from utils import *
from pymongo import MongoClient

import cv2
import numpy as np
import time

class ConsumerThread:
	def __init__(self, config, topic, batch_size, db, videos_map):
		self.config = config
		self.topic = topic
		self.batch_size = batch_size
		self.db = db
		self.videos_map = videos_map

	def read_data(self):
		consumer = Consumer(self.config)
		consumer.subscribe(self.topic)
		self.run(consumer, 0, [], [])

	def run(self, consumer, msg_count, msg_array, metadata_array):
		try:
			img_array2=[]
			while True:
				msg = consumer.poll(0.5)
				if msg == None:
					continue
				elif msg.error() == None:

					# Convert image bytes data to numpy array of dtype uint8
					nparr = np.frombuffer(msg.value(), np.uint8)

					# decode image
					img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
					img = cv2.resize(img, (224, 224))
					msg_array.append(img)
					img_array2.append(msg.value())

					# get metadata
					frame_no = msg.timestamp()[1]
					video_name = msg.header()[0][1].decode('utf-8')

					metadata_array.append((frame_no, video_name))

					# Bulk process
					msg_count += 1
					if msg_count % self.batch_size == 0:
						# predict on batch
						img_array = np.asarray(msg_array)
						img_array = preprocess_input(img_array)
						predictions = self.model.predict(img_array)
						labels = decode_predictions(predictions)

						self.videos_map = reset_map(self.videos_map)