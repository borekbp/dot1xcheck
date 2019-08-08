import re

def poukladaj(switchname):
    ####################################################
    # filtruj tylko potrzebne wpisy
    # replace wpisy na podsumowania
    # liniuj ustawienia interfejsow w jednym wierszu
    ####################################################
    plikstary = switchname + ".txt"
    pliknowy = switchname + "_filtruj.txt"
    infile = open(plikstary, 'r')
    infile_nadpisz = open(pliknowy, 'w+')

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
                                    re.sub("interface Gigabitethernet", switchname+"_Gi",
                                    line.replace('\n', ' '))))))))).replace('TWR', '\nTWR')

            infile_nadpisz.write(x1)

    infile.close()
    infile_nadpisz.close()


def znajdzzleinterfejsy(switchname):
    ##########################################
    # odrzuc interfejsy dobrze skonfigurowane
    # zapisz tylko nazwy interfejsów
    ##########################################
    plikfiltruj = switchname + "_filtruj.txt"

    infile10 = open(plikfiltruj, 'r')
    infile_nadpisz20 = open("ALL_bad_Interfaces.txt", 'a+')

    lines2 = infile10.readlines()

    for line2 in lines2:
        if 'vlan_ok dot1x_ok mode_access \n' not in line2:
            TWRwords = str(re.findall(r"\b[TWR]\S+", line2)).replace("'", '').replace("[", '').replace("]", '')
            infile_nadpisz20.write((TWRwords) + '\n')
    infile10.close()
    infile_nadpisz20.close()


def utworzblackliste():
    SWallInt = 'ALL_bad_Interfaces.txt'
    SWallowed = 'ALL_int_whitelist.txt'
    SWblacklist = 'ALL_int_blacklist.txt'

    deffile = open(SWblacklist, 'w+')

    ###########################
    #wczytaj pliki do tablicy
    ###########################

    lineListAll = list()
    lineListalowed = list()
    lineListAll = [line.rstrip('\n') for line in open(SWallInt)]
    lineListalowed = [line.rstrip('\n') for line in open(SWallowed)]


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

    deffile.close()



#####################
# wlasciwy program
#####################

TWRallInt = "ALL_switch_check.txt"
infile_nadpisz20 = open("ALL_bad_Interfaces.txt", 'w').close()
przelacznikiL2 = list()
przelacznikiL2 = [line.rstrip('\n') for line in open(TWRallInt)]

xx = 1
for xx in range(len(przelacznikiL2)):
    poukladaj(przelacznikiL2[xx])
    znajdzzleinterfejsy(przelacznikiL2[xx])
    xx += 1
utworzblackliste()




