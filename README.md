# konserva-27
Geolocating photos. Project for #douhack 2015


## How to run?
Extra step on MacOS
```
rm ./source/images/.DS_Store
rm ./source/test_images/.DS_Store  
```
then
```
python testORB.py
```

## Problem
* Where this photo was made?
Someone makes photo (building, roadblock, field with tanks) and some other wants to locate where that photo was made. Of course, it easy when photo has geo coordinates, but what if it hasn't?

## Technology
* python + opencv
* ORB featuring algorithm (detecting features on photos)
* FLANN (Fast Library for Approximate Nearest Neighbors) matching features on photos

## Demo
* We made a lot of photos inside office
* Then somebody makes **test photo**
* Program responds where **test photo** was made

## What's next?
Use this technology for process important photos from outside

##Installation  
You'll need to have opencv library for python(2.7 was used). All installation steps were taken from [here] (https://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/)

###SciPy  
for installing SciPy - just use `pip install scipy`  
