
plikstary = 'TWR-SWT-P2_liniowo.txt'
pliknowy = 'TWR-SWT-P2_odrzuc.txt'

infile = open(plikstary, 'r')
outfile = open(pliknowy, 'w')

lines1 = infile.readlines()

for line in lines1:
    if 'vlan_ok dot1x_ok mode_access\n' not in line:
        outfile.write(line)


infile.close()
outfile.close()



