#!/usr/bin/env python
import random
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
with open("mechanism/worker/data.txt", "w") as f:

    for i in range(100):
        b = random.randint(0,80)
        t = random.randint(0,80)
        w = random.randint(0,120)

        #f.write(str(b) + ";" + str(t) + ";" + str(w) + "\n")
    channel.basic_publish(exchange='', routing_key='hello', body=data.txt)
print(" [x] Sent 'Hello World!'")
connection.close()
