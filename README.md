# README

## Overview
This project is a demonstration of a video processing pipeline that utilizes various technologies such as JavaScript, Flask, Kafka, and MongoDB. The pipeline is as follows:
1. A video is recorded in .webm format directly on a browser through a JavaScript program.
2. The video is sent to the web server back-end through the Flask API in a binary format.
3. The video is converted into .mp4 format for simpler manipulation and stored locally.
4. A Kafka stream is sent containing a subset of the images via a Kafka producer.
5. The Kafka stream is received by a cluster and processed by Kafka consumer which stores the data into a local MongoDB.
6. A simple ML model is trained on the data.
7. Outside of training, a clip is directly transformed by the front-end and sent to a server which responds with a classification result, shown on the web browser.

## Requirements
- JavaScript
- Flask
- Kafka
- MongoDB

## Usage
To run this project, you need to have all the requirements installed and configured. 
