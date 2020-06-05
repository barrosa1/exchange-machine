import random

with open("mechanism/worker/data.txt", "w") as f:

    for i in range(100):
        b = random.randint(0,80)
        t = random.randint(0,80)
        w = random.randint(0,120)

        f.write(str(b) + ";" + str(t) + ";" + str(w) + "\n")