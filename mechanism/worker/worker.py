#!/usr/bin/env python
import pika

with open("data.txt", "r") as f, open("output.txt", "w") as out:
    for line in f:
        line = line.replace("\n","")
        list = line.split(";")
        b = int(list[0])
        t = int(list[1])
        w = int(list[2])

        b*=4
        t*=9
        w*=4

        out.write(str(b) + ";" + str(t) + ";" + str(w)+ "\n")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()







