import csv

inputFilename = "Tst2022-04-29LOBs"
with open(inputFilename + ".csv", mode ='r')as file:
   
  # reading the CSV file
  reader = csv.reader(file)
  #tabularData = [line for line in reader]
  tabularData = list(map(lambda row: [int(float(row[0])/0.016), float(row[0]), row[1], int(row[2]), int(row[3])], reader))
file.close()
#tabularData = list(map(lambda row: [float(row[0]), row[1], int(row[2]), int(row[3])], tabularData))
print("data loaded")


#we now need to the start and end time of a bid or ask
def createEntryWithStartAndEndTime(tabularData):
    #tabularData = list(map(lambda row: [int(row[0]/0.016),row[0],row[1],row[2], row[3]], tabularData))
    initialEntryOfInterest = tabularData[0]
    startDate = tabularData[0][1]
    endDate = -1
    print("step 1 -", len(tabularData))
    rowsOfInterest = list(filter(lambda e: e[-3:] == initialEntryOfInterest[-3:], tabularData))
    print("step 2 -", len(rowsOfInterest))
    historyOfAnEntry = []
    
    for i, row in enumerate(rowsOfInterest):
        print(round(i/len(rowsOfInterest),2))
        if (i+1)==len(rowsOfInterest) or row[0] == rowsOfInterest[i+1][0]:
            historyOfAnEntry = historyOfAnEntry + rowsOfInterest[:i+1]
    if len(historyOfAnEntry) != 0:
        endDate = historyOfAnEntry[-1][1]
    else:
        historyOfAnEntry.append(initialEntryOfInterest)
        endDate = -1
    print("step 3")
    
    tabularData = list(map(lambda row: row[:], filter(lambda row: row not in historyOfAnEntry, tabularData)))
    print("step 4 -", len(tabularData), [startDate, endDate] + initialEntryOfInterest[2:])
    return [startDate, endDate] + initialEntryOfInterest[2:], tabularData

def compressDataToStartAndEndTime(tabularData):
    data = tabularData
    print("size of Data left to analyse:", len(data))
    
    compressed = []
    while data != []:
        entry, data = createEntryWithStartAndEndTime(data)
        compressed.append(entry)
    
    return np.array(compressed)
    
compressed = compressDataToStartAndEndTime(tabularData)


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
