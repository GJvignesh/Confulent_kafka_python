# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 08:15:21 2020

@author: vgopalja
"""


import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "/cert/"
abs_file_path = script_dir + rel_path


#brokerlist = 'vm-ceph-kafka-001:9093,vm-ceph-kafka-002:9093,vm-ceph-kafka-003:9093' ## comma separated broker url 
brokerlist = 'msg-brk-dc3-001:9093' ## comma separated broker url 
sslpath = abs_file_path ## Path where you store the certs
#sslpath = "/Users/sayyadur/Desktop/certs/" ## Path where you store the certs
#trustedcachain = "1int2root-chain.cert.pem" # CA Trusted cert chain. first intermediate pem, second root cert
trustedcachain = "client-ssl.properties.prod" # CA Trusted cert chain. first intermediate pem, second root cert
topic = "sankara.topic.12" ## Topic name 

## Producer
producer_certname = "kafkatt1.p12" ## Producer application Cert name
producer_keyname = "kafkatt1.p12" ## Producer application cert private key
producer_keypass = "password" ## Producer application cert password

## Consumer 
consumer_certname = "kafkatt2.p12" ## Consumer application Cert name
consumer_keyname = "kafkatt2.p12" ## Consumer application cert private key
consumer_keypass = "password" ## Consumer application cert password
consumer_groupid = "sankaratest" ## Consumer group id

file = "\cert\test.txt"


#print(script_dir)
#print(rel_path)
#print(abs_file_path)

f = open(abs_file_path,"a")
print(f.read())