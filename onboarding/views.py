from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import os

from .forms import ImageUploadForm
from .models import ExampleModel
# Create your views here.


def index(request):
    context = {}
    print("index")
    return render(request, 'onboarding/onboarding.html', context)


def liste(request):
    # Handle file upload
    print("traitement")
    if request.method == 'POST':
        print("received form")
        if request.is_ajax():
            print("saving")
            image = request.POST.get('image')
            new_img = ExampleModel(model_pic=image)
            new_img.save()
            print("saved")
            # Redirect to the document list after POST
            """reverse('mainSite.onboarding.views.index')"""
            return HttpResponseRedirect('liste/')
    else:
        print("new form sent")
        """form = ImageUploadForm() # A empty, unbound form"""

    # Load documents for the list page
    documents = ExampleModel.objects.all()

    # Render list page with the documents and the form
    return render(request, 'onboarding/onboarding.html', {'documents': documents})
