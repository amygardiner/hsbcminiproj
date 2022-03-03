import csv

inputFilename = "Tst2022-01-13LOBs"
with open(inputFilename + ".csv", mode ='r')as file:
   
  # reading the CSV file
  reader = csv.reader(file)
 
  tabularData = []
  for i, row in enumerate(reader):
      tabularData.append( [int(i), int(float(row[0])/0.016), float(row[0]), row[1], int(row[2]), int(row[3])])

file.close()
print("data loaded")


#we now need to the start and end time of a bid or ask
def createEntryWithStartAndEndTime(tabularData):
    initialEntryOfInterest = tabularData[0]
    startDate = tabularData[0][2]
    endDate = -1
    print("step 1 -", len(tabularData))
    rowsOfInterest = list(filter(lambda e: e[-3:] == initialEntryOfInterest[-3:], tabularData))
    print("step 2 -", len(rowsOfInterest))
    historyOfAnEntry = []
    
    for i, row in enumerate(rowsOfInterest):
        if (i+1)==len(rowsOfInterest) or row[1] == rowsOfInterest[i+1][1]:
            historyOfAnEntry = historyOfAnEntry + rowsOfInterest[:i+1]
    if len(historyOfAnEntry) != 0:
        endDate = historyOfAnEntry[-1][2]
    else:
        historyOfAnEntry.append(initialEntryOfInterest)
        endDate = -1
    print("step 3")
    
    indexesToDelete = list(map(lambda row: row[0], historyOfAnEntry))

    for i, indexDel in enumerate(indexesToDelete):
        tabularData.pop(indexDel - i)
        if i % 3500 == 0:
            print(round(i / len(indexesToDelete), 5))

    print("step 4 -", len(tabularData), [startDate, endDate] + initialEntryOfInterest[3:])
    return [startDate, endDate] + initialEntryOfInterest[3:], tabularData

def compressDataToStartAndEndTime(tabularData):
    data = tabularData
    print("size of Data left to analyse:", len(data))
    
    compressed = []
    while data != []:
        entry, data = createEntryWithStartAndEndTime(data)
        compressed.append(entry)
    
    return np.array(compressed)
    
compressed = compressDataToStartAndEndTime(tabularData) # this would take roughly 18 days to complete


if len(tabularData)>0: #its possible irrelevant data is filtered out leaving an empty list
    #Now we just need to save the data as a csv file
    dict = {
        'Start_Time': np.array(compressed)[:,0],
        'End_Time': np.array(compressed)[:,1],
        'Transaction': np.array(compressed)[:,2],
        'Value': np.array(compressed)[:,3],
        'Amount': np.array(compressed)[:,4],
    }  

    df = pd.DataFrame(dict)
    df.to_csv(inputFilename + "compressed.csv") 
