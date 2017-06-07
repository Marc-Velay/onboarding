import os
import mainSite
from .transform import four_point_transform
from . import imutils
from skimage.filters import threshold_adaptive
import numpy as np
import cv2
from django.conf import settings

from PIL import Image, ImageDraw, ImageEnhance
import sys

import pyocr
import pyocr.builders

def ocr(name):
    print("ocr")
    ############# get the image to be processed ###################
    image = cv2.imread(os.path.join(settings.MEDIA_ROOT, 'onboarding/') + name, -1)
    #cv2.waitKey(0)
    #pts = np.array([(73, 239), (356, 117), (475, 265), (187, 443)], dtype="float32")
    #warped = four_point_transform(image, pts)
    ratio = image.shape[0]/500.0
    orig = image.copy()
    image = imutils.resize(image, height=600)

    ################ Init the OCR tools #####################
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))
    # Select spanish language
    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    lang = langs[2]
    print("Will use lang '%s'" % (lang))

    ############### Filter image to get a flat grayscale version ################
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (5, 5), 0)
    #edged = cv2.Canny(gray, 75, 200)
    #kernel = np.ones((5,5),np.uint8)
    #dilated = cv2.dilate(edged, kernel, iterations=1)
    # find the contours in the edged image, keeping only the
    # largest ones, and initialize the screen contour
    print("finding contours")
    #(cnts, _) 
    #_, cnts, _= cv2.findContours(dilated.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #print("sorting arrays")
    #cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    '''
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
            print("unclear picture")

    if screenCnt is not 0:
        print("drawing contours")
        cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
        #cv2.imshow("Outline", image)

    warped = four_point_transform(orig, screenCnt.reshape(4, 2)*ratio)
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    #warped = threshold_adaptive(warped, 251, offset=10)
    warped = threshold_adaptive(warped, 15, offset=10)
    warped = warped.astype("uint8") * 255
    '''
    #cv2.imshow('image', image)
    #cv2.imshow('edge', dilated)
    #cv2.imshow("Original", imutils.resize(orig, height=650))
    #cv2.imshow("Scanned", imutils.resize(warped, height=650))

    #pil_im = Image.fromarray(imutils.resize(image, height=1000))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(image)
    pil_copy = pil_im.copy()

    drawNameOne = ImageDraw.Draw(pil_im)
    drawNameOne.line((260,100,430,100), fill=0, width=3)
    drawNameOne.line((260,100,260,145), fill=0, width=3)
    drawNameOne.line((430,100,430,145), fill=0, width=3)
    drawNameOne.line((260,145,430,145), fill=0, width=3)
    areaOne = (260,100,430,145)

    drawNameTwo = ImageDraw.Draw(pil_im)
    drawNameTwo.line((260,140,430,140), fill=0, width=3)
    drawNameTwo.line((260,140,260,185), fill=0, width=3)
    drawNameTwo.line((430,140,430,185), fill=0, width=3)
    drawNameTwo.line((260,185,430,185), fill=0, width=3)
    areaTwo = (260,140,430,185)

    drawNameThree = ImageDraw.Draw(pil_im)
    drawNameThree.line((260,180,430,180), fill=0, width=3)
    drawNameThree.line((260,180,260,225), fill=0, width=3)
    drawNameThree.line((430,180,430,225), fill=0, width=3)
    drawNameThree.line((260,225,430,225), fill=0, width=3)
    areaThree = (260,180,430,225)

    factor = 1.8
    croppedOne = ImageEnhance.Sharpness(pil_copy.crop(areaOne)).enhance(factor)
    croppedTwo = ImageEnhance.Sharpness(pil_copy.crop(areaTwo)).enhance(factor)
    croppedThree = ImageEnhance.Sharpness(pil_copy.crop(areaThree)).enhance(factor)

    ImageEnhance.Sharpness(pil_im).enhance(factor).show()
    croppedOne.show()
    croppedTwo.show()
    croppedThree.show()


    txt = tool.image_to_string(
        pil_im,
        #imutils.resize(warped, height=650),
        lang="spa",
        builder=pyocr.builders.TextBuilder()
    )

    nameOne = tool.image_to_string(
        croppedOne,
        #imutils.resize(warped, height=650),
        lang="spa",
        builder=pyocr.builders.TextBuilder()
    )
    nameTwo = tool.image_to_string(
        croppedTwo,
        #imutils.resize(warped, height=650),
        lang="spa",
        builder=pyocr.builders.TextBuilder()
    )
    lastName = tool.image_to_string(
        croppedThree,
        #imutils.resize(warped, height=650),
        lang="spa",
        builder=pyocr.builders.TextBuilder()
    )
    print (txt)
    print("\n\n\n" + nameOne)
    print("\n\n\n" + nameTwo)
    print("\n\n\n" + lastName)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return
