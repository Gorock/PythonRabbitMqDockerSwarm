#!/usr/bin/env python
import pika
import time as time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbit'))
channel = connection.channel()


channel.queue_declare(queue='hello')
while 1:
    time.sleep(1)
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello World!')
    print(" [x] Sent 'Hello World!'")
connection.close()
