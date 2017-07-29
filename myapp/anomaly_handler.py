from sendgrid.helpers.mail import *
from datetime import datetime
from key_sg import *
import sendgrid



def stray_detection():

    email = raw_input("Enter Authority's Email Address")
    sg = sendgrid.SendGridAPIClient(apikey=write_your_own2)
    from_email = Email("straydetector@thewarrior.in")
    to_email = Email(email)
    subject = "Report of stray animals"
    timestamp = datetime.now()
    message = "At **location** there is a stray animal at Time: " + str(timestamp) + '. Please take necessary action ' \
                                                                                     'soon'
    content = Content("text/plain", message)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    if response.status_code == 202:
        print 'Concerned Authorities have been alerted'


def anomaly_detection():

    email = raw_input("Enter Authority's Email Address")
    sg = sendgrid.SendGridAPIClient(apikey=write_your_own2)
    from_email = Email("accidentdetection@gov.in")
    to_email = Email(email)
    subject = "Report of an accident"
    timestamp = datetime.now()
    message = "At **location** there was an accident at Time: " + str(timestamp) + '\n' \
                                                                                   'Please take necessary action soon\n' \
                                                                                   'Accident Image : %s' %(image_url)
    content = Content("text/plain", message)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    if response.status_code == 202:
        print 'Concerned Authorities have been alerted'

stray_detection()