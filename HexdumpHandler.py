
def readHexDumpFile(filePath):
    combText = ""
    with open(filePath, "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split("|", maxsplit=1)
            if len(parts) > 1:
                text = str(parts[1])[:-2]
                combText = combText + text
    return combText