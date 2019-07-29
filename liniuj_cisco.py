
plikstary = 'TWR-SWT-P2_replace.txt'
pliknowy = 'TWR-SWT-P2_liniowo.txt'

infile = open(plikstary, 'r')
outfile = open(pliknowy, 'w')


lines1 = infile.readlines()

for line in lines1:
    int_config = line.replace('\n', ' ').replace('TWR', '\nTWR').replace('access ', 'access').replace('trunk ', 'trunk')
    outfile.write(int_config)


infile.close()
outfile.close()



