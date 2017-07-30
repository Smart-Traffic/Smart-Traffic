# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Mapp, Crossing1
import json
from import_files import *
from django.shortcuts import render, redirect
from forms import DataForm
# Create your views here.

IMAGE_URL = []

# def display(request):
#     if request.method == 'GET':
#         # image_url = request.GET['url']
#         # print image_url
#         app = image_analyzer(api_key=get_your_own_key)
#         model = app.models.get('traffic density')
#         image = Image(url='http://www.dot.ca.gov/cwwp2/data/d4/cctv/image/TV503_W80atCarlson.jpg')
#         data = model.predict([image])
#         with open('repo_data.json', 'w') as outfile:
#             json.dump(data, outfile)
#         print data
#         result = data['outputs'][0]['data']['concepts'][0]['name']
#         # conclusion = Crossing1(density=result)
#         # conclusion.save()
#         return render(request, 'success.html')


def display(request):
    if request.method == 'GET':
        form = DataForm(request.GET)
        if form.is_valid():
            cam1 = form.cleaned_data['cam1']
            cam2 = form.cleaned_data['cam2']
            cam3 = form.cleaned_data['cam3']
            cam4 = form.cleaned_data['cam4']
            print cam1
            return render(request, 'disp.html', {'cam1':cam1, 'cam2':cam2 , 'cam3':cam3, 'cam4':cam4})
        else:
            return render(request, 'data.html')

