#!/usr/bin/python
import os
import numpy as np
import cv2
from scipy import ndimage
from scipy import misc
import scipy

# rotation angle in degree

from plane_tracker import PlaneTracker

SCALE_DOWN_COEF = 0.5

def rotateImage(image, angle):
    return ndimage.rotate(image, angle)


def track_from_file(input_image_file, check_images_dir, result_dir):
    print "Tracking", input_image_file
    tracker = PlaneTracker()

    # ------------ INPUT IMAGE
    input_image = cv2.imread(input_image_file)
    input_image = cv2.resize(input_image, (0,0), fx=SCALE_DOWN_COEF, fy=SCALE_DOWN_COEF)
    # input_image = rotateImage(input_image, -90)
    input_image_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    height, width = input_image.shape[:2]
    # ------------

    tracker.clear()
    tracker.add_target(input_image_gray, (0, 0, width, height))

    # ----------------
    for fn in os.listdir(check_images_dir):
        # print os.path.join(imagesDir, fn)
        filename = os.path.join(check_images_dir, fn)

        if os.path.isfile(filename):
            print "Checking", filename

            fName, fExtension = os.path.splitext(fn)
            inpfName, _ = os.path.splitext(os.path.split(input_image_file)[1])

            # print fn, fName, fExtension
            inFile = os.path.join(check_images_dir, fn)
            # print 'inFile =', inFile

            resFile = os.path.join(result_dir, inpfName + 'r' + fName + fExtension)
            # print 'resFile =', resFile

            # DO SMTH HERE inFile and resFile
            im = cv2.imread(inFile)
            im = cv2.resize(im, (0,0), fx=SCALE_DOWN_COEF, fy=SCALE_DOWN_COEF)
            # im = rotateImage(im, -90)
            imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


            # im = rotateImage(imgray, -90)

            # draw corners
            # for i in range(len(corners)):
            # print i, corners[i][0]
            #     cv2.circle(im, (corners[i][0][0], corners[i][0][1]), 50, (0,255,0), 8)


            # track & match features
            tracked = tracker.track(imgray)

            if tracked:
                print "Tracked generation started"

                resImage = np.zeros((height, width * 2, 3), np.uint8)
                resImage[:height, :width] = input_image
                resImage[:height, width:width * 2] = im

                # keypoints = tracked[0].target.keypoints
                # resImage = cv2.drawKeypoints(resImage, keypoints, color=(0, 255, 0),
                #                                     flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

                for tr in tracked:
                    for p0, p1 in zip(tr.p0, tr.p1):

                        from_point = (int(p0[0]), int(p0[1]))
                        to_point = (int(p1[0] + width), int(p1[1]))
                        cv2.line(resImage, from_point, to_point, color=(255, 0, 0))

                cv2.imwrite(resFile, rotateImage(resImage, -90))

                print 'images ', input_image_file, 'and', filename, ' are similar', ' len.p0=', len(
                    tracked[0].p0), ' len.p1=', len(tracked[0].p1)

                print_apropriate_room(filename)
                # else:
                #     print 'images are not similar'
                print "Tracked generation finished"

def print_apropriate_room(input_image_filename):
	coordinates_file = open('./source/coords', 'r')
	for line in coordinates_file:
		name, coordx, coordy, direction, room = line.split(" ")
		dot, source, images, filename = input_image_filename.split('/')
		if (name == filename):
			print '\nroom name :', room, 'coordx :', coordx, '\ncoordy :', coordy, '\n'


for fn in os.listdir('./source/test_images'):
    # print os.path.join(imagesDir, fn)
    filename = os.path.join('./source/test_images', fn)
    track_from_file(filename, './source/images', './results/orb')





