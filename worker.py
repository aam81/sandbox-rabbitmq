#!/usr/bin/env python
import pika
import datetime
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
	print " [x] Received %r - %s" % (body, datetime.datetime.now().strftime('%M:%S.%f'))
	time.sleep(body.count('.'))
	print " [x] Done"
	ch.basic_ack(delivery_tag = method.delivery_tag)
	
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='hello')

print " [x] Waiting for messages. To exit press CTRL+C"
channel.start_consuming()