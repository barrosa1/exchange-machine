
with open("data.txt", "r") as f, open("../outcome/output.txt", "w") as out:
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








