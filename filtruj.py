import re

plikstary = 'TWR-SWT-P2.txt'
pliknowy = 'TWR-SWT-P2_filter.txt'

infile = open(plikstary, 'r')
infile_nadpisz = open(pliknowy, 'w')

lines = infile.readlines()
pattern = "interface Gigabitetherne|switchport m|port-con|access vlan"

for line in lines:
    if re.search(pattern, line):
        #wyszukane = line.strip()
        #print(wyszukane)
        infile_nadpisz.write(line)

infile.close()
infile_nadpisz.close()


