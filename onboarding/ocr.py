import os
import mainSite
from .transform import four_point_transform
from . import imutils
from skimage.filters import threshold_adaptive
import numpy as np
import cv2
from django.conf import settings

def ocr(name):
    print("ocr")
    image = cv2.imread(os.path.join(settings.MEDIA_ROOT, 'onboarding/') + name, -1)
    cv2.waitKey(0)
    #pts = np.array([(73, 239), (356, 117), (475, 265), (187, 443)], dtype="float32")
    #warped = four_point_transform(image, pts)
    ratio = image.shape[0]/500.0
    orig = image.copy()
    image = imutils.resize(image, height=500)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)
    kernel = np.ones((5,5),np.uint8)
    dilated = cv2.dilate(edged, kernel, iterations=1)
    # find the contours in the edged image, keeping only the
    # largest ones, and initialize the screen contour
    print("finding contours")
    #(cnts, _) 
    _, cnts, _= cv2.findContours(dilated.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print("sorting arrays")
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    # loop over the contours
    print("analysing contours")
    for c in cnts:
        # approximate the contour
        print("approximate contours")
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            print("keeping the 4 longest")
            screenCnt = approx
            break
        else:
            screenCnt = 0

    #cv2.imshow('image', image)
    cv2.imshow('edge', dilated)
    if screenCnt is not 0:
        print("drawing contours")
        cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
        cv2.imshow("Outline", image)
    else:
        print("unclear picture")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return
