
from base64 import b64decode
import time
from os import environ, mkdir
from os.path import abspath, basename, dirname, isdir, join, normpath
from sys import path

from django.shortcuts import render
from django.core.files.base import ContentFile
from django.conf import settings

import cv2
import mainSite

#from .forms import ImageUploadForm
from .models import ImageSnapshot
#from django.conf import settings

#from PIL import Imag

from .ocr import ocr

# Create your views here.
BASE_DIR = dirname(mainSite.__file__)
def index(request):
    documents = ImageSnapshot.objects.all()
    #ocr("fotodniRotated.jpg")   #rotated the image to display image transform
    #ocr("fotodni.jpg")         #original image
    return render(request, 'onboarding/onboarding.html', {'documents': documents})


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
                ocr(name)
                model.save()

                #return redirect('/onboarding/liste/')

    # Load documents for the list page
    documents = ImageSnapshot.objects.all()
    # Render list page with the documents and the form
    return render(request, 'onboarding/onboarding.html', {'documents': documents})
