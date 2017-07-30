# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Mapp, Crossing1
import json
from import_files import *
from django.shortcuts import render, redirect
from forms import DataForm
from import_files import *
import json
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
            result = api_call(cam1, cam2, cam3, cam4)
            print result
            return render(request, 'disp.html', {'cam1':cam1, 'cam2':cam2 , 'cam3':cam3, 'cam4':cam4, 'result':result})
        else:
            return render(request, 'data.html')


def api_call(cam1,cam2,cam3,cam4):
    app = image_analyzer(api_key=get_your_own_key)
    model = app.models.get('traffic density')
    # images = [
    #     'https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/mado5ne/high-density-traffic-on-downtown-street-of-moscow_xyx5u3du__F0000.png',
    #     'https://report.az/storage/news/a1451c765f2344226690c36551b6b29a/39e6afde-526c-42cf-9354-cead17b0d93b.jpg',
    #     'http://timesofindia.indiatimes.com/thumb/msid-37055677,width-400,resizemode-4/37055677.jpg',
    #     'http://download-ets2.com/uploads/posts/2015-09/1441462911_ets2_00077.png']
    images = [cam1, cam2, cam3, cam4]
    emergency = {}
    low = {}
    high = {}
    n = 0
    for i in range(0, len(images)):
        image = Image(url=images[i])
        data = model.predict([image])
        with open('repo_data.json', 'w') as outfile:
            json.dump(data, outfile)
        print data
        print "\n\n"
        x = data['outputs'][0]['data']['concepts'][0]['name']
        y = data['outputs'][0]['data']['concepts'][0]['value']
        c = "cam" + str(i + 1)
        if x == 'ambulance' or x == 'fire':
            emergency[c] = y
        elif x == 'low density':
            low[c] = y
        elif x == 'high density':
            high[c] = y
    print emergency
    print high
    print low
    flag = 0
    str1 = ''
    if emergency:
        max_value = max(emergency.itervalues())
        z = [k for k in emergency if emergency[k] == max_value]
        del emergency[''.join(z)]
        # print ''.join(z) + "  is green for 20 seconds and then red for 60 seconds"
        str1 = str1 + ''.join(z) + "  is green for 20 seconds and then red for 60 seconds" + "<br>"
        flag = 1
        for l in range(0, len(emergency)):
            max_value1 = max(emergency.itervalues())
            z1 = [k1 for k1 in emergency if emergency[k1] == max_value1]
            n = n + 20
            # print ''.join(z1) + " is red for " + str(n) + " seconds and then green for 20 seconds"
            str1 = str1 + ''.join(z1) + " is red for " + str(n) + " seconds and then green for 20 seconds" + "<br>"
            del emergency[''.join(z1)]
    if high:
        max_value = max(high.itervalues())
        z = [k for k in high if high[k] == max_value]
        del high[''.join(z)]
        if flag == 1:
            n = n + 20
            # print ''.join(z) +  " is red for " + str(n) + " seconds and then green for 20 seconds"
            str1 = str1 + ''.join(z) + " is red for " + str(n) + " seconds and then green for 20 seconds" + "<br>"
        else:
            flag = 1
            str1 = str1 + ''.join(z) + "  is green for 20 seconds and then red for 60 seconds" + "<br>"
        for l in range(0, len(high)):
            max_value1 = max(high.itervalues())
            z1 = [k1 for k1 in high if high[k1] == max_value1]
            n = n + 20
            # print ''.join(z1) + " is red for " + str(n) + " seconds and then green for 20 seconds"
            str1 = str1 + ''.join(z1) + " is red for " + str(n) + " seconds and then green for 20 seconds" + "<br>"
            del high[''.join(z1)]
    if low:
        min_value = max(low.itervalues())
        z = [k for k in low if low[k] == min_value]
        del low[''.join(z)]
        if flag == 1:
            n = n + 20
            # print ''.join(z) +  " is red for " + str(n) + " seconds and then green for 20 seconds"
            str1 = str1 + ''.join(z) + " is red for " + str(n) + " seconds and then green for 20 seconds" + "<br>"
        else:
            str1 = str1 + ''.join(z) + "  is green for 20 seconds and then red for 60 seconds" + "<br>"
        for l in range(0, len(low)):
            min_value1 = max(low.itervalues())
            z1 = [k1 for k1 in low if low[k1] == min_value1]
            n = n + 20
            print ''.join(z1) + " is red for " + str(n) + " seconds and then green for 20 seconds"
            del low[''.join(z1)]

    return str1


