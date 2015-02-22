import os
import numpy as np
import cv2

def detect_features(frame):
        '''detect_features(self, frame) -> keypoints, descrs'''
        detector = cv2.ORB( nfeatures = 1000 )
        keypoints, descrs = detector.detectAndCompute(frame, None)
        if descrs is None:  # detectAndCompute returns descs=None if not keypoints found
            descrs = []
        return keypoints, descrs



def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape)/2)
  rot_mat = cv2.getRotationMatrix2D(image_center,angle,1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape,flags=cv2.INTER_LINEAR)
  return result

# Source dir and result dir (YOU SHOULD CREATE RESULT DIR BY HAND)
imgDir = './source/images'
resultDir = './keypoints-results'


# Iterate over files in a dir
imagesDir = './source/images'
for fn in os.listdir(imagesDir):
    #print os.path.join(imagesDir, fn)
    if os.path.isfile(os.path.join(imagesDir, fn)):
        fName, fExtension = os.path.splitext(fn)
        #print fn, fName, fExtension
        inFile = os.path.join(imagesDir, fn)
        print 'inFile =', inFile

        resFile = os.path.join(resultDir, fName + 'r' + fExtension)
        print 'resFile =', resFile

        # DO SMTH HERE inFile and resFile
        im = cv2.imread(inFile)
        imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        #im = rotateImage(imgray, -90)

        keypoints, descrs = detect_features(imgray)
        im = cv2.drawKeypoints(im, keypoints, color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    
        #corners = cv2.goodFeaturesToTrack(imgray, 20, 0.001, 1)

        # draw corners
        for i in range(len(keypoints)):
            print keypoints[i]

        cv2.imwrite(resFile, im)

        


'''

ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
'''

#cv2.drawContours(im, contours, -1, (0,255,0), 3)



#print contours, hierarchy
