
import random

rzutmoneta = ["1","1","1","1","1","2"]
jakivlan = ["switchport access vlan 228","switchport access vlan 231","switchport access vlan 50"]

for x1 in range(1,25):
   nazwapliku = "TWR-SWT-P"+str(x1)+".txt"
   f = open(nazwapliku, 'w')
   for x2 in range(1, 49):
      wypadlo = int(rzutmoneta[random.randint(0,5)])
      wypadlo2 = int(rzutmoneta[random.randint(0, 5)])
      wypadlo3 = int(rzutmoneta[random.randint(0, 5)])
      if wypadlo == 2:
         f.write("interface Gigabitethernet1/0/" + str(x2) + "\n")
         f.write(" description uplink\n")
         f.write(" switchport mode trunk\n")
         f.write(" switchport trunk alowed vlan 2-20, 44, 200-299\n")
      if wypadlo == 1:
         f.write("interface Gigabitethernet1/0/" + str(x2) + "\n")
         if wypadlo2 == 2:
            f.write("description ludzik\n")
         f.write(" " + random.choice(jakivlan) + "\n")
         if wypadlo2 == 1:
            f.write(" authentication port-control auto\n")
         f.write(" spanning-tree portfast edge\n")
         f.write(" spanning-tree bpdu-guard enable\n")
         f.write(" authentication order dot1x mab\n")
         f.write(" switchport mode access\n")
      f.write("\n")
   f.close()



