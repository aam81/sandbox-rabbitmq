#!/usr/bin/env python
import pika
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
	print " [x] Received %r - %s" % (body, datetime.datetime.now().strftime('%M:%S.%f'))
	
channel.basic_consume(callback, queue='hello', no_ack=True)

print " [x] Waiting for messages. To exit press CTRL+C"
channel.start_consuming()