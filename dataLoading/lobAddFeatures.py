import csv
import numpy as np
import pandas as pd 

inputFilenames = [
    #"Tst2022-01-14LOBs", # at 8034.144 there are lines of 'M's which are clearly erroneous and causeing it to crash
    #"Tst2022-02-04LOBs", # an error about 73% the way through the file
    "Tst2022-01-26LOBs",
]

for inputFilename in inputFilenames:

    fileLineCounter = open(inputFilename + ".csv", mode='r')
    readerLineCounter = csv.reader(fileLineCounter)

    #calculate number of lines
    numLines = 0
    for row in readerLineCounter:
        numLines += 1
    fileLineCounter.close()
    print(numLines)

    file = open(inputFilename + ".csv", mode='r')
    reader = csv.reader(file)

    time = []

    numOfBids = []
    bidAvg = []
    bidIqr = []
    bidBestPrice = []
    bidQuantityAtBestPrice = []
    bidQuantAvg = []
    bidQuantIqr = []

    numOfAsks = []
    askAvg = []
    askIqr = []
    askBestPrice = []
    askQuantityAtBestPrice = []
    askQuantAvg = []
    askQuantIqr = []

    QuotedSpread = []
    MidPrice = []
    MicroPrice = []

    prevTime = ''
    entriesOfIntrest = []
    for i, row in enumerate(reader):
        if i == 0:
            prevTime == row[0]
        elif i % (round(numLines*0.01)) == 0:
            print(round(i/numLines, 2), "complete, ", 50 - round(i/numLines, 2)*50, "minuites to go")
        
        if prevTime != row[0]:
            bids = np.array(list(filter(lambda row: row[1] == "bid", entriesOfIntrest)))
            asks = np.array(list(filter(lambda row: row[1] == "ask", entriesOfIntrest)))

            time.append(prevTime)
            if len(bids) > 0:
                numOfBids.append(len(bids))
                bidPrices = bids[:,2].astype(float)
                bidAvg.append(np.median(bidPrices))
                bidQuartile1 = np.percentile(bidPrices, 25)
                bidQuartile3 = np.percentile(bidPrices, 75)
                bidIqr.append(bidQuartile3 - bidQuartile1)
                bidBestPrice.append(np.max(bidPrices))

                bidQuantityAtBestPrice.append(np.max( bids[:,2:].astype(float), axis = 0)[1])

                bidQuantities = bids[:,3].astype(float)
                bidQuantAvg.append(np.median(bidQuantities))
                bidQuantQuartile1 = np.percentile(bidQuantities, 25)
                bidQuantQuartile3 = np.percentile(bidQuantities, 75)
                bidQuantIqr.append(bidQuantQuartile3 - bidQuantQuartile1)
            else:
                numOfBids.append(0)
                bidAvg.append(0)
                bidIqr.append(0)
                bidBestPrice.append(0)

                bidQuantityAtBestPrice.append(0)

                bidQuantAvg.append(0)
                bidQuantIqr.append(0)
                

            if len(asks) > 0:
                numOfAsks.append(len(asks))
                askPrices = asks[:,2].astype(float)
                askAvg.append(np.median(askPrices))
                askQuartile1 = np.percentile(askPrices, 25)
                askQuartile3 = np.percentile(askPrices, 75)
                askIqr.append(askQuartile3 - askQuartile1)
                askBestPrice.append(np.min(askPrices))

                askQuantityAtBestPrice.append(np.min( asks[:,2:].astype(float), axis = 0)[1])

                askQuantities = asks[:,3].astype(float)
                askQuantAvg.append(np.median(askQuantities))
                askQuantQuartile1 = np.percentile(askQuantities, 25)
                askQuantQuartile3 = np.percentile(askQuantities, 75)
                askQuantIqr.append(askQuantQuartile3 - askQuantQuartile1)
            else:
                numOfAsks.append(0)
                askAvg.append(0)
                askIqr.append(0)
                askBestPrice.append(0)

                askQuantityAtBestPrice.append(0)

                askQuantAvg.append(0)
                askQuantIqr.append(0)
            
            #Spread Indicators
            QuotedSpread.append(askBestPrice[-1] - bidBestPrice[-1])
            MidPrice.append((askBestPrice[-1] + bidBestPrice[-1]) / 2)
            if (askQuantityAtBestPrice[-1] + bidQuantityAtBestPrice[-1]) > 0:
                MicroPrice.append(round((askQuantityAtBestPrice[-1] * askBestPrice[-1] + bidQuantityAtBestPrice[-1] * bidBestPrice[-1]) / (askQuantityAtBestPrice[-1] + bidQuantityAtBestPrice[-1]), 2))
            else:
                MicroPrice.append(0)

            entriesOfIntrest = [row]
            prevTime = row[0]
        else:
            entriesOfIntrest.append([float(row[0]), row[1], float(row[2]), int(row[3])])

    file.close()

    df = pd.DataFrame({
        'time': time,
        'MicroPrice': MicroPrice,
        'MidPrice': MidPrice,
        'QuotedSpread': QuotedSpread,
        'bidAvg': bidAvg,
        'bidIqr': bidIqr,
        'bidBestPrice': bidBestPrice,
        'bidQuantityAtBestPrice': bidQuantityAtBestPrice,
        'bidQuantAvg': bidQuantAvg,
        'bidQuantIqr': bidQuantIqr,
        'numberOfBids': numOfBids,
        'askAvg': askAvg,
        'askIqr': askIqr,
        'askBestPrice': askBestPrice,
        'askQuantityAtBestPrice': askQuantityAtBestPrice,
        'askQuantAvg': askQuantAvg,
        'askQuantIqr': askQuantIqr,
        'numberOfAsks': numOfAsks,
    })
    df.to_csv(inputFilename + "Features.csv")