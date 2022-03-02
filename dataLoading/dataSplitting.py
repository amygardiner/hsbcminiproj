import io
import codecs
import math
import os

#opens file
inputFilename = "Tst2022-04-29LOBs"
with io.open(inputFilename + ".txt",'r') as f: #  encoding='utf-8'
    for count, line in enumerate(f):
        if count % 1566000 == 0:
            print(count / 156600000)
        pass
total_lines = count
f.close()

max_batch_size = 125000 #125000 file is small enough to be managed, including viewing by text editor
total_full_iterations = math.floor((total_lines / max_batch_size))
remaining = total_lines - (total_full_iterations * max_batch_size)

batches = []
for i in range(total_full_iterations):
    batches.append(max_batch_size)
batches.append(remaining)

print(total_full_iterations+1, "files incoming")

file = io.open(inputFilename + ".txt",'r', encoding='utf-8')

firstLine = file.readline()
unclosedBrackets = False

directory = r"C:/Users/Michael McCoubrey/Documents/DSMP/hsbcminiproj/dataLoading/"+inputFilename
if not os.path.isdir(directory):
    os.mkdir(directory)
    
for i, batch_size in enumerate(batches):
    folderName = "/sampleSubsetPart"
    filename = "sampleSubsetPart" + str(i) + ".txt"
    path = os.path.join(directory, filename)

    outputFile = codecs.open(path, 'w+', 'utf-16-le')
    outputFile.write(firstLine)

    print(i, "of", len(batches), "done")

    for j in range(batch_size):
        unclosedBrackets = False
        entry = []
        while not unclosedBrackets:
            entry.append(file.readline())
            if entry[-1][0] == "]":
                unclosedBrackets = True
        for line in entry:
            if j > 0:
                outputFile.write(line)
file.close()
outputFile.close()