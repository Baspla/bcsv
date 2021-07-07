#Grüße von Tim

import csv
import sys
import datetime

def process():
    if len(sys.argv) < 2:
        print("Fehlender Datei Parameter")
        return
    f = open(sys.argv[1]+"_s.csv", "w")
    with open(sys.argv[1]) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if len(row)==4:
                if row[3]!="":
                    row.pop(0)
                    row.pop(0)
                    f.write(";".join(row)+"\n")
                    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Zeile: "+str(reader.line_num))
                else:
                    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"] Zeile: "+str(reader.line_num)+" ist leer")
    f.close()
    print("#TimLoben")

if __name__ == '__main__':
    process()

