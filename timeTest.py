runTimeFile = open("runTime")
makeTimeFile = open("makeTime")
runTimeLines = runTimeFile.read().splitlines()
makeTimeLines = makeTimeFile.read().splitlines()
runTimeFile.close()
makeTimeFile.close()


totRunTime = 0
totMakeTime = 0

for line in runTimeLines:
    if line[:3] == 'use':
        min = line.find('m')
        sec = 3 + line[4:].find('s')
        currTime = 60*float(line[4:min].replace(',','.')) + float(line[min+1:sec+1].replace(',','.'))
        totRunTime += currTime
    elif line[:3] == 'sys':
        min = line.find('m')
        sec = 3 + line[4:].find('s')
        currTime = 60*float(line[4:min].replace(',','.')) + float(line[min+1:sec+1].replace(',','.'))
        totRunTime += currTime

for line in makeTimeLines:
    if line[:3] == 'use':
        min = line.find('m')
        sec = 3 + line[4:].find('s')
        currTime = 60*float(line[4:min].replace(',','.')) + float(line[min+1:sec+1].replace(',','.'))
        totMakeTime += currTime
    elif line[:3] == 'sys':
        min = line.find('m')
        sec = 3 + line[4:].find('s')
        currTime = 60*float(line[4:min].replace(',','.')) + float(line[min+1:sec+1].replace(',','.'))
        totMakeTime += currTime

print("\n\nTotal maketime was " + str(totMakeTime) + " seconds\n")
print("Total runtime was " + str(totRunTime) + " seconds\n")