import tensorflow as tf
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from IPython.display import display
from seaborn import color_palette
import cv2
import os
from yolov3_source import * 

PATH=os.getcwd()
_BATCH_NORM_DECAY = 0.9
_BATCH_NORM_EPSILON = 1e-05
_LEAKY_RELU = 0.1
_ANCHORS = [(10, 13), (16, 30), (33, 23),
            (30, 61), (62, 45), (59, 119),
            (116, 90), (156, 198), (373, 326)]
_MODEL_SIZE = (416, 416)


img_names = [os.path.join(os.getcwd(),'dog.jpg'),os.path.join(os.getcwd(),'office.jpg')]
for img in img_names: display(Image.open(img))
batch_size = len(img_names)
batch = load_images(img_names, model_size=_MODEL_SIZE)
class_names = load_class_names(os.path.join(os.getcwd(),'coco.names'))
n_classes = len(class_names)
max_output_size = 10
iou_threshold = 0.5
confidence_threshold = 0.5

model = Yolo_v3(n_classes=n_classes, model_size=_MODEL_SIZE,
                max_output_size=max_output_size,
                iou_threshold=iou_threshold,
                confidence_threshold=confidence_threshold)

tf.compat.v1.disable_eager_execution()
inputs = tf.compat.v1.placeholder(tf.compat.v1.float32, [batch_size, 416, 416, 3])

detections = model(inputs, training=False)

model_vars = tf.compat.v1.global_variables(scope='yolo_v3_model')
assign_ops = load_weights(model_vars, os.path.join(os.getcwd(),'yolov3.weights'))


with tf.compat.v1.Session() as sess:
    sespys.run(assign_ops)
    detection_result = sess.run(detections, feed_dict={inputs: batch})
    
draw_boxes(img_names, detection_result, class_names, _MODEL_SIZE)
