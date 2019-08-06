import re

plikstary = 'TWR-SWT-P2.txt'
pliknowy = 'TWR-SWT-P2_filtruj.txt'

infile = open(plikstary, 'r')
infile_nadpisz = open(pliknowy, 'w+')

####################################################
# filtruj tylko potrzebne wpisy
# replace wpisy na podsumowania
# liniuj ustawienia interfejsow w jednym wierszu
####################################################

lines = infile.readlines()
pattern = "interface Gigabitetherne|switchport m|port-con|access vlan"

for line in lines:
    if re.search(pattern, line):
        x1 = re.sub(" switchport mode trunk", "mode_trunk",
                                    re.sub(" authentication port-control auto", "dot1x_ok",
                                    re.sub(" switchport mode access", "mode_access",
                                    re.sub(" switchport access vlan ", "vlan_",
                                    re.sub(" switchport access vlan 224", "vlan_ok",
                                    re.sub(" switchport access vlan 228", "vlan_ok",
                                    re.sub(" switchport access vlan 232", "vlan_ok",
                                    re.sub("interface Gigabitethernet", "TWR-SWT-P2_Gi",
                                    line.replace('\n', ' '))))))))).replace('TWR', '\nTWR')

        infile_nadpisz.write(x1)

infile.close()
infile_nadpisz.close()

##########################################
# odrzuc interfejsy dobrze skonfigurowane
# zapisz tylko nazwy interfejsów
##########################################

plikfiltruj = 'TWR-SWT-P2_filtruj.txt'
plikodrzuc = 'TWR-SWT-P2_odrzuc.txt'

infile10 = open(plikfiltruj, 'r')
infile_nadpisz10 = open(plikodrzuc, 'w+')


lines2 = infile10.readlines()

for line2 in lines2:
    if 'vlan_ok dot1x_ok mode_access \n' not in line2:
        TWRwords = str(re.findall(r"\b[TWR]\S+", line2)).replace("'", '').replace("[", '').replace("]", '')
        infile_nadpisz10.write((TWRwords)+'\n')

        print(TWRwords)

infile10.close()
infile_nadpisz10.close()


