import csv

def load_data(_csv):
    reader = csv.reader(_csv, delimiter=",")
    titles = []
    data1 = []
    for row in reader:
        if len(titles) == 0:
            titles = row
            data1 = [[] for n in range(len(titles))]
            continue
        for i,item in enumerate(row):
            try:
                item = float(item)
            except ValueError:
                pass
            data1[i].append(item)
    return titles, data1

def difference(val1,val2):
    return [val2[i]-val1[i] for i in range(min(len(val1),len(val2)))]

def mean(v):
    if type(v[0]) in [int,float]:
        return sum(v) / len(v)
    else:
        classes = {}
        for val in v:
            if val in classes:
                classes[val] += 1
            else:
                classes[val] = 1
        
        keys = list(classes.keys())
        denom = sum(classes[i] for i in keys)
        total = 0
        for i,k in enumerate(keys):
            total += (i+1) * classes[k]

        return keys[round(total/denom)-1]

weather1fname = "London/1-9-22_to_31-10-22.csv"
weather2fname = "London/1-9-23_to_8-10-23.csv"

with open(weather1fname) as weather1csv:
    titles,data1 = load_data(weather1csv)

with open(weather2fname) as weather2csv:
    titles,data2 = load_data(weather2csv)


while True:
    n = int(input(">"))
    print(f"VARIABLE: {titles[n]}")
    if type(data1[n][0]) not in [int,float]:
        print(mean(data1[n]), mean(data2[n]), end="\n\n")
    else:
        diff = difference(data1[n],data2[n])
        print(f"MEAN DIFF: {round(mean(diff),2)}", end="\n\n")
