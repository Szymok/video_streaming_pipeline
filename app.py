import os
import json
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import numpy as np
import requests
from datetime import datetime
import logging
import base64
import cv2
from collections import Counter
import time
# from vision import label_image, extract_text


def query_model(video_path):
	print(video_path)
	img_class = []
	video = cv2.videoCapture(video_path)
	video_name = os.path.basename(video_path).split('.')[0]
	frame_no = 1
	while video.isOpened():
		_, frame = video.read()
		try:
			frame = cv2.resize(frame, (224, 224))
			if frame_no % 3 == 0:
				payload = {
				 'inputs': [{
				  'name': 'metadata-np',
				  'datatype': 'INT32',
				  'shape': [224, 224, 3],
				  'data': frame.flatten().tolist()
				 }]
				}
				response = requests.post(
				 'http://35.238.232.235:8080/v2/models/content-type-example/infer',
				 json=payload)
				# Append results to empty list
				img_class.append(json.loads(response.text)['outputs'][0]['data'][0])
		except:
			print('End of file')
			break

		time.sleep(0.1)
		frame_no += 1
	# Get most frequent classiciation
	occurence_count = Counter(img_class)
	result = occurence_count.most_common(1)[0][0]

	# Close connection to video
	video.release()
	return result


# Socket IO Flask App Setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
