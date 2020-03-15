# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:11:42 2020

@author: vgopalja
"""

#pip install confluent_kafka
from confluent_kafka import Producer, Consumer
import config as cfg
import ssl
import sys
import threading
import logging
import time
import json


#a = 'C:/Users/vgopalja.PARTNERS/.spyder-py3/cert/kafkatt1.p12'
#c = 'C:/Users/vgopalja.PARTNERS/.spyder-py3/cert/kafkatt1.p12'
#d = 'C:/Users/vgopalja.PARTNERS/.spyder-py3/cert/ciscoprodtruststore.pem'

a = '/cert/kafkatt1.p12'
c = '/cert/kafkatt1.p12'
d = '/cert/ciscoprodtruststore.pem'

class MsgProducer:
	def __init__(self):
	     self.conf = {'bootstrap.servers': cfg.brokerlist,
		'security.protocol':'ssl',
		'ssl.key.location' : a,
		'ssl.key.password' : 'password',
		'ssl.certificate.location' : c,
		'ssl.ca.location': d}

	#assuming data is already encoded when it comes in
	def produce(self, data):
		producer = Producer(**self.conf)
		producer.produce(cfg.topic, data)
		producer.flush()

if __name__ == '__main__':
	# data = sys.argv[1] #for now just a sentence
    """
    try:
        temp = sys.argv[1]
        if len(sys.argv) > 2:
            for loc in range(2, len(sys.argv)):
                temp += " " + sys.argv[loc]
        data = temp
    except:
        sys.exit ('You need to add a message. If you have multiple words, enclose the entire message in double quotes.')
        
        """
    data = 'a'
    print(cfg.brokerlist)
    print(cfg.sslpath+cfg.producer_keyname)
    print(cfg.producer_keypass)
    print(cfg.sslpath+cfg.producer_certname)
    print(cfg.sslpath+cfg.trustedcachain)
    msgproducer = MsgProducer()
    msgproducer.produce(data)
    