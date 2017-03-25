
from io import StringIO

from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.base import ContentFile

import os
import mainSite

from .forms import ImageUploadForm
from .models import ImageSnapshot
from django.conf import settings

from base64 import b64decode
import time
from PIL import Image


# Create your views here.
BASE_DIR = os.path.dirname(mainSite.__file__)

def index(request):
    documents = ImageSnapshot.objects.all()
    print("index")
    return render(request, 'onboarding/onboarding.html', {'documents': documents})


def liste(request):
    # Handle file upload
    print(request.method)
    if request.method == 'POST':
        if request.is_ajax():
            img_txt = request.POST.get('image')
            if img_txt is not None:
                img_txt = img_txt.replace('data:image/png;base64,', '')
                img_txt = img_txt.rstrip(")")
                name = "saved" + str(int(time.time())) + ".png"
                ##############################################
                #fh = open(path + name, "wb")
                #fh.write(b64decode(img_txt))
                #fh.close()
                ##############################################
                #image = Image.open(path + name)
                #tempfile_io = StringIO()
                data = ContentFile(b64decode(img_txt), name)
                #data.save(tempfile_io, format('PNG'))
                #image_file = InMemoryUploadedFile(tempfile_io,
                # None, name, 'image/png', tempfile_io.len, None)
                model = ImageSnapshot(nom=name)
                model.model_pic.save(name, data)
                #model.nom.save(nom=name)
                print(name)
                model.save()

                #return redirect('/onboarding/liste/')

    # Load documents for the list page
    documents = ImageSnapshot.objects.all()
    print(documents)
    # Render list page with the documents and the form
    return render(request, 'onboarding/onboarding.html', {'documents': documents})
