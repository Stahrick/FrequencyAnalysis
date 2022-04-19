from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from HexdumpHandler import readHexDumpFile


def drawPlot(xArr1, yArr1, xArr2, yArr2):
    plt.subplot(1,2,1)
    plt.bar(xArr1,yArr1)
    plt.title("Absolute Values")

    plt.subplot(1,2,2)
    plt.bar(xArr2, yArr2)
    plt.title("Percentage Values")

    plt.show()

def countFrequency(text:str):
    countDict = {}
    for letter in text:
        if letter in countDict:
            countDict[letter] = countDict[letter] + 1
        else:
            countDict[letter] = 1
    return countDict

def freqPercentage(freqDict, textLen):
    percDict = {}

    for k,v in freqDict.items():
        percDict[k] = v / textLen
    return percDict

def sortDict(dic):
    sortedDict = {}
    for i in sorted(dic):
        sortedDict[i] = dic[i]
    return sortedDict


dumpFilePath = (Path(__file__).parent / "hexdump.txt").resolve()
textFile = readHexDumpFile(dumpFilePath)
counter = countFrequency(textFile.lower())
#sortCounter = sortDict(counter) #sort for keys
sortCounter = dict(sorted(counter.items(), key=lambda x:x[1])) #sort for values
counterPerc = freqPercentage(sortCounter, len(textFile))
drawPlot(sortCounter.keys(), sortCounter.values(), counterPerc.keys(), counterPerc.values())