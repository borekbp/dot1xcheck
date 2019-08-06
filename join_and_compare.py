import re
plikstary = 'TWR-SWT-P2_odrzuc.txt'
pliknowy3 = 'TWR-SWT-P3_odrzuc.txt'
TWRallInt = 'TWR-SWT-allINT.txt'
TWRalowed = 'TWR-SWT-alowed.txt'
TWRdef = 'TWR-SWT_def.txt'

infile = open(plikstary, 'r')
outfile = open(pliknowy3, 'r')
deffile = open(TWRdef, 'w+')

lines1 = infile.readlines()


#####################
# połącz pliki
#####################

filenames = [plikstary, pliknowy3]
with open(TWRallInt, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())


###########################
#wczytaj pliki do tablicy
###########################

lineListAll = list()
lineListalowed = list()
lineListAll = [line.rstrip('\n') for line in open(TWRallInt)]
lineListalowed = [line.rstrip('\n') for line in open(TWRalowed)]


##########################################
# wyszukaj interfejsy poza white-lista
# zapisz wyszukane interfejsy do pliku
##########################################

tabela1len = int(len(lineListAll))
pozawhitelist = []
x10 = 0
while x10 < tabela1len:
    if lineListAll[x10] not in lineListalowed: pozawhitelist.append(lineListAll[x10])
    else: pass
    x10 += 1

xx = 0
for xx in range(int(len(pozawhitelist))):
    deffile.write(pozawhitelist[xx] + "\n")
    xx +=1

infile.close()
outfile.close()
deffile.close()


