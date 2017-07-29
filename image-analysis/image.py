from clarifai.rest import Image
from clarifai.rest import ClarifaiApp
import json

low_traffic  = ['http://condorly.com/wp-content/uploads/2016/05/Ruta_Panamericana_Buenos_Aires_Florida-low-traffic-website-conversion-rate-optimization-condorly.jpg',
'http://static.lakana.com/nxsglobal/feedsite/photo/2017/04/18/7e3d4c0e6c0549c29157f891c699caf5_19815559_ver1.0_640_360.jpg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/787NorthEnd.JPG/220px-787NorthEnd.JPG',
'https://upload.wikimedia.org/wikipedia/commons/e/ed/Southeast_freeway.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtUDLMa6ZIoJmwkih_J-EDMlAwuLXZ4i8qWa6Un9qxKLb8W2oK',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRu-64oCfLuH_OHW_IFowbiFX3GCMSaELVAOnXGhSVfqjYOV-Gu',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXeUYmRpuUiLpFAXjfZeC-X7pcBeOcEeLDzy0WwGMMTDCC253Y',
'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/I-35W_and_Minneapolis_skyline_5.jpg/220px-I-35W_and_Minneapolis_skyline_5.jpg',
'http://www.bikede.org/wp-content/uploads/2012/12/chicago_cycletrack.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7N3VhclUTuFYv-hMqt9UFQnT_0O8aZB6Rgv9MXo3oreQcJaIZ',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbzntryFd2lYgadZXQOD3YS0ZD8fopEmJNz8PqgZQOq_U38djl',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTheM_XF6bjP-OLIhAafQbvJYLWzO2REQ6FUsVdRxTYnLK6JYtljA',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJq65yuPEt-JAQ5Nw_g-H2-b-QBXEcunsQRwArnhT3kyLwrX_mGQ',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-UpbWbvH-r9w6HMfNaIkpzCSrXiX0t-Z0naq06Fyzpkl1_937yQ',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_xcCOJ7fYGeqS4XGV_NuY9_UsxI4HDxBgJoXOFdfGptuOv6rT',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuAVzT_QlWPT932mQ6xHGtRBohHjp9KIrVOFIxNUAQ5VdweIFV',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7fqQPQ_xy4ONfQA9csxlRjGO7EVPcViCCi0cCaMdE3xhhN-cpog',
'https://i.ytimg.com/vi/-S-eH0YEvOQ/maxresdefault.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDCVuYBBjXO2PxZ-kcL5MC0z6wP0Iyi9WAdqiOgyd7kMoHV3rm',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdOanmw5Ue_ML8O_nnie9DiWcW91T3mKBVqBXZT2u_6VcajtM-jA',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSr1wtikbtgQbrXmJJ6NxC2_ROTvBjSh6eQ9Z84lp9TXjyBqGfg',
'http://condorly.com/wp-content/uploads/2016/05/Ruta_Panamericana_Buenos_Aires_Florida-low-traffic-website-conversion-rate-optimization-condorly.jpg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/787NorthEnd.JPG/220px-787NorthEnd.JPG',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlAr_FE71J4G3zum1CfHZZez8Q-TQD-sOxnxv_Q-VXeuz7CyMC',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjMs1IkMJTzEgEdGVn3fHO31Bi7JzPCho1SksOuC5K0BKevcek',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4LAxZCjZuipwsU8kPhWCQF9-6svuii9XEzvGxp7EqC3hCdVXE',
'https://upload.wikimedia.org/wikipedia/commons/e/ed/Southeast_freeway.jpg',
'https://i.ytimg.com/vi/-S-eH0YEvOQ/maxresdefault.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-UpbWbvH-r9w6HMfNaIkpzCSrXiX0t-Z0naq06Fyzpkl1_937yQ',
'http://theexpiredmeter.com/wp-content/uploads/2013/04/Expressway.jpg',
'http://mediad.publicbroadcasting.net/p/kut/files/styles/x_large/public/201109/I-35_Traffic_at_Manor_002.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFFaMYTzksT_YkQBsEVUNBWDqF-eq702GKTSTL80K8P0rS0iC4',
'http://i2.cdn.turner.com/cnn/2009/US/07/08/economy.less.traffic/art.traffic.generic.gi.jpg',
'http://l7.alamy.com/zooms/5dfa00fd727942b284a881f03a2d1728/highway-with-low-traffic-hry0h9.jpg',
'https://d0ctrine.files.wordpress.com/2012/02/img_5964.jpg',
'https://d0ctrine.files.wordpress.com/2012/02/img_5979.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBkNR1Mx5o5d5j3btSg9hOdPtjpVg2DF74jwnL-EN99OBtOH5a',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTb5JjwdL9bN9U3jSFlHOFSE09CWX4TijZfAbwto3v9i8mmdPAM',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBon2r31nKweLgGlQj1mg9Rg1w6b8UsLEi19YoSDk51fSLylUa',
'https://upload.wikimedia.org/wikipedia/commons/e/ed/Southeast_freeway.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbtXUR7Q3_MEDfuNF0_2v20f8SZw7__XWcsT_an3VJcZYzWN7XHw',]

high_traffic = [ 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTl9G7cmSk7EGKpMJGM9w50zVXsj4naO-7_K_cImdlgw2ucy3Ft',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQseDTcp6-ZYbR3CFacIcmxzBSQBKQtWzqwDeJrjiqkYOuk-_d4',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyeC6D3KaX3KbNhn2rIGNtN5nBdho1TvwtZu25eRGWPKGaYZT0',
'http://static.indianexpress.com/m-images/M_Id_353588_vehicles_.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8qICn6TOmTxbIKbHCODxrEvIm6NzY9eOcZ_4Iu-QeI3FVxN0H',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbAkI-Q4xke_aYFweu-MhtLSIVNMXyRn7KYGMw4yGTdoiH2Qvd',
'http://bucurestifm.ro/wp-content/uploads/sites/2/2015/02/trafic_in_bucuresti_89514700_11503400.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZKeSdhBvML_1-rdpYVgcYZJH0QLfZ0nUF5JK0WhwwIflMjib0',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZKeSdhBvML_1-rdpYVgcYZJH0QLfZ0nUF5JK0WhwwIflMjib0',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSmJgMjnFHdRO-LZfe7_iNQh-M7TXq3pD1dQFQWBwjolKN7fIc',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT87wKZhTrsksTnCatjUdDQJZw79_VrBlIelGaKuv5t_KgM6LB4',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWBUdmgZDmWhvryxTxY_TUbK5W3N4ZaDBEYdLYpMRO5Ebtt6sW',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQy77u1A3c-gIHLaOPSGUNJRFNbBHxVovBXFVlCVxyC94U6a8wp',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRC_H0H0exjPhA2Uj1jUEw5MD-8KIgCMBM9e4an0dWHMKFLMjuK',
'https://t12.pimg.jp/012/198/682/1/12198682.jpg',
'https://report.az/storage/news/a1451c765f2344226690c36551b6b29a/39e6afde-526c-42cf-9354-cead17b0d93b.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnT0WFMFXCLYf0OmNQBJp-drGebUo1j6lwWkL2EZB9J0Ea7yL7',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTm_xbdT_gLuYghPUBfcocFgZOCfi41VZxaR1j-0_5gpHY4KStD',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGi72gJGBByZppejQDDOTt94E3OQvxWUzJIjL0zlHnKcC8yH8d',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNwttuJfdYT_vcDMXXjj9jVvkQ16MRLVQpF3pfL5tb6V-EWFLE',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnepE2hK-5kJ2MXb15aqfkCLorddTZfVxk1IMZpiqP01vIKqQI',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcDpEmG2ENsoA8cNCNHDjpmxKA8R0b-5OdSHMmIjoXOflAtq-W',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQc_QK8XRDdYkwyGpd7CixfgANWmx0gAEfKEWzIPkm65RQJSjoc',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRNiqiQZ0gAGcnM0fsqf4Q8pJuCtjkrsrcY3yGTqpjXXBGmeGW',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJLjoRbLYT_9RbdApWAP2jecYWtcTF3DgpWkB0ET8vDIUewFSx',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-TufcXHLPw4uIrqGanN_C8wWeyDy_2LOVQLdJ5Ld9d7MHYRFxLw',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRfJJTMGdn3pG3tC_sINhbZEJDsr_sio2kL7e7OVoCUr3Tmq9lEA',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxDVi0yW_5ghs-wXO0HM3R0e3ueJjHUYBmSeGn6E3Jv9-lAdVYTw',
'http://i.huffpost.com/gen/1324194/images/o-DRIVERS-TRAFFIC-facebook.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_L2PZC6AhOWda-XPc0bFo_8ySk8YrPzl8OAnFtJqeQKSwiPAg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRubnLx7zn7UiMgLBqc846PCz2ELRKYGnQYsQ5Q8A-Zp9LE71HD',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgQ3GsqQ_F6HrKre9ODBT9-X9vAfFdzHTBvhApNxFRCSqQkdRr',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRL_BeyMBDgAoavGKz_d7uLqBmKqNWlQVsuD6Fflzv3sBuwGpMZ',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXreNfS_4vP3NOOTe-duxvJNEvtM7Qkp__XLlfIrf5cOx8BeP4',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWe3RRpluLHiF1goTTFMkC9yW1QgavTGZFiXPwSzHJY_piYkoF',
'http://1.bp.blogspot.com/_1E0UrQfdsGo/SpPfn1wc0eI/AAAAAAAACa8/XGLrBKaH_CE/s400/traffic_jam.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXUo-3e5FFnufvvTkO497bHZ7UAOphS0GAdjPkwmztlUvswTsY',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcayojuUm1HOzACIxa7Lsncy55J6b-ViycE5z2KdN4tEaGVvB4',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbXMILehNvSYxJY2mFwrdQh19H70zZm6J4TuG6I9f-EwhCMR8W',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3NSFiIgNPRovL8hVDxpgqGXOEKuyccEPBzuSBdFEHvMiMzCf4',]



def start():
    app = ClarifaiApp(api_key='f71debd8952246c9bff425da4dfe9966')
    # app.inputs.delete_all()
    # for i in range(0, len(high_traffic)):
    #     try:
    #         app.inputs.create_image_from_url(url=high_traffic[i], concepts=['high density'])
    #         print i
    #     except:
    #         continue
    # for j in range(0, len(low_traffic)):
    #     try:
    #         app.inputs.create_image_from_url(url=low_traffic[j], concepts=['low density'])
    #         print j
    #     except:
    #         continue
    # app.models.create('traffic density', concepts=['high density', 'low density'])
    model = app.models.get('traffic density')
    # model.train()
    image = Image(url='http://images.indianexpress.com/2015/06/kerb-stone-delhi-759.jpg')
    data = model.predict([image])
    with open('repo_data.json', 'w') as outfile:
        json.dump(data, outfile)
    print data

    # model = app.models.get('{model_id}')
    # model.train()

start()