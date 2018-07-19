#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import aiy.i18n
import subprocess
import os

aiy.audio.say('What do you want to send?')


import smtplib
from email.mime.text import MIMEText
gmail_user = 'techappledemo@gmail.com'
gmail_password = 'pythonisthebest'


def SendEmail(content):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(gmail_user,gmail_password)
    server.send_message(content)
    server.quit()
    print('Email sent')

def main():
    aiy.i18n.set_language_code('zh-HK')
    recognizer = aiy.cloudspeech.get_recognizer()

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()
    
    
    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        led.set_state(aiy.voicehat.LED.BLINK)
        content = recognizer.recognize()
        led.set_state(aiy.voicehat.LED.OFF)
        print(content)
        
        if not content:
            print('I can not hear that')
        
        elif content =='再見' :
            subprocess.call('sudo service my_assistant_one start',shell=True)
            subprocess.call('sudo service my_assistant_two stop',shell=True)
        
        else:
            msg = MIMEText(content)
            msg['Subject'] = 'Test'
            msg['From'] = gmail_user
            msg['To'] = 'anserbridge@gmail.com'
        
            SendEmail(msg)
            

if __name__ == '__main__':
    main()
