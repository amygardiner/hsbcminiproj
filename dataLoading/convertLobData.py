import pandas as pd
import numpy as np
import re
import io

#opens file
file = io.open('sampleLOB.txt','r', encoding='utf-16-le')


#stores data from file in array and strips whitespace
data = [line for line in file.readlines() if re.search("[\w].*", line) != None][1:]
file.close()


organisedData = []
#converts to human readable lines
for line in data:
    test = list(filter(lambda match: match != '' and match != ' ' and match != '\n', re.findall("\s?[\w\.]*",line)))
    #print(test)
    for word in list(filter(lambda match: match != '' and match != ' ' and match != '\n', re.findall("\s?[\w\.]*",line))):   
        #removes speech marks and commas of time, bid and ask lines
        if not("time" in word or "bid" in word or "ask" in word):
            word = word[1:]
        organisedData.append(word)

        
def chunkArrayByWord(ls,chunkWord):   
    chunkedData = []
    chunk = []
    for line in ls:
        if line==chunkWord:
            chunkedData.append(chunk)
            chunk = []
        else:
            chunk.append(line)
    return chunkedData

chunkedData = chunkArrayByWord(organisedData, 'time')[1:]

#remove entries where there are no entries in the order log book
chunkedData = list(filter(lambda timeEntry: len(timeEntry)>3, chunkedData))

evenChunkierData = []
for time in chunkedData:
    bidPos = 1 #it will always be 1
    askPos = time.index('ask')
    evenChunkierData.append([time[0], time[bidPos+1:askPos], time[askPos+1:]])

organisedData = []
for time in evenChunkierData:
    bids = []
    asks = []
    for i, bid in enumerate(time[1]):
        if i % 2 != 0:
            bids.append(time[1][i-1:i+1])
    for i, ask in enumerate(time[2]):
        if i % 2 != 0:
            asks.append(time[2][i-1:i+1])
    organisedData.append([time[0], bids, asks])

    
# now we aim to flatten the data into tabular data which we will eventually use for the csv file
tabularData =[]
for time in organisedData:
    for bids in time[1]:
        tabularData.append([
            float(time[0]),
            'bid',
            int(bids[0]),
            int(bids[1])
        ])
    for asks in time[2]:
        tabularData.append([
            float(time[0]),
            'ask',
            int(asks[0]),
            int(asks[1])
        ])
        

#We can save this uncompressed data as csv data
dict = {
    'Time': np.array(tabularData)[:,0],
    'Transaction': np.array(tabularData)[:,1],
    'Value': np.array(tabularData)[:,2],
    'Amount': np.array(tabularData)[:,3],
}  
       
df = pd.DataFrame(dict)
df.to_csv('tabularData.csv')


#we now need to the start and end time of a bid or ask
def createEntryWithStartAndEndTime(tabularData):
    tabularData = list(map(lambda row: [int(row[0]/0.016),row[0],row[1],row[2], row[3]], tabularData))
    initialEntryOfInterest = tabularData[0]
    startDate = tabularData[0][1]
    endDate = -1
    
    rowsOfInterest = list(filter(lambda e: e[-3:] == initialEntryOfInterest[-3:], tabularData))
    historyOfAnEntry = []
    #historyOfAnEntry = [initialEntryOfInterest]
    
    for i, row in enumerate(rowsOfInterest):
        if (i+1)==len(rowsOfInterest) or row[0] == rowsOfInterest[i+1][0]:
            historyOfAnEntry = historyOfAnEntry + rowsOfInterest[:i+1]
    if len(historyOfAnEntry) != 0:
        endDate = historyOfAnEntry[-1][1]
    else:
        historyOfAnEntry.append(initialEntryOfInterest)
        endDate = -1
    
    tabularData = list(map(lambda row: row[1:], filter(lambda row: row not in historyOfAnEntry, tabularData)))
    
    return [startDate, endDate] + initialEntryOfInterest[2:], tabularData

def compressDataToStartAndEndTime(tabularData):
    data = tabularData
    
    compressed = []
    while data != []:
        entry, data = createEntryWithStartAndEndTime(data)
        compressed.append(entry)
    
    return np.array(compressed)
    
compressed = compressDataToStartAndEndTime(tabularData)


#Now we just need to save the data as a csv file
dict = {
    'Start_Time': np.array(compressed)[:,0],
    'End_Time': np.array(compressed)[:,1],
    'Transaction': np.array(compressed)[:,2],
    'Value': np.array(compressed)[:,3],
    'Amount': np.array(compressed)[:,4],
}  
       
df = pd.DataFrame(dict)
df.to_csv('compressedTabularData.csv') 