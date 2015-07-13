#!/usr/bin/env python
import pika
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

#channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
#print " [x] Sent 'Hello World!'"

print " [x] Send 1000 messages"
start = datetime.datetime.now()
for i in range(0, 1000):
	channel.basic_publish(exchange='', routing_key='hello', body='Hello World! %d' % i)
end = datetime.datetime.now()
print " [x] Sent in %s" % (end - start, )

connection.close()
