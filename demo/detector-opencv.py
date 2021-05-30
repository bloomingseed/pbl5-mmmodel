import cv2
import numpy as np 
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--webcam', help="True/False", default=False)
parser.add_argument('--play_video', help="Tue/False", default=False)
parser.add_argument('--image', help="Tue/False", default=False)
parser.add_argument('--video_path', help="Path of video file", default="videos/car_on_road.mp4")
parser.add_argument('--image_path', help="Path of image to detect objects", default="Images/bicycle.jpg")
parser.add_argument('--verbose', help="To print statements", default=False)
args = parser.parse_args()
is_verbose = False

def load_yolo():
	p_weights = "backup/obj_8000.weights"
	p_cfg = "cfg/obj.cfg"
	p_names = "data/obj.names"
	classes = []
	with open(p_names, "r") as f:
		classes = [line.strip() for line in f.readlines()]
	net = cv2.dnn.readNet(p_weights, p_cfg)
	layers_names = net.getLayerNames()
	output_layers = [layers_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
	colors = np.random.uniform(0, 255, size=(len(classes), 3))
	return net, classes, colors, output_layers

def load_image(img_path):
	img = cv2.imread(img_path)
	height, width, channels = img.shape
	return img, height, width, channels

def start_webcam():
	cap = cv2.VideoCapture(0)
	return cap


def display_blob(blob):
	'''
		Three images each for RED, GREEN, BLUE channel
	'''
	for b in blob:
		for n, imgb in enumerate(b):
			cv2.imshow(str(n), imgb)

def detect_objects(img, net, outputLayers):			
	blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
	# display_blob(blob)
	net.setInput(blob)
	start = time.time()
	outputs = net.forward(outputLayers)
	elapsed = time.time()-start
	return blob, outputs, elapsed

def get_box_dimensions(outputs, height, width, confidence_threshold=0.3):
	'''Parses through the raw outputs of the neural network, filters object 
	with higher confidence score than the `confidence_threshold` then return 
	the list of bboxes, confidence scores and class ids of the same length''' 
	boxes = []
	confs = []
	class_ids = []
	for output in outputs:
		for detect in output:
			scores = detect[5:] 			# gets list of confidence scores for each class
			class_id = np.argmax(scores) 	# gets class id of highest confidence score
			conf = scores[class_id] 		# gets the confidence score of the class id
			if conf > confidence_threshold: # checks if confidence scores is greater than threshold. This will save us some computations
				center_x = int(detect[0] * width)
				center_y = int(detect[1] * height)
				w = int(detect[2] * width)
				h = int(detect[3] * height)
				x = int(center_x - w/2)
				y = int(center_y - h / 2)
				boxes.append([x, y, w, h])
				confs.append(float(conf))
				class_ids.append(class_id)
	return boxes, confs, class_ids
			
def nms_bboxes(boxes,confs, score_threshold, nms_threshold):
	return cv2.dnn.NMSBoxes(boxes, confs, score_threshold, nms_threshold)

def draw_labels(boxes, confs, colors, class_ids, classes, img, indexes): 
	font = cv2.FONT_HERSHEY_PLAIN
	for i in range(len(boxes)):
		if i in indexes:
			x, y, w, h = boxes[i]
			cfd = confs[i]
			label = str(classes[class_ids[i]])
			color = colors[class_ids[i]]
			# puts rectangle and text directly onto the image object
			cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
			cv2.putText(img, '%s %.6f'%(label,cfd), (x, y - 5), font, 1, color, 1)
	return img

def image_detect(img_path, save_path='predictions.jpg'): 
	cfd_threshold = 0.48	# confidence score threshold for filtering for nms
	nms_threshold = 0.4 	# IoU threshold for non-max supression
	model, classes, colors, output_layers = load_yolo()
	if is_verbose:
		print('Loaded network model. Number of classes = %d:'%len(classes),' '.join(classes))
		print('Per class colors: ',colors)
	image, height, width, channels = load_image(img_path)
	blob, outputs, elapsed = detect_objects(image, model, output_layers)
	print('Prediction done in %.6f'%elapsed)	# debugging
	boxes, confs, class_ids = get_box_dimensions(outputs, height, width, cfd_threshold)
	indexes = nms_bboxes(boxes,confs,cfd_threshold,nms_threshold) 	# performs nms to get final results
	if is_verbose:
		print('Detection outputs:')
		print(type(outputs),len(outputs))
		print(outputs)
		print('Detection results:')
		[print((boxes[i],confs[i],class_ids[i])) for i in range(len(boxes))]
		print('NMS results:')
		print(indexes)
	img = draw_labels(boxes, confs, colors, class_ids, classes, image, indexes)
	cv2.imwrite(save_path,img)

def start_video(video_path):
	model, classes, colors, output_layers = load_yolo()
	cap = cv2.VideoCapture(video_path)
	start = time.time()
	total_frames = 0
	avr_infer_time = 0
	while True:
		ret, frame = cap.read()
		if ret==False: break	# checks if still has next frame
		height, width, channels = frame.shape
		blob, outputs, elapsed = detect_objects(frame, model, output_layers)
		avr_infer_time=(avr_infer_time+elapsed)/2
		total_frames = total_frames+1
		boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
		img = draw_labels(boxes, confs, colors, class_ids, classes, frame)
		cv2.imshow(video_path,img)
		cv2.waitKey(1)
	total_time = time.time()-start
	fps = total_frames/total_time
	cap.release()
	print('FPS:',fps)
	print('Average inference time:',avr_infer_time)
	return fps, avr_infer_time

def webcam_detect():
	model, classes, colors, output_layers = load_yolo()
	cap = start_webcam()
	while True:
		_, frame = cap.read()
		height, width, channels = frame.shape
		blob, outputs = detect_objects(frame, model, output_layers)
		boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
		img = draw_labels(boxes, confs, colors, class_ids, classes, frame)
		cv2.imshow('demo video',img)
		key = cv2.waitKey(1)
		if key == 27:
			break
	cap.release()

if __name__ == '__main__':
	is_verbose = args.verbose	# sets value of global variable to cmd argument value
	if args.webcam:
		if args.verbose:
			print('---- Starting Web Cam object detection ----')
		webcam_detect()
	if args.video_play:
		video_path = args.video_path
		if is_verbose:
			print('Opening '+video_path+" .... ")
		start_video(video_path)
	if args.image:
		image_path = args.image_path
		save_path = 'predictions.jpg'
		if args.verbose:
			print("Opening "+image_path+" .... ")
		image_detect(image_path, save_path)
	
	if is_verbose:
		while cv2.waitKey(1)!=27:pass
	cv2.destroyAllWindows()