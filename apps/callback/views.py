# -*- coding: utf-8 -*-
import json

from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.utils.encoding import force_unicode

from forms import CallbackForm


def sanitize(errors):
    dct = dict(
        (str(k),list(force_unicode(a) for a in v)) for k,v in errors.items())
    return dct

def handle_ajax(request, url):
    if not request.POST:
        return HttpResponse(json.dumps({'error':'no post recieved'}))
    else:
        form = CallbackForm(request.POST)
        if form.is_valid():
            callback = form.save(commit=False)
            callback.site = Site.objects.get_current()
            callback.save()
            return HttpResponse(json.dumps({}))
        else:
            
            return HttpResponse(json.dumps({'errors':sanitize(form.errors)}))