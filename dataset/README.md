# Our dataset
- 4 classes: person, car, motorcycle, vinh. Where vinh is class for one of our members.

# How to prepare the dataset we used
- For person, car and motorcycle classes, we use images from [COCO dataset](https://cocodataset.org/) and we take 2000 images equally separated using `np.linspace` for each such category (person, car, motorcycle).
- For `vinh` dataset, we captured him using phone camera which produced 70 images at 1280x720 resolution. Then for each image, we performed 24 types of image augmenting (i.e. Rotate(0), Rotate(45), Rotate(-45), Rotate(135), Rotate(-135), HorizontalFlip; each further does: scale(.3,.3), scale(-.3,-.3), randomHSV(hue=0,saturation=(10,30),value=(10,50))). This expands our `vinh` dataset to 1680 images total.
- All together, using 80/20 train/test split, our dataset structure is:
    - person: (total, train, test) = (2000,1600,400)
    - car: (2000,1600,400)
    - motorcycle: (2000,1600,400)
    - vinh: (1680,1344,336) ? (1608,1286,322)

# Python code for preparing dataset
- For preparing first 3 classes from COCO dataset, we used [this notebook](https://colab.research.google.com/drive/11bmMNcjb00jYlOPjOk8_AMYH105ZO-AX?usp=sharing)
- For preparing `vinh` dataset, we used `` notebook on captured images inside ? folder.