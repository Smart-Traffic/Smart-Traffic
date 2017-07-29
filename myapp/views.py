# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Mapp, Crossing1
import json
from import_files import *
from django.shortcuts import render, redirect
# Create your views here.


def display(request):
    if request.method == 'GET':
        app = image_analyzer(api_key=get_your_own_key)
        model = app.models.get('traffic density')
        image = Image(url='')
        data = model.predict([image])
        with open('repo_data.json', 'w') as outfile:
            json.dump(data, outfile)
        print data
        result = data['outputs'][0]['data']['concepts'][0]['name']
        conclusion = Crossing1(cam_id='cam1', conclusion=result)
        conclusion.save()
        return render(request, 'index.html')

