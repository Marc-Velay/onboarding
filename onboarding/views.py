
from io import StringIO

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

import os
import onboarding

from .forms import ImageUploadForm
from .models import ImageSnapshot
from django.conf import settings

from base64 import b64decode
import time

# Create your views here.
BASE_DIR = os.path.dirname(onboarding.__file__)

def index(request):
    context = {}
    print("index")
    return render(request, 'onboarding/onboarding.html', context)


def liste(request):
    # Handle file upload
    if request.method == 'POST':
        if request.is_ajax():
            print("saving")
            img_txt = request.POST.get('image')
            if img_txt is not None:
                print("converting")
                img_txt = img_txt.replace('data:image/png;base64,', '')
                img_txt = img_txt.rstrip(")")
                fh = open(os.path.join(BASE_DIR, 'media/onboarding/') + "saved" + str(time.clock()) + ".png", "wb")
                fh.write(b64decode(img_txt))
                fh.close()
                """img.show()
                filename = fs.save("test.png", img)
                uploaded_file_url = fs.url(filename)"""
                """setattr(ImageSnapshot, "model_pic",
                        ContentFile(image, 'test.png'))"""
            return HttpResponseRedirect('/')

    # Load documents for the list page
    documents = ImageSnapshot.objects.all()

    # Render list page with the documents and the form
    return render(request, 'onboarding/onboarding.html', {'documents': documents})
