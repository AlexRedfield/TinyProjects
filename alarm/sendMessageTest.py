from twilio.rest import Client
import pandas as pd
import datetime
import time
import cv2
import numpy as np
import easygui
import threading

auth_token = pd.read_csv('D:/Documents/token/auth token.txt', header=None)[0][0]
account_sid = pd.read_csv('D:/Documents/token/account sid.txt', header=None)[0][0]
phone_number = pd.read_csv('D:/Documents/token/Sre phone number.txt', header=None)[0][0]
dst_number = pd.read_csv('D:/Documents/token/Dst phone number.txt', header=None)[0][0]



def send_message():
    client = Client(account_sid, auth_token)
    client.messages.create(
        to='+'+str(dst_number),
        body="hello",
        from_=phone_number,
    )
send_message()