
from base64 import b64decode
import time
from os import environ, mkdir, remove
from os.path import abspath, basename, dirname, isdir, join, normpath
from sys import path

from django.shortcuts import render
from django.core.files.base import ContentFile
from django.conf import settings
from django.http import JsonResponse
import json, codecs
from datetime import datetime, timedelta

import mainSite

#from .forms import ImageUploadForm
from .models import ImageSnapshot, UserContact
#from django.conf import settings

#from PIL import Image

from .ocr import ocr

# Create your views here.
BASE_DIR = dirname(mainSite.__file__)


def index(request):
    print("index")

    documents = ImageSnapshot.objects.all()
    userdata = UserContact.objects.all()
    print(documents)
    print(userdata)
    return render(request, 'onboarding/onboarding.html', {'documents': documents, 'userData': userdata})


def doc_scan(request):
    print("doc_scan")
    readData = json.dumps(
        {"first_name": "", "last_name": "", "nationality": "", "doe": "", "dob": "", "sex": "", "dni": ""})
    if request.method == 'POST':
        if request.is_ajax():
            img_front_txt = request.POST.get('frontImage')
            img_back_txt = request.POST.get('backImage')
            if img_back_txt is not None and request.POST.get('state') == "back":
                #Back of DNI processing and saving
                img_back_txt = img_back_txt.replace('data:image/png;base64,', '')
                img_back_txt = img_back_txt.rstrip(")")
                name_back = "back" + str(int(time.time())) + ".png"
                data = ContentFile(b64decode(img_back_txt), name_back)
                model = ImageSnapshot(nom=name_back)
                model.model_pic.save(name_back, data)
                readData = ocr(name_back)
                remove(join(settings.MEDIA_ROOT, 'onboarding/') + name_back)
                model.save()
                print("proc back image")
                if readData == "error":
                    return JsonResponse({'error_msg': "Please rescan the document"})
                return JsonResponse({'response': readData})
            if img_back_txt is not None and img_front_txt is not None and request.POST.get('state') == "form":
                data = json.loads(request.POST.get('userData'))
                print(data['first_name'])
                tmpDate = datetime(year=int(data['dob'][0:2]), month=int(data['dob'][2:4]), day=int(data['dob'][4:6]))
                data['dob'] = tmpDate
                tmpDate = datetime(year=int(data['doe'][0:2]), month=int(data['doe'][2:4]), day=int(data['doe'][4:6]))
                data['doe'] = tmpDate

                user, created = UserContact.objects.get_or_create(dni=data['dni'], defaults=data)
                print(user)
                print()
                print(created)
                img_back_txt = img_back_txt.replace('data:image/png;base64,', '')
                img_back_txt = img_back_txt.rstrip(")")
                name_back = "back" + str(int(time.time())) + ".png"
                data = ContentFile(b64decode(img_back_txt), name_back)
                user.back_pic.save(name_back, data)
                img_front_txt = img_front_txt.replace('data:image/png;base64,', '')
                img_front_txt = img_front_txt.rstrip(")")
                name_front = "front" + str(int(time.time())) + ".png"
                data = ContentFile(b64decode(img_front_txt), name_front)
                user.front_pic.save(name_front, data)
                user.save()

    return render(request, 'onboarding/form.html', {'readData': readData})



'''
manage.py makemigrations
manage.py migrate

object, created Person.objects.get_or_create(nif=nif, defaults=data)'''