#!/usr/bin/env python
import pika
import datetime
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"
for i in range(1,10):
	channel.basic_publish(exchange='', routing_key='hello', body=message + '.' * i)
print " [x] Sent %r" % (message, )

connection.close()
