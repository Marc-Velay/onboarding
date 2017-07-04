
from base64 import b64decode
import time
from os import environ, mkdir
from os.path import abspath, basename, dirname, isdir, join, normpath
from sys import path

from django.shortcuts import render
from django.core.files.base import ContentFile
from django.conf import settings
import json, codecs

import mainSite

#from .forms import ImageUploadForm
from .models import ImageSnapshot
#from django.conf import settings

#from PIL import Image

from .ocr import ocr

# Create your views here.
BASE_DIR = dirname(mainSite.__file__)
def index(request):
    readData = json.dumps({"firstName": "", "secondName": "", "lastName": ""})

    if request.method == 'POST':
        if request.is_ajax():
            img_txt = request.POST.get('image')
            if img_txt is not None:
                img_txt = img_txt.replace('data:image/png;base64,', '')
                img_txt = img_txt.rstrip(")")
                name = "saved" + str(int(time.time())) + ".png"
                data = ContentFile(b64decode(img_txt), name)
                model = ImageSnapshot(nom=name)
                model.model_pic.save(name, data)
                readData = ocr(name)
                model.save()
    #ocr("fotodniRotated.jpg")   #rotated the image to display image transform
    #readData = ocr("fotodni.jpg")         #original image 
    readData = ocr("saved1499153129.png") #/home/gniorg/Documents/CIMD/website/onboarding/media/onboarding/saved1499153129.png
    print("two: " + readData)
    documents = ImageSnapshot.objects.all()
    return render(request, 'onboarding/onboarding.html', {'documents': documents, 'readData': readData})


def liste(request):
    # Handle file upload
    if request.method == 'POST':
        if request.is_ajax():
            img_txt = request.POST.get('image')
            if img_txt is not None:
                img_txt = img_txt.replace('data:image/png;base64,', '')
                img_txt = img_txt.rstrip(")")
                name = "saved" + str(int(time.time())) + ".png"
                data = ContentFile(b64decode(img_txt), name)
                model = ImageSnapshot(nom=name)
                model.model_pic.save(name, data)
                readData = ocr(name)
                model.save()
                #return redirect('/onboarding/liste/')

    # Load documents for the list page
    documents = ImageSnapshot.objects.all()
    # Render list page with the documents and the form
    print(readData)
    return render(request, 'onboarding/form.html', {'documents': documents, 'readData': readData})
