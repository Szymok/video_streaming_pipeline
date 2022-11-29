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