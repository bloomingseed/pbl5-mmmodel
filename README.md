# Subject
Objects and relatives detection for the blind.

# Hardware
- Raspberry Pi model 4B
- Buzzer
- Pi camera module version 1.3

# Machine learning
- Algorithm: Tiny YOLOv3.
- Classes: person, car, motorcycle, vinh. Where **vinh** is face of one of our members.

# Training process
- See [this notebook](https://colab.research.google.com/drive/1wuYGz38-dK94IGQjCZiHkMZ4fpauw1Gs?usp=sharing)

# Results
- Performance (Processor: Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (8 CPUs), ~2.0GHz)
    - Average FPS: 23
    - Average inference time: 23.291ms
class_id = 0, name = person, ap = 51.31%
class_id = 1, name = car, ap = 47.52%
class_id = 2, name = motorbicycle, ap = 55.44%
class_id = 3, name = vinh, ap = 99.19%
for conf_thresh = 0.25, precision = 0.70, recall = 0.37, F1-score = 0.48
IoU threshold = 30 %, used Area-Under-Curve for each unique Recall 
 mean average precision (mAP@0.30) = 0.633643, or 63.36 %