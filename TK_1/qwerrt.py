

with open("plot.log", 'r') as text:
    data = text.readlines()
    for i in data:
        d = i.split(",")
        print(d[5].split()[4:8])

