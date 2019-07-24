
import re
nameorg = 'TWR-SWT-P2'
plikstary = nameorg + '_filter.txt'
pliknowy = nameorg + '_replace.txt'

infile = open(plikstary, 'r')
infile_replace = open(pliknowy, 'w')

for line in infile: infile_replace.write(re.sub(" switchport mode trunk", "mode_trunk",
                            re.sub(" switchport mode access", "mode_access",
                            re.sub(" authentication port-control auto", "dot1x_ok",
                            re.sub(" switchport access vlan 228", "vlan_ok",
                            re.sub(" switchport access vlan 231", "vlan_ok",
                            re.sub(" switchport access vlan ", "vlan_",
                            re.sub("interface Gigabitethernet", nameorg + "_Gi",
                            line))))))))


infile.close()
infile_replace.close()



