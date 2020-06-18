#!/usr/bin/env python
with open("output.txt", "r") as f, open("result.txt", "w") as out:
    for line in f:
        line = line.replace("\n","")
        list = line.split(";")
        b = int(list[0])
        t = int(list[1])
        w = int(list[2])

        score = b + t + w

        out.write(str(score) + "\n")
