Process
A video is recorded in a .webm format directly on a browser through a javascript program.
The video is sent to the web server back-end through the Flask API in a binary format
The video is converted into a .mp4 format for simpler manipulation and stored locally
A kafka stream is sent containing a subset of the images via a Kafka producer
The Kafka stream is received by a cluster and processed by Kafka consumer which stores the data into a local MongoDB
A simple ML model is trained on the data
Outside of training, a clip is directly transformed by the front-end and sent to a server which responds with a classification result, shown on the web browser.
