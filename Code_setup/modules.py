import time
import os
import requests
import cv2
import numpy as np
import tensorflow as tf
import argparse 

# Import utilites
from flask import Flask, flash, render_template, Response, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
# from object_detection.utils import label_map_util
# from object_detection.utils import visualization_utils as vis_util

# for object detection.
PERSON_MODEL = "ssd_inception_v2.pb"

# Path to label map file
PERSON_LABELS = "label_map.pbtxt"

# Number of classes the object detector can identify
PERSON_CLASSES = 1 

filename = None

# Person count labelmap.
# load pbtxt file.		

# label_map = label_map_util.load_labelmap(PERSON_LABELS)
# categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=PERSON_CLASSES, use_display_name=True)
# category_index = label_map_util.create_category_index(categories)

#Person Count Detection Model.
# Load the Tensorflow model into memory.
detection_graph= tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PERSON_MODEL, 'rb') as fid:
       	serialized_graph = fid.read()
       	od_graph_def.ParseFromString(serialized_graph)
       	tf.import_graph_def(od_graph_def, name='')


# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')
	
