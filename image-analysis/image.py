from import_files import *
import json
from traffic_data import low_traffic, high_traffic, ambulance, fire


def start():
    app = image_analyzer(api_key=get_your_own_key)
    # app.inputs.delete_all()
    for i in range(0, len(high_traffic)):
        try:
            app.inputs.create_image_from_url(url=high_traffic[i], concepts=['high density'])
            print i
        except:
            continue
    for j in range(0, len(low_traffic)):
        try:
            app.inputs.create_image_from_url(url=low_traffic[j], concepts=['low density'])
            print j
        except:
            continue
    for k in range(0, len(ambulance)):
        try:
            app.inputs.create_image_from_url(url=ambulance[k], concepts=['ambulance'])
            print k
        except:
            continue
    for l in range(0, len(fire)):
        try:
            app.inputs.create_image_from_url(url=fire[l], concepts=['fire'])
            print l
        except:
            continue
    app.models.create('traffic density', concepts=['high density', 'low density', 'ambulance', 'fire'])
    model = app.models.get('traffic density')
    model.train()
    # image = Image(url='http://1.bp.blogspot.com/-EpVRrrrelUY/Tty53P15wrI/AAAAAAAAAFY/aLX9Le2RLno/s1600/PAINTBLOG6.JPG')
    # data = model.predict([image])
    # with open('repo_data.json', 'w') as outfile:
    #     json.dump(data, outfile)
    # print data
    # x = data['outputs'][0]['data']['concepts'][0]['value']
    # y = data['outputs'][0]['data']['concepts'][1]['value']
    # if x > y:
    #     print 'Conclusion = '+ data['outputs'][0]['data']['concepts'][0]['name']
    # else:
    #     print 'Conclusion = ' + data['outputs'][0]['data']['concepts'][1]['name']
    # app.models.create('traffic density', concepts=['high density', 'low density', 'ambulance'])
    # model = app.models.get('traffic density')
    # model.train()
start()
