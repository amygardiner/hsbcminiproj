import io
import csv
import re
import math

#opens file
inputFilename = "Tst2022-04-29LOBs"

print("calculating number of lines")
with io.open(inputFilename + ".txt",'r') as lineCounter: #  encoding='utf-8'
    for count, line in enumerate(lineCounter):
        if count % 1566000 == 0:
            print(count / 156600000, "complete")
        pass
total_lines = count
lineCounter.close()

file = io.open(inputFilename + ".txt",'r', encoding='utf-8')

f = open(inputFilename + ".csv", 'w', newline='')
writer = csv.writer(f)

computationTime = (total_lines/156696422)*16.67
print("starting conversion of", total_lines, "lines")
print("this will take roughly", computationTime, "minuites")

percentageOfLines = math.floor(total_lines*0.01)

prevState = "START"
timeValue = 0.0
transaction = ""
transactionValue = 0
transactionAmount = 0
for i in range(total_lines):
    
    if i % percentageOfLines == 0:
        print(round(i / total_lines,2), "complete, roughly", round(computationTime - (round(i / total_lines,2)*computationTime), 2), "minuites left")

    line = file.readline()
    if re.search("[\w].*", line) != None:
        word = list(filter(lambda match: match != '' and match != ' ' and match != '\n', re.findall("\s?[\w\.]*",line)))[0]
        #removes speech marks and commas of time, bid and ask lines
        if not("time" in word or "bid" in word or "ask" in word):
            word = word[1:]   
        
        if prevState == "START":
            prevState = "TIMELABEL"
        elif prevState == "TIMELABEL":
            timeValue = float(word)
            prevState = "TIMEVALUE"
        elif prevState == "TIMEVALUE":
            prevState = "BIDLABEL"
        elif prevState == "BIDLABEL" and word == "ask":
            prevState = "ASKLABEL"
        elif prevState == "BIDLABEL" and word != "ask":
            transaction = "bid"
            transactionValue = int(word)
            prevState = "BIDVALUE"
        elif prevState == "BIDVALUE":
            transactionAmount = int(word)
            writer.writerow([timeValue,transaction,transactionValue,transactionAmount])
            prevState = "BIDAMOUNT"
        elif prevState == "BIDAMOUNT" and word == "ask":
            prevState = "ASKLABEL"
        elif prevState == "BIDAMOUNT" and word != "ask":
            transaction = "bid"
            transactionValue = int(word)
            prevState = "BIDVALUE"
        elif prevState == "ASKLABEL" and word == "time":
            prevState = "TIMELABEL"
        elif prevState == "ASKLABEL" and word != "time":
            transaction = "ask"
            transactionValue = int(word)
            prevState = "ASKVALUE"
        elif prevState == "ASKVALUE":
            transactionAmount = int(word)
            writer.writerow([timeValue,transaction,transactionValue,transactionAmount])
            prevState = "ASKAMOUNT"
        elif prevState == "ASKAMOUNT" and word == "time":
            prevState = "TIMELABEL"
        elif prevState == "ASKAMOUNT" and word != "time":
            transaction = "ask"
            transactionValue = int(word)
            prevState = "ASKVALUE"

f.close()
file.close()
