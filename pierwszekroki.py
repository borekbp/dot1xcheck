strings = ("_")
newLines = []

plik = 'TWR-SWT-P2_filter'
plikorg = plik + ".txt"
pliknowy = 'TWR-SWT-P2_liniowo.txt'
with open(plikorg) as f:
    try:
        for line in f:
            if any(s in line for s in strings):
                newLines.append(line
                                .replace("\nmode", "dupa")
                               )
    except:
        pass


theFile = open(pliknowy, 'w')
for line in newLines:
    theFile.write(line)
theFile.close()

