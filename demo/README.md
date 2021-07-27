# How to run demo
- Download 3 files from [here](https://drive.google.com/drive/folders/1eetPsLEvx_528NWy1EauEc-Mq7LOYfFx?usp=sharing).
- Extract the zip file then put .weights file to backup folder, .cfg to cfg, .names to data.
- Run detector_opencv_pi.py if using on Raspberry Pi, or run detector_opencv.py otherwise.

# Command line arguments
```
python3 detector_opencv_pi.py option
```
Where option is one of:
--camera: Takes True or False value
--video_path: Takes a path to video file
--image_path: Takes a path to image file. For this option, you can also specify --output_path which takes a path to save output image which will have bounding boxes and confidence scores on the image
--is_verbose: Takes True or False value. Default is True and it will prints detection results and the filtering process to console (terminal).

# Demo results
- See images `results-demo-?.jpg` and `results-demo-console.jpg`.
- Performance:
    - Average inference time: 960ms
    - Minimal total interval: 1532ms
    - Each detection takes minimal notification time: 500ms
    - Max FPS: 1.042