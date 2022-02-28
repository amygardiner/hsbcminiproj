import pandas as pd
import numpy as np
import re
import io

#opens file
file = io.open('sampleLOB.txt','r', encoding='utf-16-le')

firstLine = [file.readline()]
unclosedBrackets = False
entries = [firstLine]

for i in range(2):
    unclosedBrackets = False
    entry = []
    while not unclosedBrackets:
        entry.append(file.readline())
        if entry[-1][0] == "[":
            unclosedBrackets = True
    entries.append(entry)
print(np.array(entries).flatten())

file.close()
