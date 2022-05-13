#import csv
import numpy as np
import pandas as pd
from tqdm import tqdm  # progress bars

lobFeatures = [
    #"Tst2022-01-04LOBsFeatures",
    #"Tst2022-01-05LOBsFeatures",
    #"Tst2022-01-06LOBsFeatures",
    #"Tst2022-01-07LOBsFeatures",
    #"Tst2022-01-10LOBsFeatures",
    #"Tst2022-01-11LOBsFeatures",
    #"Tst2022-01-12LOBsFeatures",
    #"Tst2022-01-13LOBsFeatures",
    #"Tst2022-01-17LOBsFeatures",
    #"Tst2022-01-18LOBsFeatures",
    #"Tst2022-01-19LOBsFeatures",
    #"Tst2022-01-20LOBsFeatures",
    #"Tst2022-01-21LOBsFeatures",
    #"Tst2022-01-24LOBsFeatures",
    #"Tst2022-01-25LOBsFeatures",
    #"Tst2022-01-26LOBsFeatures",
    #"Tst2022-01-27LOBsFeatures",
    #"Tst2022-01-31LOBsFeatures",
    #"Tst2022-02-01LOBsFeatures",
    #"Tst2022-02-02LOBsFeatures",
    #"Tst2022-02-03LOBsFeatures",
    #"Tst2022-02-07LOBsFeatures",
    #"Tst2022-02-08LOBsFeatures",
    #"Tst2022-02-09LOBsFeatures",
    #"Tst2022-02-10LOBsFeatures",
    #"Tst2022-02-11LOBsFeatures",
    #"Tst2022-02-14LOBsFeatures",
    #"Tst2022-02-15LOBsFeatures",
    #"Tst2022-02-16LOBsFeatures",
    #"Tst2022-02-17LOBsFeatures",
    #"Tst2022-02-18LOBsFeatures",
    #"Tst2022-02-21LOBsFeatures",
    #"Tst2022-02-22LOBsFeatures",
    #"Tst2022-02-23LOBsFeatures",
    #"Tst2022-02-24LOBsFeatures",
    #"Tst2022-02-25LOBsFeatures",
    #"Tst2022-02-28LOBsFeatures",
    #"Tst2022-03-01LOBsFeatures",
    #"Tst2022-03-02LOBsFeatures",
    #"Tst2022-03-04LOBsFeatures",
    #"Tst2022-03-08LOBsFeatures",
    #"Tst2022-03-09LOBsFeatures",
    #"Tst2022-03-10LOBsFeatures",
    #"Tst2022-04-29LOBsFeatures",
]

tapesFeatures = [
    #"0401",
    #"0501",
    #"0601",
    #"0701",
    #"1001",
    #"1101",
    #"1201",
    #"1301",
    #"1701",
    #"1801",
    #"1901",
    #"2001",
    #"2101",
    #"2401",
    #"2501",
    #"2601",
    #"2701",
    #"3101",
    #"0102",
    #"0202",
    #"0302",
    #"0702",
    #"0802",
    #"0902",
    #"1002",
    #"1102",
    #"1402",
    #"1502",
    #"1602",
    #"1702",
    #"1802",
    #"2102",
    #"2202",
    #"2302",
    #"2402",
    #"2502",
    #"2802", #why is this not present on aws, it should be
    #"0103",
    #"0203",
    #"0403",
    #"0803",
    #"0903",
    #"1003",
    #"2904",
]

numberOfDocuments = len(lobFeatures)
for i in tqdm(range(numberOfDocuments), total=numberOfDocuments, , colour='green'):

    lobFile = pd.read_csv(lobFeatures[i] + '.csv')
    tapesFile = pd.read_csv(tapesFeatures[i] + '.csv')

    lobFile = lobFile.drop('Unnamed: 0', 1)
    tapesFile.rename(columns = {'TimeInSec':'time'}, inplace = True)

    merged = pd.merge(tapesFile, lobFile, on='time', how='inner')
    merged.to_csv(tapesFeatures[i] + "CombinedFeatures.csv", index=False)