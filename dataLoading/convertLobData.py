import io
import csv
import re
import math
from tqdm import tqdm  # progress bars

#opens file
#inputFilename = "Tst2022-01-12LOBs"
inputFilenames = [
    #"Tst2022-01-14LOBs", # at 8034.144 there are lines of 'M's which are clearly erroneous and causeing it to crash
    #"Tst2022-02-04LOBs", # an error about 73% the way through the file
    #"Tst2022-03-07LOBs", # has no data at all
    #"Tst2022-03-03LOBs", # fails 48% in: ValueError: invalid literal for int() with base 10: ''
    #"Tst2022-01-28LOBs", # fails to start, undefined character
    "Tst2022-01-31LOBs",
]
def convertFile(inputFilename):
    num_lines = sum(1 for line in open(inputFilename + ".txt",'r'))

    file = io.open(inputFilename + ".txt",'r', encoding='utf-8')
    
    f = open(inputFilename + ".csv", 'w', newline='')
    writer = csv.writer(f)

    prevState = "START"
    timeValue = 0.0
    transaction = ""
    transactionValue = 0
    transactionAmount = 0
    filePrefix = "converting " + inputFilename
    for line in tqdm(file, total=num_lines, colour='green', desc=filePrefix):

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


for inputFilename in inputFilenames:
    convertFile(inputFilename)